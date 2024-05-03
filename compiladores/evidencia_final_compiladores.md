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

## Funciones Implementadas
- Aceptar archivos y ejecutar el contenido
- Implementación de visualización de histogramas
- Implementación de un algoritmo complejo
- Implementación de pruebas automatizadas
- Implementación de un algoritmo complejo como herramienta en el lenguaje: WaterShed, Grabcut, TemplateMatching, CannyEdgeDetection
- 

## Expresiones

## Videos
[Emiliano Cabrera Ruiz]()
<br>[Do Hyun Nam]()
<br>[Valter Alejandro Kuhne Hernández]()

## Referencias