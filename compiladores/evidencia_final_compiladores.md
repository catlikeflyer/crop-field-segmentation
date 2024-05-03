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
#### Nuevas características
##### Archivos
![Archivos1](./doc_images/archivos1.png) 
![Archivos2](./doc_images/archivos2.png)
##### Matrices y numpy
![numpy1](./doc_images/numpy1.png)
![numpy2](./doc_images/numpy2.png)
![numpy3](./doc_images/numpy3.png)
##### Histogramas
![Histograma1](./doc_images/histogram1.png)
![Histograma2](./doc_images/histogram2.png)
##### Pruebas automáticas
![Pruebas](./doc_images/pruebas%20de%20imagenes.png)
![Pruebas](./doc_images/pruebas_de_imagenes.png)
![Pruebas](./doc_images/pruebas_de_histograma.png)

## Videos
[Emiliano Cabrera Ruiz]()
<br>[Do Hyun Nam]()
<br>[Valter Alejandro Kuhne Hernández]()

## Referencias
