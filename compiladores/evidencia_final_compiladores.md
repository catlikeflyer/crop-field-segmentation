# Evidencia Final Compiladores
#### Equipo 7
**Emiliano Cabrera Ruiz**: A01025453
<br>**Do Hyun Nam**: A01025276
<br>**Valter Alejandro Kuhne Hernández**: A01379392

## Gramática
**Rule 0** |     S' -> assignment
<br>**Rule 1** |    assignment -> VARIABLE SETTO expression
<br>**Rule 2** |    assignment -> VARIABLE SETTO flow
<br>**Rule 3** |    flow -> VARIABLE CONNECT flow_functions
<br>**Rule 4** |    flow_functions -> flow_function_call CONNECT flow_functions
<br>**Rule 5** |    flow_functions -> flow_function_call
<br>**Rule 6** |    flow_function_call -> VARIABLE LPAREN RPAREN
<br>**Rule 7** |    assignment -> expression
<br>**Rule 8** |    expression -> expression PLUS term
<br>**Rule 9** |    expression -> expression MINUS term
<br>**Rule 10** |   expression -> term
<br>**Rule 11** |   expression -> string
<br>**Rule 12** |   string -> STRING
<br>**Rule 13** |   term -> term TIMES exponent
<br>**Rule 14** |   term -> term DIVIDE exponent
<br>**Rule 15** |   term -> exponent
<br>**Rule 16** |   exponent -> factor EXP factor
<br>**Rule 17** |   exponent -> factor
<br>**Rule 18** |   exponent -> LPAREN expression RPAREN
<br>**Rule 19** |   factor -> NUMBER
<br>**Rule 20** |   factor -> VARIABLE
<br>**Rule 21** |   factor -> function_call
<br>**Rule 22** |   function_call -> VARIABLE LPAREN RPAREN
<br>**Rule 23** |   function_call -> VARIABLE LPAREN params RPAREN
<br>**Rule 24** |   params -> params COMMA expression
<br>**Rule 25** |   params -> expression
<br>**Rule 26** |   function_call -> WATERSHED LPAREN VARIABLE RPAREN
<br>**Rule 27** |   function_call -> GRABCUT LPAREN VARIABLE RPAREN
<br>**Rule 28** |   function_call -> TEMPLATEMATCHING LPAREN VARIABLE COMMA VARIABLE RPAREN
<br>**Rule 29** |   function_call -> CANNYEDGEDETECTION LPAREN VARIABLE RPAREN
<br>**Rule 30** |   expression -> list
<br>**Rule 31** |   list -> LSQUARE list_items RSQUARE
<br>**Rule 32** |   list_items -> list_items COMMA NUMBER
<br>**Rule 33** |   list_items -> NUMBER
<br>**Rule 34** |   expression -> expression LSQUARE NUMBER RSQUARE
<br>**Rule 35** |   expression -> expression LSQUARE NUMBER RSQUARE SETTO expression

## Funciones Implementadas
CANNYEDGEDETECTION: función de OpenCV
<br>COMMA: caracter ','
<br>CONNECT: expresión regular que busca '->'
<br>DIVIDE: expresión regular que busca '/'
<br>EXP: expresión regular que busca '^'
<br>GRABCUT: función de OpenCV
<br>LPAREN: expresión regular que busca '('
<br>LSQUARE: expresión regular que busca '['
<br>MINUS: expresión regular que busca '-'
<br>NUMBER: expresión regular que busca cualquier número y lo vuelve entero o decimal 
<br>PLUS: expresión regular que busca '+'
<br>RPAREN: expresión regular que busca ')'
<br>RSQUARE: expresión regular que busca ']'
<br>SETTO: expresión regular que busca '='
<br>STRING: expresión regular que busca cualquier string que se encuentre entre comillas dobles '"'
<br>TEMPLATEMATCHING: función de OpenCV
<br>TIMES: expresión regular que busca '*'
<br>VARIABLE: expresión regular que busca cualquier string que no empiece con números y no tenga comillas dobles
<br>WATERSHED: función de OpenCV

## Expresiones de Prueba
#### Operadores
![Precedencia de operadores](./doc_images/tree1.png)
#### Funciones
![Funciones](./doc_images/funcs.png)
#### Variables
![Asignacion de variables](./doc_images/vars.png)
#### Flujos de imagenes
![Flujos de imagenes](./doc_images/image_flow.png)
#### Filtros OpenCV
![Filtros OpenCV](./doc_images/filter.png)


## Arboles de sintaxis
### Para archivo instrucciones.py donde se pusieron a prueba los filtros OpenCV 

Expresión en la línea 1: image = load_image("C:\\Users\\valte\\8th semester\\Compiladores\\1499_sat.jpg")

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'STRING', 'label': 'str_C:\\\\Users\\\\valte\\\\8th semester\\\\Compiladores\\\\1499_sat.jpg', 'value': 'C:\\\\Users\\\\valte\\\\8th semester\\\\Compiladores\\\\1499_sat.jpg', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_load_image', 'value': 'load_image', 'counter': 2}
3: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 3}
4: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_image', 'value': 'image', 'counter': 4}

Expresión en la línea 3: image_segmented = watershed_segmentation(image)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image', 'value': 'image', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_watershed_segmentation', 'value': 'watershed_segmentation', 'counter': 2}
3: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 3}
4: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_image_segmented', 'value': 'image_segmented', 'counter': 4}

Expresión en la línea 4: show_image(image_segmented)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image_segmented', 'value': 'image_segmented', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_show_image', 'value': 'show_image', 'counter': 2}

Expresión en la línea 6: image_segmented = grabcut_segmentation(image)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image', 'value': 'image', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_grabcut_segmentation', 'value': 'grabcut_segmentation', 'counter': 2}
3: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 3}
4: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_image_segmented', 'value': 'image_segmented', 'counter': 4}

Expresión en la línea 7: show_image(image_segmented)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image_segmented', 'value': 'image_segmented', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_show_image', 'value': 'show_image', 'counter': 2}

Expresión en la línea 9: template = load_image("C:\\Users\\valte\\8th semester\\Compiladores\\template.jpg")

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'STRING', 'label': 'str_C:\\\\Users\\\\valte\\\\8th semester\\\\Compiladores\\\\template.jpg', 'value': 'C:\\\\Users\\\\valte\\\\8th semester\\\\Compiladores\\\\template.jpg', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_load_image', 'value': 'load_image', 'counter': 2}
3: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 3}
4: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_template', 'value': 'template', 'counter': 4}

Expresión en la línea 10: image_matched = template_matching(image, template)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image', 'value': 'image', 'counter': 1}
2: {'type': 'VARIABLE', 'label': 'VAR_template', 'value': 'template', 'counter': 2}
3: {'type': 'FUNCTION_CALL', 'label': 'FUN_template_matching', 'value': 'template_matching', 'counter': 3}
4: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 4}
5: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_image_matched', 'value': 'image_matched', 'counter': 5}

Expresión en la línea 11: show_image(image_matched)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image_matched', 'value': 'image_matched', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_show_image', 'value': 'show_image', 'counter': 2}

Expresión en la línea 13: edges = canny_edge_detection(image)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_image', 'value': 'image', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_canny_edge_detection', 'value': 'canny_edge_detection', 'counter': 2}
3: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 3}
4: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_edges', 'value': 'edges', 'counter': 4}

Expresión en la línea 14: show_image(edges)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_edges', 'value': 'edges', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_show_image', 'value': 'show_image', 'counter': 2}

### Para archivo instrucciones_lista.txt donde se probaron la creación de matrices y funciones de numpy

Expresión en la línea 1: matriz = gen_matrix(1,2,3,4)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'NUMBER', 'label': 'NUM_1', 'value': 1, 'counter': 1}
2: {'type': 'NUMBER', 'label': 'NUM_2', 'value': 2, 'counter': 2}
3: {'type': 'NUMBER', 'label': 'NUM_3', 'value': 3, 'counter': 3}
4: {'type': 'NUMBER', 'label': 'NUM_4', 'value': 4, 'counter': 4}
5: {'type': 'FUNCTION_CALL', 'label': 'FUN_gen_matrix', 'value': 'gen_matrix', 'counter': 5}
6: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 6}
7: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 7}

Expresión en la línea 3: matriz_t = np_transpose(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_transpose', 'value': 'np_transpose', 'counter': 2}
3: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 3}
4: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_matriz_t', 'value': 'matriz_t', 'counter': 4}

Expresión en la línea 4: matriz_d = np_dot(matriz, matriz_t)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'VARIABLE', 'label': 'VAR_matriz_t', 'value': 'matriz_t', 'counter': 2}
3: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_dot', 'value': 'np_dot', 'counter': 3}
4: {'type': 'ASSIGN', 'label': '=', 'value': '', 'counter': 4}
5: {'type': 'VARIABLE_ASSIGN', 'label': 'VAR_matriz_d', 'value': 'matriz_d', 'counter': 5}

Expresión en la línea 6: np_max(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_max', 'value': 'np_max', 'counter': 2}

Expresión en la línea 7: np_mean(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_mean', 'value': 'np_mean', 'counter': 2}

Expresión en la línea 8: np_std(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_std', 'value': 'np_std', 'counter': 2}

Expresión en la línea 9: np_sum(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_sum', 'value': 'np_sum', 'counter': 2}

Expresión en la línea 10: np_max(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_max', 'value': 'np_max', 'counter': 2}

Expresión en la línea 11: np_min(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_min', 'value': 'np_min', 'counter': 2}

Expresión en la línea 12: np_var(matriz)

Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_var', 'value': 'np_var', 'counter': 2}

Expresión en la línea 13: np_median(matriz)
Árbol de sintaxis abstracto:
0: {'type': 'INITIAL', 'label': 'INIT', 'counter': 0}
1: {'type': 'VARIABLE', 'label': 'VAR_matriz', 'value': 'matriz', 'counter': 1}
2: {'type': 'FUNCTION_CALL', 'label': 'FUN_np_median', 'value': 'np_median', 'counter': 2}

#### Nuevas características
![]() 

## Videos
[Emiliano Cabrera Ruiz]()
<br>[Do Hyun Nam]()
<br>[Valter Alejandro Kuhne Hernández]()

## Referencias
