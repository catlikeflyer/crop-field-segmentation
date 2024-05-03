import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
import sys

from library import *
parseGraph = None
draw = False
NODE_COUNTER = 0

def add_node(attr):
    global parseGraph
    global NODE_COUNTER
    attr["counter"] = NODE_COUNTER
    parseGraph.add_node( NODE_COUNTER , **attr)
    NODE_COUNTER += 1

    return parseGraph.nodes[NODE_COUNTER-1]

symbol_table = dict()

symbol_table["e"] = 2.718281828459045
symbol_table["max"] = max

symbol_table["load_image"] = load_image
symbol_table["save_image"] = save_image
symbol_table["gen_matrix"] = gen_matrix
symbol_table["gen_vector"] = gen_vector
symbol_table["show_image"] = show_image
symbol_table["show_histogram"] = show_histogram
symbol_table["watershed_segmentation"] = watershed_segmentation 
symbol_table["grabcut_segmentation"] = grabcut_segmentation
symbol_table["template_matching"] = template_matching
symbol_table["canny_edge_detection"] = canny_edge_detection

PLUS_OP = 1
MINUS_OP = 2
TIMES_OP = 3
DIVIDE_OP = 4

tokens = (
    'NUMBER',
    'VARIABLE',
    'SETTO',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXP',
    'LPAREN',
    'RPAREN',
    'LSQUARE',
    'RSQUARE',
    'COMMA',
    'STRING',
    'CONNECT',
    'WATERSHED',
    'GRABCUT',
    'TEMPLATEMATCHING',
    'CANNYEDGEDETECTION',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SETTO = r'='
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COMMA = r','
t_CONNECT = r'\->'


def t_NUMBER(t):
    r'\d+\.?\d*'

    if( t.value.find(".") > -1 ):
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[A-Za-z]([A-Za-z0-9_])*'
    return t

def t_STRING(t):
    r'\"(.)*\"'
    t.value = t.value[1:-1]

    return t

### ------------------------------------ boilerplate start
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_error(t):
    print("Error on analysis")
    t.lexer.skip(1)
### ------------------------------------ boilerplate end

lexer = lex.lex()

precedence = (
    ('left', 'LSQUARE', 'RSQUARE'),  # Precedencia para la indexación de lista
    ('left', 'SETTO')  # Precedencia para la asignación de lista
)


def p_assignment_assign(p):
    '''
    assignment : VARIABLE SETTO expression
    '''

    node = add_node( {'type':'ASSIGN' , 'label':'=' , 'value':''} )
    node_variable = add_node( {'type':'VARIABLE_ASSIGN' , 'label':f'VAR_{p[1]}' , 'value':p[1]} )
    parseGraph.add_edge(node["counter"] , node_variable["counter"])
    parseGraph.add_edge(node["counter"] , p[3]["counter"])
    p[0] = node

def p_assignment_flow(p):
    '''
    assignment : VARIABLE SETTO flow
    '''
    global symbol_table
    symbol_table[p[1]] = p[3]
    p[0] = p[3]

def p_flow_form(p):
    '''
    flow : VARIABLE CONNECT flow_functions
    '''
    p[0] = {"function": p[1], "params": p[3]}

def p_flow_functions(p):
    '''
    flow_functions : flow_function_call CONNECT flow_functions
    '''
    p[0] = [p[1]] + p[3]

def p_flow_function(p):
    '''
    flow_functions : flow_function_call
    '''
    p[0] = [p[1]]

def p_flow_function_call(p):
    '''
    flow_function_call : VARIABLE LPAREN RPAREN
    '''
    p[0] = {"function": p[1], "params": []}

def p_assignment_expression(p):
    ''' assignment : expression
    '''
    p[0] = p[1]

def p_expression_plus(p):
    """
    expression : expression PLUS term
    """
    node = add_node( {'type':'PLUS' , 'label':'+' , 'value':''} )
    parseGraph.add_edge(node["counter"] , p[1]["counter"])
    parseGraph.add_edge(node["counter"] , p[3]["counter"])
    
    p[0] = node

def p_expression_minus(p):
    """
    expression : expression MINUS term
    """
    node = add_node( {'type':'MINUS' , 'label':'-' , 'value':''} )
    parseGraph.add_edge(node["counter"] , p[1]["counter"])
    parseGraph.add_edge(node["counter"] , p[3]["counter"])

    p[0] = node

def p_expression_term(p):
    """
    expression : term 
                | string
    """
    p[0] = p[1]

def p_string_def(p):
    '''
    string : STRING
    '''
    p[0] =  add_node( {'type':'STRING' , 'label':f'str_{p[1]}' , 'value':p[1]} )

def p_term_times(p):
    '''
    term : term TIMES exponent
    '''
    node = add_node( {'type':'TIMES' , 'label':'*' , 'value':''} )
    parseGraph.add_edge(node["counter"] , p[1]["counter"])
    parseGraph.add_edge(node["counter"] , p[3]["counter"])
    p[0] = node

def p_term_divide(p):
    '''
    term : term DIVIDE exponent
    '''
    node = add_node( {'type':'DIVIDE' , 'label':'/' , 'value':''} )
    parseGraph.add_edge(node["counter"] , p[1]["counter"])
    parseGraph.add_edge(node["counter"] , p[3]["counter"])
    p[0] = node

def p_term_exponent(p):
    '''
    term : exponent
    '''
    p[0] = p[1]

def p_exponent_exp(p):
    '''
    exponent : factor EXP factor
    '''
    node = add_node( {'type':'POWER' , 'label':'POW' , 'value':''} )
    parseGraph.add_edge(node["counter"] , p[1]["counter"])
    parseGraph.add_edge(node["counter"] , p[3]["counter"])
    p[0] = node

def p_exponent_factor(p):
    '''
    exponent : factor
    '''
    p[0] = p[1]

def p_exponent_parent(p):
    '''
    exponent : LPAREN expression RPAREN
    '''
    node = add_node( {'type':'GROUP' , 'label':'( )' , 'value':''} )
    parseGraph.add_edge(node["counter"] , p[2]["counter"])
    p[0] = node

def p_factor_num(p):
    ''' factor : NUMBER
    '''
    p[0] = add_node(  {'type':'NUMBER' , 'label':f'NUM_{p[1]}' , 'value':p[1]} )

def p_factor_id(p):
    ''' factor : VARIABLE
    '''
    p[0] = add_node(  {'type':'VARIABLE' , 'label':f'VAR_{p[1]}' , 'value':p[1]} )
    

def p_factor_function_call(p):
    '''
    factor : function_call
    '''
    p[0] = p[1]


def p_function_call_no_params(p):
    '''
    function_call : VARIABLE LPAREN  RPAREN
    '''
    p[0] = add_node(  {'type':'FUNCTION_CALL' , 'label':f'FUN_{p[1]}' , 'value':p[1]} )


def p_function_call_params(p):
    '''
    function_call : VARIABLE LPAREN params RPAREN
    '''
    #print(p[3])
    node = add_node(  {'type':'FUNCTION_CALL' , 'label':f'FUN_{p[1]}' , 'value':p[1]} )
    for n in p[3]:
        parseGraph.add_edge(node["counter"] , n["counter"])
    p[0] = node

def p_params(p):
    '''
    params : params COMMA expression 
            | expression
    '''
    if( len(p) > 2):
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_function_call_watershed(p):
    '''
    function_call : WATERSHED LPAREN VARIABLE RPAREN
    '''
    p[0] = watershed_segmentation(p[3])

def p_function_call_grabcut(p):
    '''
    function_call : GRABCUT LPAREN VARIABLE RPAREN
    '''
    p[0] = grabcut_segmentation(p[3])

def p_function_call_template_matching(p):
    '''
    function_call : TEMPLATEMATCHING LPAREN VARIABLE COMMA VARIABLE RPAREN
    '''
    p[0] = template_matching(p[3], p[5])

def p_function_call_canny_edge_detection(p):
    '''
    function_call : CANNYEDGEDETECTION LPAREN VARIABLE RPAREN
    '''
    p[0] = canny_edge_detection(p[3])


def p_error(p):
    print("Syntax error on input ", p)

def execute_parse_tree(tree):
    root = tree.nodes[0]
    root_id = 0
    res = visit_node(tree, root_id, -1)
    if( type(res) == int or type(res) == float ):
        print("TREE_RESULT: " , res)

def visit_node(tree, node_id, from_id):
    children = tree.neighbors(node_id)

    res = []
    for c in children:
        if( c != from_id):
            res.append(visit_node(tree, c, node_id) )

    current_node = tree.nodes[node_id]
    # print(f"From Node {node_id}" , res)

    if( current_node["type"] == "INITIAL" ):
        return res[0]

    if( current_node["type"] == "ASSIGN" ):
        symbol_table[ res[0] ] = res[1]
        return res[1]

    if( current_node["type"] == "VARIABLE_ASSIGN" ):
        return current_node["value"]

    if( current_node["type"] == "NUMBER" ):
        return current_node["value"]
    
    if( current_node["type"] == "STRING" ):
        return current_node["value"]
    
    if( current_node["type"] == "PLUS" ):
        return res[0] + res[1]
    
    if( current_node["type"] == "VARIABLE" ):
        return symbol_table[current_node["value"]]
    
    if( current_node["type"] == "MINUS" ):
        return res[0] - res[1]

    if( current_node["type"] == "POWER" ):
        return pow(res[0], res[1])
    
    if(current_node["type"] == "GROUP"):
        return res[0]

    if( current_node["type"] == 'TIMES'):
        return res[0] * res[1]
    
    if( current_node["type"] == 'DIVIDE'):
        return res[0] / res[1]
    
    if( current_node["type"] == "FUNCTION_CALL"):
        v = current_node["value"]
        if v in symbol_table:
            fn = symbol_table[v]

            if( callable(fn) ):
                try:
                    res = fn(*res)
                    return res
                except Exception as e:
                    print(f"Error calling function {v} "  , e)
                    return "Error"
            else:
                print(f"Error  function {v} IS NOT a function ")
                return "Error"
        else:
            fn = search_cv2(v)
            if( fn is not None):
                if( callable(fn) ):
                    try:
                        res = fn(*res)
                        return res
                    except Exception as e:
                        print(f"Error calling function {v} "  , e)
                        return "Error"
                else:
                    print(f"Error  function {v} IS NOT a function ")
                    return "Error"
            else:
                print(f"Error {v} IS NOT on symbol table ")
                return "Error"
                

# Modifica el bucle principal para leer y procesar archivos si se proporcionan como argumentos de línea de comandos
def process_file(filename):
    global parseGraph
    global NODE_COUNTER

    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():  # Saltar líneas en blanco
                continue
            
            try:
                NODE_COUNTER = 0
                parseGraph = nx.Graph()
                root = add_node({"type": "INITIAL", "label": "INIT"})
                result = parser.parse(line)
                parseGraph.add_edge(root["counter"], result["counter"])
                execute_parse_tree(parseGraph)
            except Exception as e:
                print(f"Error en la línea {line_number}: {e}")


parser = yacc.yacc()


# Modifica el bucle principal para leer y procesar archivos si se proporcionan como argumentos de línea de comandos
if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            process_file(filename)
    else:
        while True:
            try:
                data = input(">")
                if data == 'exit':
                    break
                if data == 'symbols':
                    print(symbol_table)
                    continue

            except EOFError:
                break

            if not data: continue

            NODE_COUNTER = 0
            parseGraph = nx.Graph()
            root = add_node({"type": "INITIAL", "label": "INIT"})
            result = parser.parse(data)
            parseGraph.add_edge(root["counter"], result["counter"])

            execute_parse_tree(parseGraph)

print("Finished, accepted")
