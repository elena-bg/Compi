from antlr4 import *
from cochinero import SymbolTable
from myListener import MyListener
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser

#Directorio de funciones de variables locales y globales
def main():
    symbol_table = SymbolTable()

    input_stream = FileStream("if.txt")
    lexer = gramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)

    tree = parser.programRule()
    listener = MyListener(symbol_table)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()