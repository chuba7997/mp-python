// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1

from lexerror import *

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BREAK_KW=1, CONTINUE_KW=2, FOR_KW=3, TO_KW=4, DOWNTO_KW=5, DO_KW=6, IF_KW=7, 
		THEN_KW=8, ELSE_KW=9, RETURN_KW=10, WHILE_KW=11, BEGIN_KW=12, END_KW=13, 
		FUNCTION_KW=14, PROCEDURE_KW=15, VAR_KW=16, ARRAY_KW=17, OF_KW=18, WITH_KW=19, 
		ADD_KW=20, SUB_KW=21, MUL_KW=22, DIVR_KW=23, NOT_KW=24, MOD_KW=25, OR_KW=26, 
		AND_KW=27, ORELSE_KW=28, ANDTHEN_KW=29, NOTEQUAL_KW=30, EQUAL_KW=31, LESSTHAN_KW=32, 
		GREATERTHAN_KW=33, LESSOREQUAL_KW=34, GREATEROREQUAL_KW=35, DIV_KW=36, 
		ASSIGN_KW=37, LSB=38, RSB=39, LB=40, RB=41, COLON=42, SEMICOLON=43, DDOT=44, 
		COMMA=45, INTLIT=46, FLOATLIT=47, BOOLEANLIT=48, STRINGLIT=49, BOOLEAN_KW=50, 
		INTEGER_KW=51, REAL_KW=52, STRING_KW=53, T_COMMENT=54, B_COMMENT=55, L_COMMENT=56, 
		ID=57, WS=58, ILLEGAL_CHAR=59, ILLEGAL_ESCAPE=60, UNCLOSE_STRING=61, ERROR_CHAR=62;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
		"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "LETTERS", 
		"BREAK_KW", "CONTINUE_KW", "FOR_KW", "TO_KW", "DOWNTO_KW", "DO_KW", "IF_KW", 
		"THEN_KW", "ELSE_KW", "RETURN_KW", "WHILE_KW", "BEGIN_KW", "END_KW", "FUNCTION_KW", 
		"PROCEDURE_KW", "VAR_KW", "ARRAY_KW", "OF_KW", "WITH_KW", "ADD_KW", "SUB_KW", 
		"MUL_KW", "DIVR_KW", "NOT_KW", "MOD_KW", "OR_KW", "AND_KW", "ORELSE_KW", 
		"ANDTHEN_KW", "NOTEQUAL_KW", "EQUAL_KW", "LESSTHAN_KW", "GREATERTHAN_KW", 
		"LESSOREQUAL_KW", "GREATEROREQUAL_KW", "DIV_KW", "ASSIGN_KW", "LSB", "RSB", 
		"LB", "RB", "COLON", "SEMICOLON", "DDOT", "COMMA", "NUMBER", "INTLIT", 
		"EXPONENT", "FRACTION", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEAN_KW", 
		"INTEGER_KW", "REAL_KW", "STRING_KW", "T_COMMENT", "B_COMMENT", "L_COMMENT", 
		"ID", "WS", "ILLEGAL_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, "'+'", "'-'", "'*'", "'/'", 
		null, null, null, null, null, null, "'<>'", "'='", "'<'", "'>'", "'<='", 
		"'>='", null, "':='", "'['", "']'", "'('", "')'", "':'", "';'", "'..'", 
		"','"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "BREAK_KW", "CONTINUE_KW", "FOR_KW", "TO_KW", "DOWNTO_KW", "DO_KW", 
		"IF_KW", "THEN_KW", "ELSE_KW", "RETURN_KW", "WHILE_KW", "BEGIN_KW", "END_KW", 
		"FUNCTION_KW", "PROCEDURE_KW", "VAR_KW", "ARRAY_KW", "OF_KW", "WITH_KW", 
		"ADD_KW", "SUB_KW", "MUL_KW", "DIVR_KW", "NOT_KW", "MOD_KW", "OR_KW", 
		"AND_KW", "ORELSE_KW", "ANDTHEN_KW", "NOTEQUAL_KW", "EQUAL_KW", "LESSTHAN_KW", 
		"GREATERTHAN_KW", "LESSOREQUAL_KW", "GREATEROREQUAL_KW", "DIV_KW", "ASSIGN_KW", 
		"LSB", "RSB", "LB", "RB", "COLON", "SEMICOLON", "DDOT", "COMMA", "INTLIT", 
		"FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEAN_KW", "INTEGER_KW", "REAL_KW", 
		"STRING_KW", "T_COMMENT", "B_COMMENT", "L_COMMENT", "ID", "WS", "ILLEGAL_CHAR", 
		"ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR"
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


	public MPLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 78:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 88:
			ILLEGAL_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		case 89:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 90:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 91:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.text=self.text[1:-1]
			break;
		}
	}
	private void ILLEGAL_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			raise IllegalCharInString(self.text[1:])
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			raise IllegalEscapeInString(self.text[1:])
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			raise UnclosedString(self.text[1:])
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			raise ErrorToken(self.text)
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@\u026e\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3\2\3\2\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3"+
		"\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23"+
		"\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32"+
		"\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3"+
		"!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3"+
		"&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3"+
		"*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3"+
		"-\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62"+
		"\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67"+
		"\3\67\3\67\3\67\38\38\38\38\38\38\38\38\39\39\39\39\39\39\39\39\39\3:"+
		"\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3B"+
		"\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3K\6K\u01ad\nK\rK"+
		"\16K\u01ae\3L\3L\5L\u01b3\nL\3L\6L\u01b6\nL\rL\16L\u01b7\3M\6M\u01bb\n"+
		"M\rM\16M\u01bc\3M\7M\u01c0\nM\fM\16M\u01c3\13M\3N\6N\u01c6\nN\rN\16N\u01c7"+
		"\3N\5N\u01cb\nN\3N\7N\u01ce\nN\fN\16N\u01d1\13N\3N\7N\u01d4\nN\fN\16N"+
		"\u01d7\13N\3N\5N\u01da\nN\3N\6N\u01dd\nN\rN\16N\u01de\5N\u01e1\nN\3O\3"+
		"O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u01ee\nO\3P\3P\3P\3P\7P\u01f4\nP\fP\16"+
		"P\u01f7\13P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3R\3R\3"+
		"S\3S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\7U\u021c\nU\fU\16U\u021f"+
		"\13U\3U\3U\3U\3U\3U\3V\3V\7V\u0228\nV\fV\16V\u022b\13V\3V\3V\3V\3V\3W"+
		"\3W\3W\3W\7W\u0235\nW\fW\16W\u0238\13W\3W\3W\3X\3X\5X\u023e\nX\3X\3X\3"+
		"X\7X\u0243\nX\fX\16X\u0246\13X\3Y\6Y\u0249\nY\rY\16Y\u024a\3Y\3Y\3Z\3"+
		"Z\3Z\3[\3[\7[\u0254\n[\f[\16[\u0257\13[\3[\3[\7[\u025b\n[\f[\16[\u025e"+
		"\13[\3[\3[\3[\3\\\3\\\7\\\u0265\n\\\f\\\16\\\u0268\13\\\3\\\3\\\3]\3]"+
		"\3]\4\u021d\u0229\2^\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2"+
		"\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\3;"+
		"\4=\5?\6A\7C\bE\tG\nI\13K\fM\rO\16Q\17S\20U\21W\22Y\23[\24]\25_\26a\27"+
		"c\30e\31g\32i\33k\34m\35o\36q\37s u!w\"y#{$}%\177&\u0081\'\u0083(\u0085"+
		")\u0087*\u0089+\u008b,\u008d-\u008f.\u0091/\u0093\2\u0095\60\u0097\2\u0099"+
		"\2\u009b\61\u009d\62\u009f\63\u00a1\64\u00a3\65\u00a5\66\u00a7\67\u00a9"+
		"8\u00ab9\u00ad:\u00af;\u00b1<\u00b3=\u00b5>\u00b7?\u00b9@\3\2&\4\2CCc"+
		"c\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2"+
		"LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4"+
		"\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4\2C"+
		"\\c|\3\2\62;\3\2//\3\2\60\60\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\4"+
		"\2\f\f\17\17\5\2\13\f\17\17\"\"\5\2\f\f\17\17$$\3\2$$\2\u0269\29\3\2\2"+
		"\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2"+
		"G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3"+
		"\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2"+
		"\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2"+
		"m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3"+
		"\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2"+
		"\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2"+
		"\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0095\3\2\2\2\2\u009b"+
		"\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2"+
		"\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad"+
		"\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2"+
		"\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\3\u00bb\3\2\2\2\5\u00bd\3\2\2\2\7\u00bf"+
		"\3\2\2\2\t\u00c1\3\2\2\2\13\u00c3\3\2\2\2\r\u00c5\3\2\2\2\17\u00c7\3\2"+
		"\2\2\21\u00c9\3\2\2\2\23\u00cb\3\2\2\2\25\u00cd\3\2\2\2\27\u00cf\3\2\2"+
		"\2\31\u00d1\3\2\2\2\33\u00d3\3\2\2\2\35\u00d5\3\2\2\2\37\u00d7\3\2\2\2"+
		"!\u00d9\3\2\2\2#\u00db\3\2\2\2%\u00dd\3\2\2\2\'\u00df\3\2\2\2)\u00e1\3"+
		"\2\2\2+\u00e3\3\2\2\2-\u00e5\3\2\2\2/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63"+
		"\u00eb\3\2\2\2\65\u00ed\3\2\2\2\67\u00ef\3\2\2\29\u00f1\3\2\2\2;\u00f7"+
		"\3\2\2\2=\u0100\3\2\2\2?\u0104\3\2\2\2A\u0107\3\2\2\2C\u010e\3\2\2\2E"+
		"\u0111\3\2\2\2G\u0114\3\2\2\2I\u0119\3\2\2\2K\u011e\3\2\2\2M\u0125\3\2"+
		"\2\2O\u012b\3\2\2\2Q\u0131\3\2\2\2S\u0135\3\2\2\2U\u013e\3\2\2\2W\u0148"+
		"\3\2\2\2Y\u014c\3\2\2\2[\u0152\3\2\2\2]\u0155\3\2\2\2_\u015a\3\2\2\2a"+
		"\u015c\3\2\2\2c\u015e\3\2\2\2e\u0160\3\2\2\2g\u0162\3\2\2\2i\u0166\3\2"+
		"\2\2k\u016a\3\2\2\2m\u016d\3\2\2\2o\u0171\3\2\2\2q\u0179\3\2\2\2s\u0182"+
		"\3\2\2\2u\u0185\3\2\2\2w\u0187\3\2\2\2y\u0189\3\2\2\2{\u018b\3\2\2\2}"+
		"\u018e\3\2\2\2\177\u0191\3\2\2\2\u0081\u0195\3\2\2\2\u0083\u0198\3\2\2"+
		"\2\u0085\u019a\3\2\2\2\u0087\u019c\3\2\2\2\u0089\u019e\3\2\2\2\u008b\u01a0"+
		"\3\2\2\2\u008d\u01a2\3\2\2\2\u008f\u01a4\3\2\2\2\u0091\u01a7\3\2\2\2\u0093"+
		"\u01a9\3\2\2\2\u0095\u01ac\3\2\2\2\u0097\u01b0\3\2\2\2\u0099\u01ba\3\2"+
		"\2\2\u009b\u01e0\3\2\2\2\u009d\u01ed\3\2\2\2\u009f\u01ef\3\2\2\2\u00a1"+
		"\u01fb\3\2\2\2\u00a3\u0203\3\2\2\2\u00a5\u020b\3\2\2\2\u00a7\u0210\3\2"+
		"\2\2\u00a9\u0217\3\2\2\2\u00ab\u0225\3\2\2\2\u00ad\u0230\3\2\2\2\u00af"+
		"\u023d\3\2\2\2\u00b1\u0248\3\2\2\2\u00b3\u024e\3\2\2\2\u00b5\u0251\3\2"+
		"\2\2\u00b7\u0262\3\2\2\2\u00b9\u026b\3\2\2\2\u00bb\u00bc\t\2\2\2\u00bc"+
		"\4\3\2\2\2\u00bd\u00be\t\3\2\2\u00be\6\3\2\2\2\u00bf\u00c0\t\4\2\2\u00c0"+
		"\b\3\2\2\2\u00c1\u00c2\t\5\2\2\u00c2\n\3\2\2\2\u00c3\u00c4\t\6\2\2\u00c4"+
		"\f\3\2\2\2\u00c5\u00c6\t\7\2\2\u00c6\16\3\2\2\2\u00c7\u00c8\t\b\2\2\u00c8"+
		"\20\3\2\2\2\u00c9\u00ca\t\t\2\2\u00ca\22\3\2\2\2\u00cb\u00cc\t\n\2\2\u00cc"+
		"\24\3\2\2\2\u00cd\u00ce\t\13\2\2\u00ce\26\3\2\2\2\u00cf\u00d0\t\f\2\2"+
		"\u00d0\30\3\2\2\2\u00d1\u00d2\t\r\2\2\u00d2\32\3\2\2\2\u00d3\u00d4\t\16"+
		"\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\t\17\2\2\u00d6\36\3\2\2\2\u00d7\u00d8"+
		"\t\20\2\2\u00d8 \3\2\2\2\u00d9\u00da\t\21\2\2\u00da\"\3\2\2\2\u00db\u00dc"+
		"\t\22\2\2\u00dc$\3\2\2\2\u00dd\u00de\t\23\2\2\u00de&\3\2\2\2\u00df\u00e0"+
		"\t\24\2\2\u00e0(\3\2\2\2\u00e1\u00e2\t\25\2\2\u00e2*\3\2\2\2\u00e3\u00e4"+
		"\t\26\2\2\u00e4,\3\2\2\2\u00e5\u00e6\t\27\2\2\u00e6.\3\2\2\2\u00e7\u00e8"+
		"\t\30\2\2\u00e8\60\3\2\2\2\u00e9\u00ea\t\31\2\2\u00ea\62\3\2\2\2\u00eb"+
		"\u00ec\t\32\2\2\u00ec\64\3\2\2\2\u00ed\u00ee\t\33\2\2\u00ee\66\3\2\2\2"+
		"\u00ef\u00f0\t\34\2\2\u00f08\3\2\2\2\u00f1\u00f2\5\5\3\2\u00f2\u00f3\5"+
		"%\23\2\u00f3\u00f4\5\13\6\2\u00f4\u00f5\5\3\2\2\u00f5\u00f6\5\27\f\2\u00f6"+
		":\3\2\2\2\u00f7\u00f8\5\7\4\2\u00f8\u00f9\5\37\20\2\u00f9\u00fa\5\35\17"+
		"\2\u00fa\u00fb\5)\25\2\u00fb\u00fc\5\23\n\2\u00fc\u00fd\5\35\17\2\u00fd"+
		"\u00fe\5+\26\2\u00fe\u00ff\5\13\6\2\u00ff<\3\2\2\2\u0100\u0101\5\r\7\2"+
		"\u0101\u0102\5\37\20\2\u0102\u0103\5%\23\2\u0103>\3\2\2\2\u0104\u0105"+
		"\5)\25\2\u0105\u0106\5\37\20\2\u0106@\3\2\2\2\u0107\u0108\5\t\5\2\u0108"+
		"\u0109\5\37\20\2\u0109\u010a\5/\30\2\u010a\u010b\5\35\17\2\u010b\u010c"+
		"\5)\25\2\u010c\u010d\5\37\20\2\u010dB\3\2\2\2\u010e\u010f\5\t\5\2\u010f"+
		"\u0110\5\37\20\2\u0110D\3\2\2\2\u0111\u0112\5\23\n\2\u0112\u0113\5\r\7"+
		"\2\u0113F\3\2\2\2\u0114\u0115\5)\25\2\u0115\u0116\5\21\t\2\u0116\u0117"+
		"\5\13\6\2\u0117\u0118\5\35\17\2\u0118H\3\2\2\2\u0119\u011a\5\13\6\2\u011a"+
		"\u011b\5\31\r\2\u011b\u011c\5\'\24\2\u011c\u011d\5\13\6\2\u011dJ\3\2\2"+
		"\2\u011e\u011f\5%\23\2\u011f\u0120\5\13\6\2\u0120\u0121\5)\25\2\u0121"+
		"\u0122\5+\26\2\u0122\u0123\5%\23\2\u0123\u0124\5\35\17\2\u0124L\3\2\2"+
		"\2\u0125\u0126\5/\30\2\u0126\u0127\5\21\t\2\u0127\u0128\5\23\n\2\u0128"+
		"\u0129\5\31\r\2\u0129\u012a\5\13\6\2\u012aN\3\2\2\2\u012b\u012c\5\5\3"+
		"\2\u012c\u012d\5\13\6\2\u012d\u012e\5\17\b\2\u012e\u012f\5\23\n\2\u012f"+
		"\u0130\5\35\17\2\u0130P\3\2\2\2\u0131\u0132\5\13\6\2\u0132\u0133\5\35"+
		"\17\2\u0133\u0134\5\t\5\2\u0134R\3\2\2\2\u0135\u0136\5\r\7\2\u0136\u0137"+
		"\5+\26\2\u0137\u0138\5\35\17\2\u0138\u0139\5\7\4\2\u0139\u013a\5)\25\2"+
		"\u013a\u013b\5\23\n\2\u013b\u013c\5\37\20\2\u013c\u013d\5\35\17\2\u013d"+
		"T\3\2\2\2\u013e\u013f\5!\21\2\u013f\u0140\5%\23\2\u0140\u0141\5\37\20"+
		"\2\u0141\u0142\5\7\4\2\u0142\u0143\5\13\6\2\u0143\u0144\5\t\5\2\u0144"+
		"\u0145\5+\26\2\u0145\u0146\5%\23\2\u0146\u0147\5\13\6\2\u0147V\3\2\2\2"+
		"\u0148\u0149\5-\27\2\u0149\u014a\5\3\2\2\u014a\u014b\5%\23\2\u014bX\3"+
		"\2\2\2\u014c\u014d\5\3\2\2\u014d\u014e\5%\23\2\u014e\u014f\5%\23\2\u014f"+
		"\u0150\5\3\2\2\u0150\u0151\5\63\32\2\u0151Z\3\2\2\2\u0152\u0153\5\37\20"+
		"\2\u0153\u0154\5\r\7\2\u0154\\\3\2\2\2\u0155\u0156\5/\30\2\u0156\u0157"+
		"\5\23\n\2\u0157\u0158\5)\25\2\u0158\u0159\5\21\t\2\u0159^\3\2\2\2\u015a"+
		"\u015b\7-\2\2\u015b`\3\2\2\2\u015c\u015d\7/\2\2\u015db\3\2\2\2\u015e\u015f"+
		"\7,\2\2\u015fd\3\2\2\2\u0160\u0161\7\61\2\2\u0161f\3\2\2\2\u0162\u0163"+
		"\5\35\17\2\u0163\u0164\5\37\20\2\u0164\u0165\5)\25\2\u0165h\3\2\2\2\u0166"+
		"\u0167\5\33\16\2\u0167\u0168\5\37\20\2\u0168\u0169\5\t\5\2\u0169j\3\2"+
		"\2\2\u016a\u016b\5\37\20\2\u016b\u016c\5%\23\2\u016cl\3\2\2\2\u016d\u016e"+
		"\5\3\2\2\u016e\u016f\5\35\17\2\u016f\u0170\5\t\5\2\u0170n\3\2\2\2\u0171"+
		"\u0172\5\37\20\2\u0172\u0173\5%\23\2\u0173\u0174\7\"\2\2\u0174\u0175\5"+
		"\13\6\2\u0175\u0176\5\31\r\2\u0176\u0177\5\'\24\2\u0177\u0178\5\13\6\2"+
		"\u0178p\3\2\2\2\u0179\u017a\5\3\2\2\u017a\u017b\5\35\17\2\u017b\u017c"+
		"\5\t\5\2\u017c\u017d\7\"\2\2\u017d\u017e\5)\25\2\u017e\u017f\5\21\t\2"+
		"\u017f\u0180\5\13\6\2\u0180\u0181\5\35\17\2\u0181r\3\2\2\2\u0182\u0183"+
		"\7>\2\2\u0183\u0184\7@\2\2\u0184t\3\2\2\2\u0185\u0186\7?\2\2\u0186v\3"+
		"\2\2\2\u0187\u0188\7>\2\2\u0188x\3\2\2\2\u0189\u018a\7@\2\2\u018az\3\2"+
		"\2\2\u018b\u018c\7>\2\2\u018c\u018d\7?\2\2\u018d|\3\2\2\2\u018e\u018f"+
		"\7@\2\2\u018f\u0190\7?\2\2\u0190~\3\2\2\2\u0191\u0192\5\t\5\2\u0192\u0193"+
		"\5\23\n\2\u0193\u0194\5-\27\2\u0194\u0080\3\2\2\2\u0195\u0196\7<\2\2\u0196"+
		"\u0197\7?\2\2\u0197\u0082\3\2\2\2\u0198\u0199\7]\2\2\u0199\u0084\3\2\2"+
		"\2\u019a\u019b\7_\2\2\u019b\u0086\3\2\2\2\u019c\u019d\7*\2\2\u019d\u0088"+
		"\3\2\2\2\u019e\u019f\7+\2\2\u019f\u008a\3\2\2\2\u01a0\u01a1\7<\2\2\u01a1"+
		"\u008c\3\2\2\2\u01a2\u01a3\7=\2\2\u01a3\u008e\3\2\2\2\u01a4\u01a5\7\60"+
		"\2\2\u01a5\u01a6\7\60\2\2\u01a6\u0090\3\2\2\2\u01a7\u01a8\7.\2\2\u01a8"+
		"\u0092\3\2\2\2\u01a9\u01aa\t\35\2\2\u01aa\u0094\3\2\2\2\u01ab\u01ad\5"+
		"\u0093J\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac\3\2\2\2"+
		"\u01ae\u01af\3\2\2\2\u01af\u0096\3\2\2\2\u01b0\u01b2\5\13\6\2\u01b1\u01b3"+
		"\t\36\2\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2"+
		"\u01b4\u01b6\5\u0093J\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7"+
		"\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u0098\3\2\2\2\u01b9\u01bb\5\u0093"+
		"J\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc"+
		"\u01bd\3\2\2\2\u01bd\u01c1\3\2\2\2\u01be\u01c0\5\u0097L\2\u01bf\u01be"+
		"\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2"+
		"\u009a\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c6\5\u0093J\2\u01c5\u01c4"+
		"\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8"+
		"\u01ca\3\2\2\2\u01c9\u01cb\t\37\2\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb\3"+
		"\2\2\2\u01cb\u01cf\3\2\2\2\u01cc\u01ce\5\u0099M\2\u01cd\u01cc\3\2\2\2"+
		"\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01e1"+
		"\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d4\5\u0093J\2\u01d3\u01d2\3\2\2"+
		"\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d9"+
		"\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01da\t\37\2\2\u01d9\u01d8\3\2\2\2"+
		"\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01dd\5\u0099M\2\u01dc"+
		"\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2"+
		"\2\2\u01df\u01e1\3\2\2\2\u01e0\u01c5\3\2\2\2\u01e0\u01d5\3\2\2\2\u01e1"+
		"\u009c\3\2\2\2\u01e2\u01e3\5)\25\2\u01e3\u01e4\5%\23\2\u01e4\u01e5\5+"+
		"\26\2\u01e5\u01e6\5\13\6\2\u01e6\u01ee\3\2\2\2\u01e7\u01e8\5\r\7\2\u01e8"+
		"\u01e9\5\3\2\2\u01e9\u01ea\5\31\r\2\u01ea\u01eb\5\'\24\2\u01eb\u01ec\5"+
		"\13\6\2\u01ec\u01ee\3\2\2\2\u01ed\u01e2\3\2\2\2\u01ed\u01e7\3\2\2\2\u01ee"+
		"\u009e\3\2\2\2\u01ef\u01f5\7$\2\2\u01f0\u01f4\n \2\2\u01f1\u01f2\7^\2"+
		"\2\u01f2\u01f4\t!\2\2\u01f3\u01f0\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f7"+
		"\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7"+
		"\u01f5\3\2\2\2\u01f8\u01f9\7$\2\2\u01f9\u01fa\bP\2\2\u01fa\u00a0\3\2\2"+
		"\2\u01fb\u01fc\5\5\3\2\u01fc\u01fd\5\37\20\2\u01fd\u01fe\5\37\20\2\u01fe"+
		"\u01ff\5\31\r\2\u01ff\u0200\5\13\6\2\u0200\u0201\5\3\2\2\u0201\u0202\5"+
		"\35\17\2\u0202\u00a2\3\2\2\2\u0203\u0204\5\23\n\2\u0204\u0205\5\35\17"+
		"\2\u0205\u0206\5)\25\2\u0206\u0207\5\13\6\2\u0207\u0208\5\17\b\2\u0208"+
		"\u0209\5\13\6\2\u0209\u020a\5%\23\2\u020a\u00a4\3\2\2\2\u020b\u020c\5"+
		"%\23\2\u020c\u020d\5\13\6\2\u020d\u020e\5\3\2\2\u020e\u020f\5\31\r\2\u020f"+
		"\u00a6\3\2\2\2\u0210\u0211\5\'\24\2\u0211\u0212\5)\25\2\u0212\u0213\5"+
		"%\23\2\u0213\u0214\5\23\n\2\u0214\u0215\5\35\17\2\u0215\u0216\5\17\b\2"+
		"\u0216\u00a8\3\2\2\2\u0217\u0218\7*\2\2\u0218\u0219\7,\2\2\u0219\u021d"+
		"\3\2\2\2\u021a\u021c\13\2\2\2\u021b\u021a\3\2\2\2\u021c\u021f\3\2\2\2"+
		"\u021d\u021e\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d"+
		"\3\2\2\2\u0220\u0221\7,\2\2\u0221\u0222\7+\2\2\u0222\u0223\3\2\2\2\u0223"+
		"\u0224\bU\3\2\u0224\u00aa\3\2\2\2\u0225\u0229\7}\2\2\u0226\u0228\13\2"+
		"\2\2\u0227\u0226\3\2\2\2\u0228\u022b\3\2\2\2\u0229\u022a\3\2\2\2\u0229"+
		"\u0227\3\2\2\2\u022a\u022c\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022d\7\177"+
		"\2\2\u022d\u022e\3\2\2\2\u022e\u022f\bV\3\2\u022f\u00ac\3\2\2\2\u0230"+
		"\u0231\7\61\2\2\u0231\u0232\7\61\2\2\u0232\u0236\3\2\2\2\u0233\u0235\n"+
		"\"\2\2\u0234\u0233\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236"+
		"\u0237\3\2\2\2\u0237\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\bW"+
		"\3\2\u023a\u00ae\3\2\2\2\u023b\u023e\5\67\34\2\u023c\u023e\7a\2\2\u023d"+
		"\u023b\3\2\2\2\u023d\u023c\3\2\2\2\u023e\u0244\3\2\2\2\u023f\u0243\5\67"+
		"\34\2\u0240\u0243\5\u0093J\2\u0241\u0243\7a\2\2\u0242\u023f\3\2\2\2\u0242"+
		"\u0240\3\2\2\2\u0242\u0241\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2"+
		"\2\2\u0244\u0245\3\2\2\2\u0245\u00b0\3\2\2\2\u0246\u0244\3\2\2\2\u0247"+
		"\u0249\t#\2\2\u0248\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0248\3\2"+
		"\2\2\u024a\u024b\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\bY\3\2\u024d"+
		"\u00b2\3\2\2\2\u024e\u024f\13\2\2\2\u024f\u0250\bZ\4\2\u0250\u00b4\3\2"+
		"\2\2\u0251\u0255\7$\2\2\u0252\u0254\n$\2\2\u0253\u0252\3\2\2\2\u0254\u0257"+
		"\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0258\3\2\2\2\u0257"+
		"\u0255\3\2\2\2\u0258\u025c\7^\2\2\u0259\u025b\n!\2\2\u025a\u0259\3\2\2"+
		"\2\u025b\u025e\3\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025f"+
		"\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0260\7$\2\2\u0260\u0261\b[\5\2\u0261"+
		"\u00b6\3\2\2\2\u0262\u0266\7$\2\2\u0263\u0265\n%\2\2\u0264\u0263\3\2\2"+
		"\2\u0265\u0268\3\2\2\2\u0266\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0269"+
		"\3\2\2\2\u0268\u0266\3\2\2\2\u0269\u026a\b\\\6\2\u026a\u00b8\3\2\2\2\u026b"+
		"\u026c\13\2\2\2\u026c\u026d\b]\7\2\u026d\u00ba\3\2\2\2\34\2\u01ae\u01b2"+
		"\u01b7\u01bc\u01c1\u01c7\u01ca\u01cf\u01d5\u01d9\u01de\u01e0\u01ed\u01f3"+
		"\u01f5\u021d\u0229\u0236\u023d\u0242\u0244\u024a\u0255\u025c\u0266\b\3"+
		"P\2\b\2\2\3Z\3\3[\4\3\\\5\3]\6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}