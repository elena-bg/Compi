// Generated from /Users/elenaballinas/Desktop/Compi/gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramaticaParser}.
 */
public interface gramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#programRule}.
	 * @param ctx the parse tree
	 */
	void enterProgramRule(gramaticaParser.ProgramRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#programRule}.
	 * @param ctx the parse tree
	 */
	void exitProgramRule(gramaticaParser.ProgramRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(gramaticaParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(gramaticaParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#writeln}.
	 * @param ctx the parse tree
	 */
	void enterWriteln(gramaticaParser.WritelnContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#writeln}.
	 * @param ctx the parse tree
	 */
	void exitWriteln(gramaticaParser.WritelnContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(gramaticaParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(gramaticaParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#end}.
	 * @param ctx the parse tree
	 */
	void enterEnd(gramaticaParser.EndContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#end}.
	 * @param ctx the parse tree
	 */
	void exitEnd(gramaticaParser.EndContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(gramaticaParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(gramaticaParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#void}.
	 * @param ctx the parse tree
	 */
	void enterVoid(gramaticaParser.VoidContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#void}.
	 * @param ctx the parse tree
	 */
	void exitVoid(gramaticaParser.VoidContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#int}.
	 * @param ctx the parse tree
	 */
	void enterInt(gramaticaParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#int}.
	 * @param ctx the parse tree
	 */
	void exitInt(gramaticaParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#float}.
	 * @param ctx the parse tree
	 */
	void enterFloat(gramaticaParser.FloatContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#float}.
	 * @param ctx the parse tree
	 */
	void exitFloat(gramaticaParser.FloatContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#else}.
	 * @param ctx the parse tree
	 */
	void enterElse(gramaticaParser.ElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#else}.
	 * @param ctx the parse tree
	 */
	void exitElse(gramaticaParser.ElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#if}.
	 * @param ctx the parse tree
	 */
	void enterIf(gramaticaParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#if}.
	 * @param ctx the parse tree
	 */
	void exitIf(gramaticaParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#while}.
	 * @param ctx the parse tree
	 */
	void enterWhile(gramaticaParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#while}.
	 * @param ctx the parse tree
	 */
	void exitWhile(gramaticaParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#do}.
	 * @param ctx the parse tree
	 */
	void enterDo(gramaticaParser.DoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#do}.
	 * @param ctx the parse tree
	 */
	void exitDo(gramaticaParser.DoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#for}.
	 * @param ctx the parse tree
	 */
	void enterFor(gramaticaParser.ForContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#for}.
	 * @param ctx the parse tree
	 */
	void exitFor(gramaticaParser.ForContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#write}.
	 * @param ctx the parse tree
	 */
	void enterWrite(gramaticaParser.WriteContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#write}.
	 * @param ctx the parse tree
	 */
	void exitWrite(gramaticaParser.WriteContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(gramaticaParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(gramaticaParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(gramaticaParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(gramaticaParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(gramaticaParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(gramaticaParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(gramaticaParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(gramaticaParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(gramaticaParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(gramaticaParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(gramaticaParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(gramaticaParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#initialization}.
	 * @param ctx the parse tree
	 */
	void enterInitialization(gramaticaParser.InitializationContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#initialization}.
	 * @param ctx the parse tree
	 */
	void exitInitialization(gramaticaParser.InitializationContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(gramaticaParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(gramaticaParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#cycle}.
	 * @param ctx the parse tree
	 */
	void enterCycle(gramaticaParser.CycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#cycle}.
	 * @param ctx the parse tree
	 */
	void exitCycle(gramaticaParser.CycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#forSt}.
	 * @param ctx the parse tree
	 */
	void enterForSt(gramaticaParser.ForStContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#forSt}.
	 * @param ctx the parse tree
	 */
	void exitForSt(gramaticaParser.ForStContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(gramaticaParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(gramaticaParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(gramaticaParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(gramaticaParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(gramaticaParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(gramaticaParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(gramaticaParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(gramaticaParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(gramaticaParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(gramaticaParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#variables}.
	 * @param ctx the parse tree
	 */
	void enterVariables(gramaticaParser.VariablesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#variables}.
	 * @param ctx the parse tree
	 */
	void exitVariables(gramaticaParser.VariablesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listvars}.
	 * @param ctx the parse tree
	 */
	void enterListvars(gramaticaParser.ListvarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listvars}.
	 * @param ctx the parse tree
	 */
	void exitListvars(gramaticaParser.ListvarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#listaId}.
	 * @param ctx the parse tree
	 */
	void enterListaId(gramaticaParser.ListaIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#listaId}.
	 * @param ctx the parse tree
	 */
	void exitListaId(gramaticaParser.ListaIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#idExtra}.
	 * @param ctx the parse tree
	 */
	void enterIdExtra(gramaticaParser.IdExtraContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#idExtra}.
	 * @param ctx the parse tree
	 */
	void exitIdExtra(gramaticaParser.IdExtraContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(gramaticaParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(gramaticaParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(gramaticaParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(gramaticaParser.ParameterContext ctx);
}