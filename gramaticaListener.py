# Generated from ./gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#programRule.
    def enterProgramRule(self, ctx:gramaticaParser.ProgramRuleContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programRule.
    def exitProgramRule(self, ctx:gramaticaParser.ProgramRuleContext):
        pass


    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#writeln.
    def enterWriteln(self, ctx:gramaticaParser.WritelnContext):
        pass

    # Exit a parse tree produced by gramaticaParser#writeln.
    def exitWriteln(self, ctx:gramaticaParser.WritelnContext):
        pass


    # Enter a parse tree produced by gramaticaParser#main.
    def enterMain(self, ctx:gramaticaParser.MainContext):
        pass

    # Exit a parse tree produced by gramaticaParser#main.
    def exitMain(self, ctx:gramaticaParser.MainContext):
        pass


    # Enter a parse tree produced by gramaticaParser#end.
    def enterEnd(self, ctx:gramaticaParser.EndContext):
        pass

    # Exit a parse tree produced by gramaticaParser#end.
    def exitEnd(self, ctx:gramaticaParser.EndContext):
        pass


    # Enter a parse tree produced by gramaticaParser#var.
    def enterVar(self, ctx:gramaticaParser.VarContext):
        pass

    # Exit a parse tree produced by gramaticaParser#var.
    def exitVar(self, ctx:gramaticaParser.VarContext):
        pass


    # Enter a parse tree produced by gramaticaParser#void.
    def enterVoid(self, ctx:gramaticaParser.VoidContext):
        pass

    # Exit a parse tree produced by gramaticaParser#void.
    def exitVoid(self, ctx:gramaticaParser.VoidContext):
        pass


    # Enter a parse tree produced by gramaticaParser#int.
    def enterInt(self, ctx:gramaticaParser.IntContext):
        pass

    # Exit a parse tree produced by gramaticaParser#int.
    def exitInt(self, ctx:gramaticaParser.IntContext):
        pass


    # Enter a parse tree produced by gramaticaParser#float.
    def enterFloat(self, ctx:gramaticaParser.FloatContext):
        pass

    # Exit a parse tree produced by gramaticaParser#float.
    def exitFloat(self, ctx:gramaticaParser.FloatContext):
        pass


    # Enter a parse tree produced by gramaticaParser#else.
    def enterElse(self, ctx:gramaticaParser.ElseContext):
        pass

    # Exit a parse tree produced by gramaticaParser#else.
    def exitElse(self, ctx:gramaticaParser.ElseContext):
        pass


    # Enter a parse tree produced by gramaticaParser#if.
    def enterIf(self, ctx:gramaticaParser.IfContext):
        pass

    # Exit a parse tree produced by gramaticaParser#if.
    def exitIf(self, ctx:gramaticaParser.IfContext):
        pass


    # Enter a parse tree produced by gramaticaParser#while.
    def enterWhile(self, ctx:gramaticaParser.WhileContext):
        pass

    # Exit a parse tree produced by gramaticaParser#while.
    def exitWhile(self, ctx:gramaticaParser.WhileContext):
        pass


    # Enter a parse tree produced by gramaticaParser#do.
    def enterDo(self, ctx:gramaticaParser.DoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#do.
    def exitDo(self, ctx:gramaticaParser.DoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#for.
    def enterFor(self, ctx:gramaticaParser.ForContext):
        pass

    # Exit a parse tree produced by gramaticaParser#for.
    def exitFor(self, ctx:gramaticaParser.ForContext):
        pass


    # Enter a parse tree produced by gramaticaParser#write.
    def enterWrite(self, ctx:gramaticaParser.WriteContext):
        pass

    # Exit a parse tree produced by gramaticaParser#write.
    def exitWrite(self, ctx:gramaticaParser.WriteContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expression.
    def enterExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expression.
    def exitExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#exp.
    def enterExp(self, ctx:gramaticaParser.ExpContext):
        pass

    # Exit a parse tree produced by gramaticaParser#exp.
    def exitExp(self, ctx:gramaticaParser.ExpContext):
        pass


    # Enter a parse tree produced by gramaticaParser#term.
    def enterTerm(self, ctx:gramaticaParser.TermContext):
        pass

    # Exit a parse tree produced by gramaticaParser#term.
    def exitTerm(self, ctx:gramaticaParser.TermContext):
        pass


    # Enter a parse tree produced by gramaticaParser#factor.
    def enterFactor(self, ctx:gramaticaParser.FactorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#factor.
    def exitFactor(self, ctx:gramaticaParser.FactorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#body.
    def enterBody(self, ctx:gramaticaParser.BodyContext):
        pass

    # Exit a parse tree produced by gramaticaParser#body.
    def exitBody(self, ctx:gramaticaParser.BodyContext):
        pass


    # Enter a parse tree produced by gramaticaParser#block.
    def enterBlock(self, ctx:gramaticaParser.BlockContext):
        pass

    # Exit a parse tree produced by gramaticaParser#block.
    def exitBlock(self, ctx:gramaticaParser.BlockContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assign.
    def enterAssign(self, ctx:gramaticaParser.AssignContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assign.
    def exitAssign(self, ctx:gramaticaParser.AssignContext):
        pass


    # Enter a parse tree produced by gramaticaParser#initialization.
    def enterInitialization(self, ctx:gramaticaParser.InitializationContext):
        pass

    # Exit a parse tree produced by gramaticaParser#initialization.
    def exitInitialization(self, ctx:gramaticaParser.InitializationContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condition.
    def enterCondition(self, ctx:gramaticaParser.ConditionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condition.
    def exitCondition(self, ctx:gramaticaParser.ConditionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cycle.
    def enterCycle(self, ctx:gramaticaParser.CycleContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cycle.
    def exitCycle(self, ctx:gramaticaParser.CycleContext):
        pass


    # Enter a parse tree produced by gramaticaParser#forSt.
    def enterForSt(self, ctx:gramaticaParser.ForStContext):
        pass

    # Exit a parse tree produced by gramaticaParser#forSt.
    def exitForSt(self, ctx:gramaticaParser.ForStContext):
        pass


    # Enter a parse tree produced by gramaticaParser#print.
    def enterPrint(self, ctx:gramaticaParser.PrintContext):
        pass

    # Exit a parse tree produced by gramaticaParser#print.
    def exitPrint(self, ctx:gramaticaParser.PrintContext):
        pass


    # Enter a parse tree produced by gramaticaParser#functionCall.
    def enterFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by gramaticaParser#functionCall.
    def exitFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by gramaticaParser#type.
    def enterType(self, ctx:gramaticaParser.TypeContext):
        pass

    # Exit a parse tree produced by gramaticaParser#type.
    def exitType(self, ctx:gramaticaParser.TypeContext):
        pass


    # Enter a parse tree produced by gramaticaParser#function.
    def enterFunction(self, ctx:gramaticaParser.FunctionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#function.
    def exitFunction(self, ctx:gramaticaParser.FunctionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#variables.
    def enterVariables(self, ctx:gramaticaParser.VariablesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#variables.
    def exitVariables(self, ctx:gramaticaParser.VariablesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#listvars.
    def enterListvars(self, ctx:gramaticaParser.ListvarsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#listvars.
    def exitListvars(self, ctx:gramaticaParser.ListvarsContext):
        pass


    # Enter a parse tree produced by gramaticaParser#listaId.
    def enterListaId(self, ctx:gramaticaParser.ListaIdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#listaId.
    def exitListaId(self, ctx:gramaticaParser.ListaIdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#idExtra.
    def enterIdExtra(self, ctx:gramaticaParser.IdExtraContext):
        pass

    # Exit a parse tree produced by gramaticaParser#idExtra.
    def exitIdExtra(self, ctx:gramaticaParser.IdExtraContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parameters.
    def enterParameters(self, ctx:gramaticaParser.ParametersContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parameters.
    def exitParameters(self, ctx:gramaticaParser.ParametersContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parameter.
    def enterParameter(self, ctx:gramaticaParser.ParameterContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parameter.
    def exitParameter(self, ctx:gramaticaParser.ParameterContext):
        pass



del gramaticaParser