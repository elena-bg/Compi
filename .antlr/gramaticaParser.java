// Generated from /Users/elenaballinas/Desktop/Compi/gramatica.g4 by ANTLR 4.13.1

from cochinero import SymbolTable
symbol_table = SymbolTable()
current_scope=0
vacia = []

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gramaticaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, Id=27, CTE_STRING=28, CTE_INT=29, CTE_FLOAT=30, WS=31, 
		OP_REL=32;
	public static final int
		RULE_programRule = 0, RULE_program = 1, RULE_writeln = 2, RULE_main = 3, 
		RULE_end = 4, RULE_var = 5, RULE_void = 6, RULE_int = 7, RULE_float = 8, 
		RULE_else = 9, RULE_if = 10, RULE_while = 11, RULE_do = 12, RULE_for = 13, 
		RULE_write = 14, RULE_expression = 15, RULE_exp = 16, RULE_term = 17, 
		RULE_factor = 18, RULE_body = 19, RULE_block = 20, RULE_assign = 21, RULE_initialization = 22, 
		RULE_condition = 23, RULE_cycle = 24, RULE_forSt = 25, RULE_print = 26, 
		RULE_functionCall = 27, RULE_type = 28, RULE_function = 29, RULE_statement = 30, 
		RULE_variables = 31, RULE_listvars = 32, RULE_listaId = 33, RULE_idExtra = 34, 
		RULE_parameters = 35, RULE_parameter = 36;
	private static String[] makeRuleNames() {
		return new String[] {
			"programRule", "program", "writeln", "main", "end", "var", "void", "int", 
			"float", "else", "if", "while", "do", "for", "write", "expression", "exp", 
			"term", "factor", "body", "block", "assign", "initialization", "condition", 
			"cycle", "forSt", "print", "functionCall", "type", "function", "statement", 
			"variables", "listvars", "listaId", "idExtra", "parameters", "parameter"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "'program'", "'writeln'", "'main'", "'end'", "'var'", 
			"'void'", "'int'", "'float'", "'else'", "'if'", "'while'", "'do'", "'for'", 
			"'write'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'='", "';'", 
			"','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "Id", "CTE_STRING", "CTE_INT", "CTE_FLOAT", "WS", "OP_REL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramRuleContext extends ParserRuleContext {
		public ProgramContext program() {
			return getRuleContext(ProgramContext.class,0);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public VariablesContext variables() {
			return getRuleContext(VariablesContext.class,0);
		}
		public TerminalNode EOF() { return getToken(gramaticaParser.EOF, 0); }
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programRule; }
	}

	public final ProgramRuleContext programRule() throws RecognitionException {
		ProgramRuleContext _localctx = new ProgramRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			program();
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__7) {
				{
				{
				setState(75);
				function();
				}
				}
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(81);
			main();
			setState(82);
			match(T__0);
			setState(83);
			variables();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134328336L) != 0)) {
				{
				{
				setState(84);
				statement();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
			match(T__1);
			setState(91);
			match(EOF);
			symbol_table.maquina()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WritelnContext extends ParserRuleContext {
		public WritelnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_writeln; }
	}

	public final WritelnContext writeln() throws RecognitionException {
		WritelnContext _localctx = new WritelnContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_writeln);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MainContext extends ParserRuleContext {
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EndContext extends ParserRuleContext {
		public EndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end; }
	}

	public final EndContext end() throws RecognitionException {
		EndContext _localctx = new EndContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_end);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ParserRuleContext {
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VoidContext extends ParserRuleContext {
		public VoidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_void; }
	}

	public final VoidContext void_() throws RecognitionException {
		VoidContext _localctx = new VoidContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_void);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends ParserRuleContext {
		public IntContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int; }
	}

	public final IntContext int_() throws RecognitionException {
		IntContext _localctx = new IntContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_int);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FloatContext extends ParserRuleContext {
		public FloatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float; }
	}

	public final FloatContext float_() throws RecognitionException {
		FloatContext _localctx = new FloatContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_float);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseContext extends ParserRuleContext {
		public ElseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else; }
	}

	public final ElseContext else_() throws RecognitionException {
		ElseContext _localctx = new ElseContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_else);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(T__10);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ParserRuleContext {
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends ParserRuleContext {
		public WhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while; }
	}

	public final WhileContext while_() throws RecognitionException {
		WhileContext _localctx = new WhileContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(T__12);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoContext extends ParserRuleContext {
		public DoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do; }
	}

	public final DoContext do_() throws RecognitionException {
		DoContext _localctx = new DoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_do);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForContext extends ParserRuleContext {
		public ForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for; }
	}

	public final ForContext for_() throws RecognitionException {
		ForContext _localctx = new ForContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_for);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(T__14);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteContext extends ParserRuleContext {
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_write);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public Token OP_REL;
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> OP_REL() { return getTokens(gramaticaParser.OP_REL); }
		public TerminalNode OP_REL(int i) {
			return getToken(gramaticaParser.OP_REL, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			exp();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_REL) {
				{
				{
				setState(123);
				((ExpressionContext)_localctx).OP_REL = match(OP_REL);
				symbol_table.push_operador((((ExpressionContext)_localctx).OP_REL!=null?((ExpressionContext)_localctx).OP_REL.getText():null))
				setState(125);
				exp();
				symbol_table.push_mayor_menor()
				}
				}
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			term();
			symbol_table.push_sumas()
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__16 || _la==T__17) {
				{
				{
				setState(139);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__16:
					{
					setState(135);
					match(T__16);
					symbol_table.push_operador('+')
					}
					break;
				case T__17:
					{
					setState(137);
					match(T__17);
					symbol_table.push_operador('-')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(141);
				term();
				symbol_table.push_sumas()
				}
				}
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			factor();
			symbol_table.push_multi()
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) {
				{
				{
				setState(157);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__18:
					{
					setState(151);
					match(T__18);
					symbol_table.push_operador('*')
					}
					break;
				case T__19:
					{
					setState(153);
					match(T__19);
					symbol_table.push_operador('/')
					}
					break;
				case T__20:
					{
					setState(155);
					match(T__20);
					symbol_table.push_operador('%')
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(159);
				factor();
				symbol_table.push_multi()
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public Token Id;
		public Token CTE_INT;
		public Token CTE_FLOAT;
		public TerminalNode Id() { return getToken(gramaticaParser.Id, 0); }
		public TerminalNode CTE_INT() { return getToken(gramaticaParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(gramaticaParser.CTE_FLOAT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16 || _la==T__17) {
				{
				setState(167);
				_la = _input.LA(1);
				if ( !(_la==T__16 || _la==T__17) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(182);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Id:
				{
				setState(170);
				((FactorContext)_localctx).Id = match(Id);
				symbol_table.push_factor((((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), None, False)
				}
				break;
			case CTE_INT:
				{
				setState(172);
				((FactorContext)_localctx).CTE_INT = match(CTE_INT);
				symbol_table.push_factor((((FactorContext)_localctx).CTE_INT!=null?((FactorContext)_localctx).CTE_INT.getText():null), 'int', True)
				}
				break;
			case CTE_FLOAT:
				{
				setState(174);
				((FactorContext)_localctx).CTE_FLOAT = match(CTE_FLOAT);
				symbol_table.push_factor((((FactorContext)_localctx).CTE_FLOAT!=null?((FactorContext)_localctx).CTE_FLOAT.getText():null), 'float', True)
				}
				break;
			case T__21:
				{
				setState(176);
				match(T__21);
				symbol_table.push_parentesis('(')
				setState(178);
				expression();
				setState(179);
				match(T__22);
				symbol_table.pop_parentesis()
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			match(T__0);
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134328336L) != 0)) {
				{
				{
				setState(185);
				statement();
				}
				}
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(191);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134328336L) != 0)) {
				{
				{
				setState(193);
				statement();
				}
				}
				setState(198);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public Token Id;
		public TerminalNode Id() { return getToken(gramaticaParser.Id, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			((AssignContext)_localctx).Id = match(Id);
			setState(200);
			match(T__23);
			setState(201);
			expression();
			symbol_table.assign((((AssignContext)_localctx).Id!=null?((AssignContext)_localctx).Id.getText():null), '=')
			setState(203);
			match(T__24);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitializationContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public InitializationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initialization; }
	}

	public final InitializationContext initialization() throws RecognitionException {
		InitializationContext _localctx = new InitializationContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_initialization);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			assign();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public ElseContext else_() {
			return getRuleContext(ElseContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			if_();
			setState(208);
			match(T__21);
			setState(209);
			expression();
			setState(210);
			match(T__22);
			symbol_table.ifSt()
			setState(212);
			body();
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(213);
				else_();
				symbol_table.elseSt()
				setState(215);
				body();
				}
			}

			symbol_table.endIf()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public WhileContext while_() {
			return getRuleContext(WhileContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			while_();
			symbol_table.whileSt()
			setState(223);
			match(T__21);
			setState(224);
			expression();
			setState(225);
			match(T__22);
			symbol_table.ifSt()
			setState(227);
			body();
			symbol_table.end_while()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStContext extends ParserRuleContext {
		public AssignContext assign;
		public ForContext for_() {
			return getRuleContext(ForContext.class,0);
		}
		public List<AssignContext> assign() {
			return getRuleContexts(AssignContext.class);
		}
		public AssignContext assign(int i) {
			return getRuleContext(AssignContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ForStContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forSt; }
	}

	public final ForStContext forSt() throws RecognitionException {
		ForStContext _localctx = new ForStContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_forSt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			for_();
			setState(231);
			match(T__21);
			setState(232);
			((ForStContext)_localctx).assign = assign();
			symbol_table.forSt((((ForStContext)_localctx).assign!=null?_input.getText(((ForStContext)_localctx).assign.start,((ForStContext)_localctx).assign.stop):null))
			setState(234);
			expression();
			symbol_table.for_condition()
			setState(236);
			match(T__24);
			setState(237);
			((ForStContext)_localctx).assign = assign();
			setState(238);
			match(T__22);
			setState(239);
			body();
			symbol_table.end_for()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public Token CTE_STRING;
		public WriteContext write() {
			return getRuleContext(WriteContext.class,0);
		}
		public WritelnContext writeln() {
			return getRuleContext(WritelnContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> CTE_STRING() { return getTokens(gramaticaParser.CTE_STRING); }
		public TerminalNode CTE_STRING(int i) {
			return getToken(gramaticaParser.CTE_STRING, i);
		}
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				{
				setState(242);
				write();
				}
				break;
			case T__3:
				{
				setState(243);
				writeln();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(246);
			match(T__21);
			setState(252);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__16:
			case T__17:
			case T__21:
			case Id:
			case CTE_INT:
			case CTE_FLOAT:
				{
				setState(247);
				expression();
				symbol_table.print_function()
				}
				break;
			case CTE_STRING:
				{
				setState(250);
				((PrintContext)_localctx).CTE_STRING = match(CTE_STRING);
				symbol_table.push_factor((((PrintContext)_localctx).CTE_STRING!=null?((PrintContext)_localctx).CTE_STRING.getText():null), "string", True); symbol_table.print_function()
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(261);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(254);
				match(T__25);
				setState(257);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__16:
				case T__17:
				case T__21:
				case Id:
				case CTE_INT:
				case CTE_FLOAT:
					{
					setState(255);
					expression();
					}
					break;
				case CTE_STRING:
					{
					setState(256);
					((PrintContext)_localctx).CTE_STRING = match(CTE_STRING);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(263);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(264);
			match(T__22);
			setState(265);
			match(T__24);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public Token Id;
		public TerminalNode Id() { return getToken(gramaticaParser.Id, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			((FunctionCallContext)_localctx).Id = match(Id);
			setState(268);
			match(T__21);
			symbol_table.function_call((((FunctionCallContext)_localctx).Id!=null?((FunctionCallContext)_localctx).Id.getText():null))
			setState(278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1749417984L) != 0)) {
				{
				setState(270);
				expression();
				setState(275);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__25) {
					{
					{
					setState(271);
					match(T__25);
					setState(272);
					expression();
					}
					}
					setState(277);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(280);
			match(T__22);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public IntContext int_() {
			return getRuleContext(IntContext.class,0);
		}
		public FloatContext float_() {
			return getRuleContext(FloatContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_type);
		try {
			setState(284);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(282);
				int_();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				float_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public Token Id;
		public ParametersContext parameters;
		public VariablesContext variables;
		public VoidContext void_() {
			return getRuleContext(VoidContext.class,0);
		}
		public TerminalNode Id() { return getToken(gramaticaParser.Id, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public VariablesContext variables() {
			return getRuleContext(VariablesContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			void_();
			setState(287);
			((FunctionContext)_localctx).Id = match(Id);
			setState(288);
			match(T__21);
			setState(289);
			((FunctionContext)_localctx).parameters = parameters();
			setState(290);
			match(T__22);
			setState(291);
			match(T__0);
			setState(292);
			((FunctionContext)_localctx).variables = variables();
			symbol_table.add_func((((FunctionContext)_localctx).Id!=null?((FunctionContext)_localctx).Id.getText():null), (((FunctionContext)_localctx).parameters!=null?_input.getText(((FunctionContext)_localctx).parameters.start,((FunctionContext)_localctx).parameters.stop):null), (((FunctionContext)_localctx).variables!=null?_input.getText(((FunctionContext)_localctx).variables.start,((FunctionContext)_localctx).variables.stop):null), current_scope)
			setState(294);
			block();
			setState(295);
			match(T__1);
			symbol_table.end_function()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ForStContext forSt() {
			return getRuleContext(ForStContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_statement);
		try {
			setState(304);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(298);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(299);
				forSt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(300);
				condition();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(301);
				cycle();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(302);
				print();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(303);
				functionCall();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariablesContext extends ParserRuleContext {
		public List<ListvarsContext> listvars() {
			return getRuleContexts(ListvarsContext.class);
		}
		public ListvarsContext listvars(int i) {
			return getRuleContext(ListvarsContext.class,i);
		}
		public VariablesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variables; }
	}

	public final VariablesContext variables() throws RecognitionException {
		VariablesContext _localctx = new VariablesContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_variables);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__8 || _la==T__9) {
				{
				{
				setState(306);
				listvars();
				}
				}
				setState(311);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListvarsContext extends ParserRuleContext {
		public TypeContext type;
		public ListaIdContext listaId;
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ListaIdContext listaId() {
			return getRuleContext(ListaIdContext.class,0);
		}
		public ListvarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listvars; }
	}

	public final ListvarsContext listvars() throws RecognitionException {
		ListvarsContext _localctx = new ListvarsContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_listvars);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			((ListvarsContext)_localctx).type = type();
			setState(313);
			((ListvarsContext)_localctx).listaId = listaId();
			setState(314);
			match(T__24);
			symbol_table.add_symbol((((ListvarsContext)_localctx).listaId!=null?_input.getText(((ListvarsContext)_localctx).listaId.start,((ListvarsContext)_localctx).listaId.stop):null), (((ListvarsContext)_localctx).type!=null?_input.getText(((ListvarsContext)_localctx).type.start,((ListvarsContext)_localctx).type.stop):null), current_scope)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaIdContext extends ParserRuleContext {
		public TerminalNode Id() { return getToken(gramaticaParser.Id, 0); }
		public IdExtraContext idExtra() {
			return getRuleContext(IdExtraContext.class,0);
		}
		public ListaIdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaId; }
	}

	public final ListaIdContext listaId() throws RecognitionException {
		ListaIdContext _localctx = new ListaIdContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_listaId);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			match(Id);
			setState(318);
			idExtra();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdExtraContext extends ParserRuleContext {
		public List<ListaIdContext> listaId() {
			return getRuleContexts(ListaIdContext.class);
		}
		public ListaIdContext listaId(int i) {
			return getRuleContext(ListaIdContext.class,i);
		}
		public IdExtraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idExtra; }
	}

	public final IdExtraContext idExtra() throws RecognitionException {
		IdExtraContext _localctx = new IdExtraContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_idExtra);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(320);
					match(T__25);
					setState(321);
					listaId();
					}
					} 
				}
				setState(326);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			parameter();
			setState(332);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(328);
				match(T__25);
				setState(329);
				parameter();
				}
				}
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public TypeContext type;
		public Token Id;
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode Id() { return getToken(gramaticaParser.Id, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			((ParameterContext)_localctx).type = type();
			setState(336);
			((ParameterContext)_localctx).Id = match(Id);
			symbol_table.add_symbol((((ParameterContext)_localctx).Id!=null?((ParameterContext)_localctx).Id.getText():null), (((ParameterContext)_localctx).type!=null?_input.getText(((ParameterContext)_localctx).type.start,((ParameterContext)_localctx).type.stop):null), current_scope)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001 \u0154\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0001\u0000\u0001\u0000\u0005\u0000M\b\u0000\n"+
		"\u0000\f\u0000P\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000V\b\u0000\n\u0000\f\u0000Y\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u0081\b\u000f\n\u000f"+
		"\f\u000f\u0084\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0003\u0010\u008c\b\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0005\u0010\u0091\b\u0010\n\u0010\f\u0010\u0094\t\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0003\u0011\u009e\b\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0005\u0011\u00a3\b\u0011\n\u0011\f\u0011\u00a6\t\u0011\u0001\u0012"+
		"\u0003\u0012\u00a9\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0003\u0012\u00b7\b\u0012\u0001\u0013\u0001\u0013"+
		"\u0005\u0013\u00bb\b\u0013\n\u0013\f\u0013\u00be\t\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0005\u0014\u00c3\b\u0014\n\u0014\f\u0014\u00c6\t\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0003\u0017\u00da\b\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0003\u001a\u00f5\b\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a"+
		"\u00fd\b\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u0102\b"+
		"\u001a\u0005\u001a\u0104\b\u001a\n\u001a\f\u001a\u0107\t\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0005\u001b\u0112\b\u001b\n\u001b\f\u001b\u0115"+
		"\t\u001b\u0003\u001b\u0117\b\u001b\u0001\u001b\u0001\u001b\u0001\u001c"+
		"\u0001\u001c\u0003\u001c\u011d\b\u001c\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u0131\b\u001e\u0001\u001f"+
		"\u0005\u001f\u0134\b\u001f\n\u001f\f\u001f\u0137\t\u001f\u0001 \u0001"+
		" \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001\"\u0001\"\u0005\"\u0143"+
		"\b\"\n\"\f\"\u0146\t\"\u0001#\u0001#\u0001#\u0005#\u014b\b#\n#\f#\u014e"+
		"\t#\u0001$\u0001$\u0001$\u0001$\u0001$\u0000\u0000%\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.02468:<>@BDFH\u0000\u0001\u0001\u0000\u0011\u0012\u014c\u0000J\u0001"+
		"\u0000\u0000\u0000\u0002^\u0001\u0000\u0000\u0000\u0004`\u0001\u0000\u0000"+
		"\u0000\u0006b\u0001\u0000\u0000\u0000\bd\u0001\u0000\u0000\u0000\nf\u0001"+
		"\u0000\u0000\u0000\fh\u0001\u0000\u0000\u0000\u000ej\u0001\u0000\u0000"+
		"\u0000\u0010l\u0001\u0000\u0000\u0000\u0012n\u0001\u0000\u0000\u0000\u0014"+
		"p\u0001\u0000\u0000\u0000\u0016r\u0001\u0000\u0000\u0000\u0018t\u0001"+
		"\u0000\u0000\u0000\u001av\u0001\u0000\u0000\u0000\u001cx\u0001\u0000\u0000"+
		"\u0000\u001ez\u0001\u0000\u0000\u0000 \u0085\u0001\u0000\u0000\u0000\""+
		"\u0095\u0001\u0000\u0000\u0000$\u00a8\u0001\u0000\u0000\u0000&\u00b8\u0001"+
		"\u0000\u0000\u0000(\u00c4\u0001\u0000\u0000\u0000*\u00c7\u0001\u0000\u0000"+
		"\u0000,\u00cd\u0001\u0000\u0000\u0000.\u00cf\u0001\u0000\u0000\u00000"+
		"\u00dd\u0001\u0000\u0000\u00002\u00e6\u0001\u0000\u0000\u00004\u00f4\u0001"+
		"\u0000\u0000\u00006\u010b\u0001\u0000\u0000\u00008\u011c\u0001\u0000\u0000"+
		"\u0000:\u011e\u0001\u0000\u0000\u0000<\u0130\u0001\u0000\u0000\u0000>"+
		"\u0135\u0001\u0000\u0000\u0000@\u0138\u0001\u0000\u0000\u0000B\u013d\u0001"+
		"\u0000\u0000\u0000D\u0144\u0001\u0000\u0000\u0000F\u0147\u0001\u0000\u0000"+
		"\u0000H\u014f\u0001\u0000\u0000\u0000JN\u0003\u0002\u0001\u0000KM\u0003"+
		":\u001d\u0000LK\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001"+
		"\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OQ\u0001\u0000\u0000\u0000"+
		"PN\u0001\u0000\u0000\u0000QR\u0003\u0006\u0003\u0000RS\u0005\u0001\u0000"+
		"\u0000SW\u0003>\u001f\u0000TV\u0003<\u001e\u0000UT\u0001\u0000\u0000\u0000"+
		"VY\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000"+
		"\u0000XZ\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000Z[\u0005\u0002"+
		"\u0000\u0000[\\\u0005\u0000\u0000\u0001\\]\u0006\u0000\uffff\uffff\u0000"+
		"]\u0001\u0001\u0000\u0000\u0000^_\u0005\u0003\u0000\u0000_\u0003\u0001"+
		"\u0000\u0000\u0000`a\u0005\u0004\u0000\u0000a\u0005\u0001\u0000\u0000"+
		"\u0000bc\u0005\u0005\u0000\u0000c\u0007\u0001\u0000\u0000\u0000de\u0005"+
		"\u0006\u0000\u0000e\t\u0001\u0000\u0000\u0000fg\u0005\u0007\u0000\u0000"+
		"g\u000b\u0001\u0000\u0000\u0000hi\u0005\b\u0000\u0000i\r\u0001\u0000\u0000"+
		"\u0000jk\u0005\t\u0000\u0000k\u000f\u0001\u0000\u0000\u0000lm\u0005\n"+
		"\u0000\u0000m\u0011\u0001\u0000\u0000\u0000no\u0005\u000b\u0000\u0000"+
		"o\u0013\u0001\u0000\u0000\u0000pq\u0005\f\u0000\u0000q\u0015\u0001\u0000"+
		"\u0000\u0000rs\u0005\r\u0000\u0000s\u0017\u0001\u0000\u0000\u0000tu\u0005"+
		"\u000e\u0000\u0000u\u0019\u0001\u0000\u0000\u0000vw\u0005\u000f\u0000"+
		"\u0000w\u001b\u0001\u0000\u0000\u0000xy\u0005\u0010\u0000\u0000y\u001d"+
		"\u0001\u0000\u0000\u0000z\u0082\u0003 \u0010\u0000{|\u0005 \u0000\u0000"+
		"|}\u0006\u000f\uffff\uffff\u0000}~\u0003 \u0010\u0000~\u007f\u0006\u000f"+
		"\uffff\uffff\u0000\u007f\u0081\u0001\u0000\u0000\u0000\u0080{\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u001f\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0086\u0003\"\u0011"+
		"\u0000\u0086\u0092\u0006\u0010\uffff\uffff\u0000\u0087\u0088\u0005\u0011"+
		"\u0000\u0000\u0088\u008c\u0006\u0010\uffff\uffff\u0000\u0089\u008a\u0005"+
		"\u0012\u0000\u0000\u008a\u008c\u0006\u0010\uffff\uffff\u0000\u008b\u0087"+
		"\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008c\u008d"+
		"\u0001\u0000\u0000\u0000\u008d\u008e\u0003\"\u0011\u0000\u008e\u008f\u0006"+
		"\u0010\uffff\uffff\u0000\u008f\u0091\u0001\u0000\u0000\u0000\u0090\u008b"+
		"\u0001\u0000\u0000\u0000\u0091\u0094\u0001\u0000\u0000\u0000\u0092\u0090"+
		"\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093!\u0001"+
		"\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0095\u0096\u0003"+
		"$\u0012\u0000\u0096\u00a4\u0006\u0011\uffff\uffff\u0000\u0097\u0098\u0005"+
		"\u0013\u0000\u0000\u0098\u009e\u0006\u0011\uffff\uffff\u0000\u0099\u009a"+
		"\u0005\u0014\u0000\u0000\u009a\u009e\u0006\u0011\uffff\uffff\u0000\u009b"+
		"\u009c\u0005\u0015\u0000\u0000\u009c\u009e\u0006\u0011\uffff\uffff\u0000"+
		"\u009d\u0097\u0001\u0000\u0000\u0000\u009d\u0099\u0001\u0000\u0000\u0000"+
		"\u009d\u009b\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000"+
		"\u009f\u00a0\u0003$\u0012\u0000\u00a0\u00a1\u0006\u0011\uffff\uffff\u0000"+
		"\u00a1\u00a3\u0001\u0000\u0000\u0000\u00a2\u009d\u0001\u0000\u0000\u0000"+
		"\u00a3\u00a6\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5#\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a7\u00a9\u0007\u0000\u0000\u0000\u00a8"+
		"\u00a7\u0001\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9"+
		"\u00b6\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005\u001b\u0000\u0000\u00ab"+
		"\u00b7\u0006\u0012\uffff\uffff\u0000\u00ac\u00ad\u0005\u001d\u0000\u0000"+
		"\u00ad\u00b7\u0006\u0012\uffff\uffff\u0000\u00ae\u00af\u0005\u001e\u0000"+
		"\u0000\u00af\u00b7\u0006\u0012\uffff\uffff\u0000\u00b0\u00b1\u0005\u0016"+
		"\u0000\u0000\u00b1\u00b2\u0006\u0012\uffff\uffff\u0000\u00b2\u00b3\u0003"+
		"\u001e\u000f\u0000\u00b3\u00b4\u0005\u0017\u0000\u0000\u00b4\u00b5\u0006"+
		"\u0012\uffff\uffff\u0000\u00b5\u00b7\u0001\u0000\u0000\u0000\u00b6\u00aa"+
		"\u0001\u0000\u0000\u0000\u00b6\u00ac\u0001\u0000\u0000\u0000\u00b6\u00ae"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b0\u0001\u0000\u0000\u0000\u00b7%\u0001"+
		"\u0000\u0000\u0000\u00b8\u00bc\u0005\u0001\u0000\u0000\u00b9\u00bb\u0003"+
		"<\u001e\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb\u00be\u0001\u0000"+
		"\u0000\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000"+
		"\u0000\u0000\u00bd\u00bf\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000"+
		"\u0000\u0000\u00bf\u00c0\u0005\u0002\u0000\u0000\u00c0\'\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c3\u0003<\u001e\u0000\u00c2\u00c1\u0001\u0000\u0000\u0000"+
		"\u00c3\u00c6\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000"+
		"\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5)\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005\u001b\u0000\u0000\u00c8"+
		"\u00c9\u0005\u0018\u0000\u0000\u00c9\u00ca\u0003\u001e\u000f\u0000\u00ca"+
		"\u00cb\u0006\u0015\uffff\uffff\u0000\u00cb\u00cc\u0005\u0019\u0000\u0000"+
		"\u00cc+\u0001\u0000\u0000\u0000\u00cd\u00ce\u0003*\u0015\u0000\u00ce-"+
		"\u0001\u0000\u0000\u0000\u00cf\u00d0\u0003\u0014\n\u0000\u00d0\u00d1\u0005"+
		"\u0016\u0000\u0000\u00d1\u00d2\u0003\u001e\u000f\u0000\u00d2\u00d3\u0005"+
		"\u0017\u0000\u0000\u00d3\u00d4\u0006\u0017\uffff\uffff\u0000\u00d4\u00d9"+
		"\u0003&\u0013\u0000\u00d5\u00d6\u0003\u0012\t\u0000\u00d6\u00d7\u0006"+
		"\u0017\uffff\uffff\u0000\u00d7\u00d8\u0003&\u0013\u0000\u00d8\u00da\u0001"+
		"\u0000\u0000\u0000\u00d9\u00d5\u0001\u0000\u0000\u0000\u00d9\u00da\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0001\u0000\u0000\u0000\u00db\u00dc\u0006"+
		"\u0017\uffff\uffff\u0000\u00dc/\u0001\u0000\u0000\u0000\u00dd\u00de\u0003"+
		"\u0016\u000b\u0000\u00de\u00df\u0006\u0018\uffff\uffff\u0000\u00df\u00e0"+
		"\u0005\u0016\u0000\u0000\u00e0\u00e1\u0003\u001e\u000f\u0000\u00e1\u00e2"+
		"\u0005\u0017\u0000\u0000\u00e2\u00e3\u0006\u0018\uffff\uffff\u0000\u00e3"+
		"\u00e4\u0003&\u0013\u0000\u00e4\u00e5\u0006\u0018\uffff\uffff\u0000\u00e5"+
		"1\u0001\u0000\u0000\u0000\u00e6\u00e7\u0003\u001a\r\u0000\u00e7\u00e8"+
		"\u0005\u0016\u0000\u0000\u00e8\u00e9\u0003*\u0015\u0000\u00e9\u00ea\u0006"+
		"\u0019\uffff\uffff\u0000\u00ea\u00eb\u0003\u001e\u000f\u0000\u00eb\u00ec"+
		"\u0006\u0019\uffff\uffff\u0000\u00ec\u00ed\u0005\u0019\u0000\u0000\u00ed"+
		"\u00ee\u0003*\u0015\u0000\u00ee\u00ef\u0005\u0017\u0000\u0000\u00ef\u00f0"+
		"\u0003&\u0013\u0000\u00f0\u00f1\u0006\u0019\uffff\uffff\u0000\u00f13\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f5\u0003\u001c\u000e\u0000\u00f3\u00f5\u0003"+
		"\u0004\u0002\u0000\u00f4\u00f2\u0001\u0000\u0000\u0000\u00f4\u00f3\u0001"+
		"\u0000\u0000\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000\u00f6\u00fc\u0005"+
		"\u0016\u0000\u0000\u00f7\u00f8\u0003\u001e\u000f\u0000\u00f8\u00f9\u0006"+
		"\u001a\uffff\uffff\u0000\u00f9\u00fd\u0001\u0000\u0000\u0000\u00fa\u00fb"+
		"\u0005\u001c\u0000\u0000\u00fb\u00fd\u0006\u001a\uffff\uffff\u0000\u00fc"+
		"\u00f7\u0001\u0000\u0000\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000\u00fd"+
		"\u0105\u0001\u0000\u0000\u0000\u00fe\u0101\u0005\u001a\u0000\u0000\u00ff"+
		"\u0102\u0003\u001e\u000f\u0000\u0100\u0102\u0005\u001c\u0000\u0000\u0101"+
		"\u00ff\u0001\u0000\u0000\u0000\u0101\u0100\u0001\u0000\u0000\u0000\u0102"+
		"\u0104\u0001\u0000\u0000\u0000\u0103\u00fe\u0001\u0000\u0000\u0000\u0104"+
		"\u0107\u0001\u0000\u0000\u0000\u0105\u0103\u0001\u0000\u0000\u0000\u0105"+
		"\u0106\u0001\u0000\u0000\u0000\u0106\u0108\u0001\u0000\u0000\u0000\u0107"+
		"\u0105\u0001\u0000\u0000\u0000\u0108\u0109\u0005\u0017\u0000\u0000\u0109"+
		"\u010a\u0005\u0019\u0000\u0000\u010a5\u0001\u0000\u0000\u0000\u010b\u010c"+
		"\u0005\u001b\u0000\u0000\u010c\u010d\u0005\u0016\u0000\u0000\u010d\u0116"+
		"\u0006\u001b\uffff\uffff\u0000\u010e\u0113\u0003\u001e\u000f\u0000\u010f"+
		"\u0110\u0005\u001a\u0000\u0000\u0110\u0112\u0003\u001e\u000f\u0000\u0111"+
		"\u010f\u0001\u0000\u0000\u0000\u0112\u0115\u0001\u0000\u0000\u0000\u0113"+
		"\u0111\u0001\u0000\u0000\u0000\u0113\u0114\u0001\u0000\u0000\u0000\u0114"+
		"\u0117\u0001\u0000\u0000\u0000\u0115\u0113\u0001\u0000\u0000\u0000\u0116"+
		"\u010e\u0001\u0000\u0000\u0000\u0116\u0117\u0001\u0000\u0000\u0000\u0117"+
		"\u0118\u0001\u0000\u0000\u0000\u0118\u0119\u0005\u0017\u0000\u0000\u0119"+
		"7\u0001\u0000\u0000\u0000\u011a\u011d\u0003\u000e\u0007\u0000\u011b\u011d"+
		"\u0003\u0010\b\u0000\u011c\u011a\u0001\u0000\u0000\u0000\u011c\u011b\u0001"+
		"\u0000\u0000\u0000\u011d9\u0001\u0000\u0000\u0000\u011e\u011f\u0003\f"+
		"\u0006\u0000\u011f\u0120\u0005\u001b\u0000\u0000\u0120\u0121\u0005\u0016"+
		"\u0000\u0000\u0121\u0122\u0003F#\u0000\u0122\u0123\u0005\u0017\u0000\u0000"+
		"\u0123\u0124\u0005\u0001\u0000\u0000\u0124\u0125\u0003>\u001f\u0000\u0125"+
		"\u0126\u0006\u001d\uffff\uffff\u0000\u0126\u0127\u0003(\u0014\u0000\u0127"+
		"\u0128\u0005\u0002\u0000\u0000\u0128\u0129\u0006\u001d\uffff\uffff\u0000"+
		"\u0129;\u0001\u0000\u0000\u0000\u012a\u0131\u0003*\u0015\u0000\u012b\u0131"+
		"\u00032\u0019\u0000\u012c\u0131\u0003.\u0017\u0000\u012d\u0131\u00030"+
		"\u0018\u0000\u012e\u0131\u00034\u001a\u0000\u012f\u0131\u00036\u001b\u0000"+
		"\u0130\u012a\u0001\u0000\u0000\u0000\u0130\u012b\u0001\u0000\u0000\u0000"+
		"\u0130\u012c\u0001\u0000\u0000\u0000\u0130\u012d\u0001\u0000\u0000\u0000"+
		"\u0130\u012e\u0001\u0000\u0000\u0000\u0130\u012f\u0001\u0000\u0000\u0000"+
		"\u0131=\u0001\u0000\u0000\u0000\u0132\u0134\u0003@ \u0000\u0133\u0132"+
		"\u0001\u0000\u0000\u0000\u0134\u0137\u0001\u0000\u0000\u0000\u0135\u0133"+
		"\u0001\u0000\u0000\u0000\u0135\u0136\u0001\u0000\u0000\u0000\u0136?\u0001"+
		"\u0000\u0000\u0000\u0137\u0135\u0001\u0000\u0000\u0000\u0138\u0139\u0003"+
		"8\u001c\u0000\u0139\u013a\u0003B!\u0000\u013a\u013b\u0005\u0019\u0000"+
		"\u0000\u013b\u013c\u0006 \uffff\uffff\u0000\u013cA\u0001\u0000\u0000\u0000"+
		"\u013d\u013e\u0005\u001b\u0000\u0000\u013e\u013f\u0003D\"\u0000\u013f"+
		"C\u0001\u0000\u0000\u0000\u0140\u0141\u0005\u001a\u0000\u0000\u0141\u0143"+
		"\u0003B!\u0000\u0142\u0140\u0001\u0000\u0000\u0000\u0143\u0146\u0001\u0000"+
		"\u0000\u0000\u0144\u0142\u0001\u0000\u0000\u0000\u0144\u0145\u0001\u0000"+
		"\u0000\u0000\u0145E\u0001\u0000\u0000\u0000\u0146\u0144\u0001\u0000\u0000"+
		"\u0000\u0147\u014c\u0003H$\u0000\u0148\u0149\u0005\u001a\u0000\u0000\u0149"+
		"\u014b\u0003H$\u0000\u014a\u0148\u0001\u0000\u0000\u0000\u014b\u014e\u0001"+
		"\u0000\u0000\u0000\u014c\u014a\u0001\u0000\u0000\u0000\u014c\u014d\u0001"+
		"\u0000\u0000\u0000\u014dG\u0001\u0000\u0000\u0000\u014e\u014c\u0001\u0000"+
		"\u0000\u0000\u014f\u0150\u00038\u001c\u0000\u0150\u0151\u0005\u001b\u0000"+
		"\u0000\u0151\u0152\u0006$\uffff\uffff\u0000\u0152I\u0001\u0000\u0000\u0000"+
		"\u0017NW\u0082\u008b\u0092\u009d\u00a4\u00a8\u00b6\u00bc\u00c4\u00d9\u00f4"+
		"\u00fc\u0101\u0105\u0113\u0116\u011c\u0130\u0135\u0144\u014c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}