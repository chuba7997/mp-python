// Generated from c:\Users\User\Documents\NL_NNLT\assignment1\initial\src\main\mp\parser\MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BREAK=1, CONTINUE=2, FOR=3, TO=4, DOWNTO=5, DO=6, IF=7, RETURN=8, WHILE=9, 
		BEGIN=10, END=11, FUNCTION=12, PROCEDURE=13, VAR=14, ARRAY=15, OF=16, 
		WITH=17, ADD=18, SUB=19, MUL=20, DIVR=21, NOT=22, MOD=23, SC_OR=24, SC_AND=25, 
		NOTEQUAL=26, EQUAL=27, LESSTHAN=28, GREATERTHAN=29, LESSOREQUAL=30, GREATEROREQUAL=31, 
		DIV=32, ASIGNOP=33, LSB=34, RSB=35, LB=36, RB=37, COLON=38, SEMICOLON=39, 
		DDOT=40, COMMA=41, INTLIT=42, FLOATLIT=43, BOOLEANLIT=44, STRINGLIT=45, 
		BOOLEAN=46, INTEGER=47, REAL=48, STRING=49, T_COMMENT=50, B_COMMENT=51, 
		L_COMMENT=52, WS=53, ID=54, ILLEGAL_ESCAPE=55, UNCLOSE_STRING=56, ILLEGAL_CHAR=57, 
		ERROR_CHAR=58;
	public static final int
		RULE_program = 0, RULE_manyDecl = 1, RULE_vDecl = 2, RULE_varDecl = 3, 
		RULE_arrayDecl = 4, RULE_varName = 5, RULE_mptype = 6;
	public static final String[] ruleNames = {
		"program", "manyDecl", "vDecl", "varDecl", "arrayDecl", "varName", "mptype"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, "'+'", "'-'", "'*'", "'/'", null, 
		null, null, null, "'<>'", "'='", "'<'", "'>'", "'<='", "'>='", null, "':='", 
		"'['", "']'", "'('", "')'", "':'", "';'", "'..'", "','"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "RETURN", 
		"WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "ARRAY", "OF", 
		"WITH", "ADD", "SUB", "MUL", "DIVR", "NOT", "MOD", "SC_OR", "SC_AND", 
		"NOTEQUAL", "EQUAL", "LESSTHAN", "GREATERTHAN", "LESSOREQUAL", "GREATEROREQUAL", 
		"DIV", "ASIGNOP", "LSB", "RSB", "LB", "RB", "COLON", "SEMICOLON", "DDOT", 
		"COMMA", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEAN", "INTEGER", 
		"REAL", "STRING", "T_COMMENT", "B_COMMENT", "L_COMMENT", "WS", "ID", "ILLEGAL_ESCAPE", 
		"UNCLOSE_STRING", "ILLEGAL_CHAR", "ERROR_CHAR"
	};
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
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MPParser.EOF, 0); }
		public List<ManyDeclContext> manyDecl() {
			return getRuleContexts(ManyDeclContext.class);
		}
		public ManyDeclContext manyDecl(int i) {
			return getRuleContext(ManyDeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==ID) {
				{
				{
				setState(14);
				manyDecl();
				}
				}
				setState(19);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(20);
			match(EOF);
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

	public static class ManyDeclContext extends ParserRuleContext {
		public VDeclContext vDecl() {
			return getRuleContext(VDeclContext.class,0);
		}
		public ManyDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_manyDecl; }
	}

	public final ManyDeclContext manyDecl() throws RecognitionException {
		ManyDeclContext _localctx = new ManyDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_manyDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			vDecl();
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

	public static class VDeclContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public ArrayDeclContext arrayDecl() {
			return getRuleContext(ArrayDeclContext.class,0);
		}
		public VDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vDecl; }
	}

	public final VDeclContext vDecl() throws RecognitionException {
		VDeclContext _localctx = new VDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vDecl);
		try {
			setState(26);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				varDecl();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				arrayDecl();
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

	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(MPParser.VAR, 0); }
		public List<VarNameContext> varName() {
			return getRuleContexts(VarNameContext.class);
		}
		public VarNameContext varName(int i) {
			return getRuleContext(VarNameContext.class,i);
		}
		public TerminalNode COLON() { return getToken(MPParser.COLON, 0); }
		public MptypeContext mptype() {
			return getRuleContext(MptypeContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MPParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(MPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MPParser.COMMA, i);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(VAR);
			setState(29);
			varName();
			setState(34);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(30);
				match(COMMA);
				setState(31);
				varName();
				}
				}
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(37);
			match(COLON);
			setState(38);
			mptype();
			setState(39);
			match(SEMICOLON);
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

	public static class ArrayDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public TerminalNode COLON() { return getToken(MPParser.COLON, 0); }
		public TerminalNode ARRAY() { return getToken(MPParser.ARRAY, 0); }
		public TerminalNode LSB() { return getToken(MPParser.LSB, 0); }
		public List<TerminalNode> INTLIT() { return getTokens(MPParser.INTLIT); }
		public TerminalNode INTLIT(int i) {
			return getToken(MPParser.INTLIT, i);
		}
		public TerminalNode RSB() { return getToken(MPParser.RSB, 0); }
		public TerminalNode OF() { return getToken(MPParser.OF, 0); }
		public MptypeContext mptype() {
			return getRuleContext(MptypeContext.class,0);
		}
		public ArrayDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayDecl; }
	}

	public final ArrayDeclContext arrayDecl() throws RecognitionException {
		ArrayDeclContext _localctx = new ArrayDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_arrayDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(ID);
			setState(42);
			match(COLON);
			setState(43);
			match(ARRAY);
			setState(44);
			match(LSB);
			setState(45);
			match(INTLIT);
			setState(46);
			match(DDOT);
			setState(47);
			match(INTLIT);
			setState(48);
			match(RSB);
			setState(49);
			match(OF);
			setState(50);
			mptype();
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

	public static class VarNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public VarNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varName; }
	}

	public final VarNameContext varName() throws RecognitionException {
		VarNameContext _localctx = new VarNameContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(ID);
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

	public static class MptypeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(MPParser.INTEGER, 0); }
		public TerminalNode REAL() { return getToken(MPParser.REAL, 0); }
		public TerminalNode BOOLEAN() { return getToken(MPParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(MPParser.STRING, 0); }
		public MptypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mptype; }
	}

	public final MptypeContext mptype() throws RecognitionException {
		MptypeContext _localctx = new MptypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_mptype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INTEGER) | (1L << REAL) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<;\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13"+
		"\2\3\2\3\2\3\3\3\3\3\4\3\4\5\4\35\n\4\3\5\3\5\3\5\3\5\7\5#\n\5\f\5\16"+
		"\5&\13\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\7\3\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\60\63\2\66\2\23\3\2\2"+
		"\2\4\30\3\2\2\2\6\34\3\2\2\2\b\36\3\2\2\2\n+\3\2\2\2\f\66\3\2\2\2\168"+
		"\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24"+
		"\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\27\7\2\2\3\27\3\3\2\2\2\30\31"+
		"\5\6\4\2\31\5\3\2\2\2\32\35\5\b\5\2\33\35\5\n\6\2\34\32\3\2\2\2\34\33"+
		"\3\2\2\2\35\7\3\2\2\2\36\37\7\20\2\2\37$\5\f\7\2 !\7+\2\2!#\5\f\7\2\""+
		" \3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7(\2"+
		"\2()\5\16\b\2)*\7)\2\2*\t\3\2\2\2+,\78\2\2,-\7(\2\2-.\7\21\2\2./\7$\2"+
		"\2/\60\7,\2\2\60\61\7*\2\2\61\62\7,\2\2\62\63\7%\2\2\63\64\7\22\2\2\64"+
		"\65\5\16\b\2\65\13\3\2\2\2\66\67\78\2\2\67\r\3\2\2\289\t\2\2\29\17\3\2"+
		"\2\2\5\23\34$";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}