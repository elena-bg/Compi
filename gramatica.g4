grammar gramatica;

@parser::header {
from cochinero import SymbolTable
symbol_table = SymbolTable()
current_scope=0
vacia = []
}

// Regla principal que define el programa completo
programRule : program main '{' variables (function)* statement* '}' EOF {symbol_table.maquina()}; //{symbol_table.maquina()}

// Definición de las palabras clave y tokens básicos
program : 'program';
writeln : 'writeln';
Id : [a-zA-Z]+[0-9]*;
main : 'main';
end : 'end';
var : 'var';
void : 'void';
int : 'int';
float : 'float';
else: 'else';
if : 'if';
while : 'while';
do : 'do';
for: 'for';
write : 'write';
CTE_STRING : '"' .*? '"';
CTE_INT : [0-9]+;
CTE_FLOAT : [0-9]+ '.' [0-9]+ ('f'|'F')?;  // Permitimos 'f' o 'F' al final
WS: [ \t\r\n]+ -> skip;
OP_REL: '>=' | '<=' | '==' | '!=' | '>' | '<';

// Expresiones aritméticas y lógicas
expression: exp (OP_REL {symbol_table.push_operador($OP_REL.text)} exp {symbol_table.push_mayor_menor()})*;
exp: term {symbol_table.push_sumas()} 
    (('+' {symbol_table.push_operador('+')} | '-' {symbol_table.push_operador('-')}) term {symbol_table.push_sumas()})*;
term: factor {symbol_table.push_multi()} 
      (('*' {symbol_table.push_operador('*')} | '/' {symbol_table.push_operador('/')} | '%' {symbol_table.push_operador('%')}) factor {symbol_table.push_multi()})*;

factor: ('+'| '-')? (Id {symbol_table.push_factor($Id.text, None, False)} 
       | CTE_INT {symbol_table.push_factor($CTE_INT.text, 'int', True)} 
       | CTE_FLOAT {symbol_table.push_factor($CTE_FLOAT.text, 'float', True)} 
       | '(' expression ')');


// Definición de estructuras de control y asignación
body: '{' statement* '}';
assign: Id '='  expression {symbol_table.assign($Id.text, '=')} ';';
initialization: assign;
condition: if '('  expression ')' {symbol_table.ifSt()} body (else {symbol_table.elseSt()} body)? {symbol_table.endIf()};
cycle: while {symbol_table.whileSt()} '(' expression ')' {symbol_table.ifSt()} body {symbol_table.end_while()};
forSt: for '(' assign ';' expression {symbol_table.ifSt()}';' assign ')' body;
print : (write | writeln) '(' (expression {symbol_table.print_function()} | CTE_STRING {symbol_table.push_factor($CTE_STRING.text, "string", True); symbol_table.print_function()}) (',' (expression | CTE_STRING))* ')' ';';
functionCall: Id '(' (expression (',' expression)*)? ')' ';';
type: int | float;

// Definición de funciones y variables
function: void Id '(' parameters ')' '{' variables body '}' ';' {symbol_table.add_func($Id.text, $parameters.text, $variables.text, current_scope)} {symbol_table.pop_func($Id.text)};
statement: assign | forSt | condition | cycle | print | functionCall;
variables: listvars*;
listvars: type listaId ';' {symbol_table.add_symbol($listaId.text, $type.text, current_scope)};
listaId : Id idExtra;
idExtra : (',' listaId)*;
parameters: parameter (',' parameter)*;
parameter: Id ':' type {symbol_table.add_symbol($Id.text, $type.text, current_scope)};
