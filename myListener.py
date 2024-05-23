from gramaticaListener import gramaticaListener

class MyListener(gramaticaListener):
    def enterEveryRule(self, ctx):
        #print("Enter rule: ", type(ctx).__name__)
        pass
    
    def exitEveryRule(self, ctx):
        #print("Exit rule:", type(ctx).__name__)
        pass
        
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table