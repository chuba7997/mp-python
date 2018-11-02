// Generated from c:\Users\User\Documents\NL_NNLT\assignment1\initial\src\main\mp\parser\MP.g4 by ANTLR 4.7.1

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
		BREAK=1, CONTINUE=2, FOR=3, TO=4, DOWNTO=5, DO=6, IF=7, RETURN=8, WHILE=9, 
		BEGIN=10, END=11, FUNCTION=12, PROCEDURE=13, VAR=14, ARRAY=15, OF=16, 
		WITH=17, ADD=18, SUB=19, MUL=20, DIVR=21, NOT=22, MOD=23, SC_OR=24, SC_AND=25, 
		NOTEQUAL=26, EQUAL=27, LESSTHAN=28, GREATERTHAN=29, LESSOREQUAL=30, GREATEROREQUAL=31, 
		DIV=32, ASIGNOP=33, LSB=34, RSB=35, LB=36, RB=37, COLON=38, SEMICOLON=39, 
		DDOT=40, COMMA=41, INTLIT=42, FLOATLIT=43, BOOLEANLIT=44, STRINGLIT=45, 
		BOOLEAN=46, INTEGER=47, REAL=48, STRING=49, T_COMMENT=50, B_COMMENT=51, 
		L_COMMENT=52, WS=53, ID=54, ILLEGAL_ESCAPE=55, UNCLOSE_STRING=56, ILLEGAL_CHAR=57, 
		ERROR_CHAR=58;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
		"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "LETTERS", 
		"NUMBER", "ESCAPE_SEQUENCE", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
		"DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
		"PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "WITH", "ADD", "SUB", 
		"MUL", "DIVR", "NOT", "MOD", "OR", "AND", "SC_OR", "SC_AND", "NOTEQUAL", 
		"EQUAL", "LESSTHAN", "GREATERTHAN", "LESSOREQUAL", "GREATEROREQUAL", "DIV", 
		"ASIGNOP", "LSB", "RSB", "LB", "RB", "COLON", "SEMICOLON", "DDOT", "COMMA", 
		"INTLIT", "EXPONENT", "FRACTION", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
		"BOOLEAN", "INTEGER", "REAL", "STRING", "T_COMMENT", "B_COMMENT", "L_COMMENT", 
		"WS", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ILLEGAL_CHAR", "ERROR_CHAR"
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
		case 81:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 91:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 92:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 93:
			ILLEGAL_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		case 94:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			setText(getText().substring(1, getText().length()-1));
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			raise ErrorToken(self.text)
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			raise ErrorToken(self.text)
			break;
		}
	}
	private void ILLEGAL_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			raise ErrorToken(self.text)
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<\u026e\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
		"`\t`\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3"+
		"\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3"+
		"\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3"+
		"\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3"+
		"\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3"+
		"\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3"+
		"\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3"+
		"*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3"+
		"-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3"+
		"\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3"+
		"\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\39\39\39\39\3:\3:\3:\3;\3;\3"+
		";\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\3C\3C\3"+
		"D\3D\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3L\3M\3"+
		"M\3N\6N\u01b6\nN\rN\16N\u01b7\3O\3O\5O\u01bc\nO\3O\6O\u01bf\nO\rO\16O"+
		"\u01c0\3P\6P\u01c4\nP\rP\16P\u01c5\3P\7P\u01c9\nP\fP\16P\u01cc\13P\3Q"+
		"\6Q\u01cf\nQ\rQ\16Q\u01d0\3Q\5Q\u01d4\nQ\3Q\7Q\u01d7\nQ\fQ\16Q\u01da\13"+
		"Q\3Q\7Q\u01dd\nQ\fQ\16Q\u01e0\13Q\3Q\5Q\u01e3\nQ\3Q\6Q\u01e6\nQ\rQ\16"+
		"Q\u01e7\5Q\u01ea\nQ\3R\3R\5R\u01ee\nR\3S\3S\3S\7S\u01f3\nS\fS\16S\u01f6"+
		"\13S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3U\3U\3V\3V\3"+
		"V\3V\3V\3W\3W\3W\3W\3W\3W\3W\3X\3X\3X\3X\7X\u021b\nX\fX\16X\u021e\13X"+
		"\3X\3X\3X\3X\3X\3Y\3Y\7Y\u0227\nY\fY\16Y\u022a\13Y\3Y\3Y\3Y\3Y\3Z\3Z\3"+
		"Z\3Z\7Z\u0234\nZ\fZ\16Z\u0237\13Z\3Z\3Z\3[\6[\u023c\n[\r[\16[\u023d\3"+
		"[\3[\3\\\3\\\5\\\u0244\n\\\3\\\3\\\3\\\7\\\u0249\n\\\f\\\16\\\u024c\13"+
		"\\\3]\3]\7]\u0250\n]\f]\16]\u0253\13]\3]\3]\7]\u0257\n]\f]\16]\u025a\13"+
		"]\3]\3]\3]\3^\3^\7^\u0261\n^\f^\16^\u0264\13^\3^\3^\3^\3_\3_\3_\3`\3`"+
		"\3`\4\u021c\u0228\2a\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2"+
		"\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;"+
		"\2=\3?\4A\5C\6E\7G\bI\tK\2M\2O\nQ\13S\fU\rW\16Y\17[\20]\2_\2a\21c\22e"+
		"\23g\24i\25k\26m\27o\30q\31s\2u\2w\32y\33{\34}\35\177\36\u0081\37\u0083"+
		" \u0085!\u0087\"\u0089#\u008b$\u008d%\u008f&\u0091\'\u0093(\u0095)\u0097"+
		"*\u0099+\u009b,\u009d\2\u009f\2\u00a1-\u00a3.\u00a5/\u00a7\60\u00a9\61"+
		"\u00ab\62\u00ad\63\u00af\64\u00b1\65\u00b3\66\u00b5\67\u00b78\u00b99\u00bb"+
		":\u00bd;\u00bf<\3\2&\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4"+
		"\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQq"+
		"q\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2"+
		"ZZzz\4\2[[{{\4\2\\\\||\4\2C\\c|\3\2\62;\n\2$$))^^ddhhppttvv\3\2//\3\2"+
		"\60\60\6\2\f\f\17\17$$^^\4\2\f\f\17\17\5\2\13\f\17\17\"\"\5\2\f\f\17\17"+
		"$$\3\2$$\2\u0262\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2"+
		"\2\2G\3\2\2\2\2I\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2"+
		"W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3"+
		"\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2w\3\2\2"+
		"\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083"+
		"\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2"+
		"\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095"+
		"\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u00a1\3\2\2"+
		"\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab"+
		"\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2"+
		"\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd"+
		"\3\2\2\2\2\u00bf\3\2\2\2\3\u00c1\3\2\2\2\5\u00c3\3\2\2\2\7\u00c5\3\2\2"+
		"\2\t\u00c7\3\2\2\2\13\u00c9\3\2\2\2\r\u00cb\3\2\2\2\17\u00cd\3\2\2\2\21"+
		"\u00cf\3\2\2\2\23\u00d1\3\2\2\2\25\u00d3\3\2\2\2\27\u00d5\3\2\2\2\31\u00d7"+
		"\3\2\2\2\33\u00d9\3\2\2\2\35\u00db\3\2\2\2\37\u00dd\3\2\2\2!\u00df\3\2"+
		"\2\2#\u00e1\3\2\2\2%\u00e3\3\2\2\2\'\u00e5\3\2\2\2)\u00e7\3\2\2\2+\u00e9"+
		"\3\2\2\2-\u00eb\3\2\2\2/\u00ed\3\2\2\2\61\u00ef\3\2\2\2\63\u00f1\3\2\2"+
		"\2\65\u00f3\3\2\2\2\67\u00f5\3\2\2\29\u00f7\3\2\2\2;\u00f9\3\2\2\2=\u00fc"+
		"\3\2\2\2?\u0102\3\2\2\2A\u010b\3\2\2\2C\u010f\3\2\2\2E\u0112\3\2\2\2G"+
		"\u0119\3\2\2\2I\u011c\3\2\2\2K\u011f\3\2\2\2M\u0124\3\2\2\2O\u0129\3\2"+
		"\2\2Q\u0130\3\2\2\2S\u0136\3\2\2\2U\u013c\3\2\2\2W\u0140\3\2\2\2Y\u0149"+
		"\3\2\2\2[\u0153\3\2\2\2]\u0157\3\2\2\2_\u015c\3\2\2\2a\u0162\3\2\2\2c"+
		"\u0168\3\2\2\2e\u016b\3\2\2\2g\u0170\3\2\2\2i\u0172\3\2\2\2k\u0174\3\2"+
		"\2\2m\u0176\3\2\2\2o\u0178\3\2\2\2q\u017c\3\2\2\2s\u0180\3\2\2\2u\u0183"+
		"\3\2\2\2w\u0187\3\2\2\2y\u018a\3\2\2\2{\u018d\3\2\2\2}\u0190\3\2\2\2\177"+
		"\u0192\3\2\2\2\u0081\u0194\3\2\2\2\u0083\u0196\3\2\2\2\u0085\u0199\3\2"+
		"\2\2\u0087\u019c\3\2\2\2\u0089\u01a0\3\2\2\2\u008b\u01a3\3\2\2\2\u008d"+
		"\u01a5\3\2\2\2\u008f\u01a7\3\2\2\2\u0091\u01a9\3\2\2\2\u0093\u01ab\3\2"+
		"\2\2\u0095\u01ad\3\2\2\2\u0097\u01af\3\2\2\2\u0099\u01b2\3\2\2\2\u009b"+
		"\u01b5\3\2\2\2\u009d\u01b9\3\2\2\2\u009f\u01c3\3\2\2\2\u00a1\u01e9\3\2"+
		"\2\2\u00a3\u01ed\3\2\2\2\u00a5\u01ef\3\2\2\2\u00a7\u01fa\3\2\2\2\u00a9"+
		"\u0202\3\2\2\2\u00ab\u020a\3\2\2\2\u00ad\u020f\3\2\2\2\u00af\u0216\3\2"+
		"\2\2\u00b1\u0224\3\2\2\2\u00b3\u022f\3\2\2\2\u00b5\u023b\3\2\2\2\u00b7"+
		"\u0243\3\2\2\2\u00b9\u024d\3\2\2\2\u00bb\u025e\3\2\2\2\u00bd\u0268\3\2"+
		"\2\2\u00bf\u026b\3\2\2\2\u00c1\u00c2\t\2\2\2\u00c2\4\3\2\2\2\u00c3\u00c4"+
		"\t\3\2\2\u00c4\6\3\2\2\2\u00c5\u00c6\t\4\2\2\u00c6\b\3\2\2\2\u00c7\u00c8"+
		"\t\5\2\2\u00c8\n\3\2\2\2\u00c9\u00ca\t\6\2\2\u00ca\f\3\2\2\2\u00cb\u00cc"+
		"\t\7\2\2\u00cc\16\3\2\2\2\u00cd\u00ce\t\b\2\2\u00ce\20\3\2\2\2\u00cf\u00d0"+
		"\t\t\2\2\u00d0\22\3\2\2\2\u00d1\u00d2\t\n\2\2\u00d2\24\3\2\2\2\u00d3\u00d4"+
		"\t\13\2\2\u00d4\26\3\2\2\2\u00d5\u00d6\t\f\2\2\u00d6\30\3\2\2\2\u00d7"+
		"\u00d8\t\r\2\2\u00d8\32\3\2\2\2\u00d9\u00da\t\16\2\2\u00da\34\3\2\2\2"+
		"\u00db\u00dc\t\17\2\2\u00dc\36\3\2\2\2\u00dd\u00de\t\20\2\2\u00de \3\2"+
		"\2\2\u00df\u00e0\t\21\2\2\u00e0\"\3\2\2\2\u00e1\u00e2\t\22\2\2\u00e2$"+
		"\3\2\2\2\u00e3\u00e4\t\23\2\2\u00e4&\3\2\2\2\u00e5\u00e6\t\24\2\2\u00e6"+
		"(\3\2\2\2\u00e7\u00e8\t\25\2\2\u00e8*\3\2\2\2\u00e9\u00ea\t\26\2\2\u00ea"+
		",\3\2\2\2\u00eb\u00ec\t\27\2\2\u00ec.\3\2\2\2\u00ed\u00ee\t\30\2\2\u00ee"+
		"\60\3\2\2\2\u00ef\u00f0\t\31\2\2\u00f0\62\3\2\2\2\u00f1\u00f2\t\32\2\2"+
		"\u00f2\64\3\2\2\2\u00f3\u00f4\t\33\2\2\u00f4\66\3\2\2\2\u00f5\u00f6\t"+
		"\34\2\2\u00f68\3\2\2\2\u00f7\u00f8\t\35\2\2\u00f8:\3\2\2\2\u00f9\u00fa"+
		"\7^\2\2\u00fa\u00fb\t\36\2\2\u00fb<\3\2\2\2\u00fc\u00fd\5\5\3\2\u00fd"+
		"\u00fe\5%\23\2\u00fe\u00ff\5\13\6\2\u00ff\u0100\5\3\2\2\u0100\u0101\5"+
		"\27\f\2\u0101>\3\2\2\2\u0102\u0103\5\7\4\2\u0103\u0104\5\37\20\2\u0104"+
		"\u0105\5\35\17\2\u0105\u0106\5)\25\2\u0106\u0107\5\23\n\2\u0107\u0108"+
		"\5\35\17\2\u0108\u0109\5+\26\2\u0109\u010a\5\13\6\2\u010a@\3\2\2\2\u010b"+
		"\u010c\5\r\7\2\u010c\u010d\5\37\20\2\u010d\u010e\5%\23\2\u010eB\3\2\2"+
		"\2\u010f\u0110\5)\25\2\u0110\u0111\5\37\20\2\u0111D\3\2\2\2\u0112\u0113"+
		"\5\t\5\2\u0113\u0114\5\37\20\2\u0114\u0115\5/\30\2\u0115\u0116\5\35\17"+
		"\2\u0116\u0117\5)\25\2\u0117\u0118\5\37\20\2\u0118F\3\2\2\2\u0119\u011a"+
		"\5\t\5\2\u011a\u011b\5\37\20\2\u011bH\3\2\2\2\u011c\u011d\5\23\n\2\u011d"+
		"\u011e\5\r\7\2\u011eJ\3\2\2\2\u011f\u0120\5)\25\2\u0120\u0121\5\21\t\2"+
		"\u0121\u0122\5\13\6\2\u0122\u0123\5\35\17\2\u0123L\3\2\2\2\u0124\u0125"+
		"\5\13\6\2\u0125\u0126\5\31\r\2\u0126\u0127\5\'\24\2\u0127\u0128\5\13\6"+
		"\2\u0128N\3\2\2\2\u0129\u012a\5%\23\2\u012a\u012b\5\13\6\2\u012b\u012c"+
		"\5)\25\2\u012c\u012d\5+\26\2\u012d\u012e\5%\23\2\u012e\u012f\5\35\17\2"+
		"\u012fP\3\2\2\2\u0130\u0131\5/\30\2\u0131\u0132\5\21\t\2\u0132\u0133\5"+
		"\23\n\2\u0133\u0134\5\31\r\2\u0134\u0135\5\13\6\2\u0135R\3\2\2\2\u0136"+
		"\u0137\5\5\3\2\u0137\u0138\5\13\6\2\u0138\u0139\5\17\b\2\u0139\u013a\5"+
		"\23\n\2\u013a\u013b\5\35\17\2\u013bT\3\2\2\2\u013c\u013d\5\13\6\2\u013d"+
		"\u013e\5\35\17\2\u013e\u013f\5\t\5\2\u013fV\3\2\2\2\u0140\u0141\5\r\7"+
		"\2\u0141\u0142\5+\26\2\u0142\u0143\5\35\17\2\u0143\u0144\5\7\4\2\u0144"+
		"\u0145\5)\25\2\u0145\u0146\5\23\n\2\u0146\u0147\5\37\20\2\u0147\u0148"+
		"\5\35\17\2\u0148X\3\2\2\2\u0149\u014a\5!\21\2\u014a\u014b\5%\23\2\u014b"+
		"\u014c\5\37\20\2\u014c\u014d\5\7\4\2\u014d\u014e\5\13\6\2\u014e\u014f"+
		"\5\t\5\2\u014f\u0150\5+\26\2\u0150\u0151\5%\23\2\u0151\u0152\5\13\6\2"+
		"\u0152Z\3\2\2\2\u0153\u0154\5-\27\2\u0154\u0155\5\3\2\2\u0155\u0156\5"+
		"%\23\2\u0156\\\3\2\2\2\u0157\u0158\5)\25\2\u0158\u0159\5%\23\2\u0159\u015a"+
		"\5+\26\2\u015a\u015b\5\13\6\2\u015b^\3\2\2\2\u015c\u015d\5\r\7\2\u015d"+
		"\u015e\5\3\2\2\u015e\u015f\5\31\r\2\u015f\u0160\5\'\24\2\u0160\u0161\5"+
		"\13\6\2\u0161`\3\2\2\2\u0162\u0163\5\3\2\2\u0163\u0164\5%\23\2\u0164\u0165"+
		"\5%\23\2\u0165\u0166\5\3\2\2\u0166\u0167\5\63\32\2\u0167b\3\2\2\2\u0168"+
		"\u0169\5\37\20\2\u0169\u016a\5\r\7\2\u016ad\3\2\2\2\u016b\u016c\5/\30"+
		"\2\u016c\u016d\5\23\n\2\u016d\u016e\5)\25\2\u016e\u016f\5\21\t\2\u016f"+
		"f\3\2\2\2\u0170\u0171\7-\2\2\u0171h\3\2\2\2\u0172\u0173\7/\2\2\u0173j"+
		"\3\2\2\2\u0174\u0175\7,\2\2\u0175l\3\2\2\2\u0176\u0177\7\61\2\2\u0177"+
		"n\3\2\2\2\u0178\u0179\5\35\17\2\u0179\u017a\5\37\20\2\u017a\u017b\5)\25"+
		"\2\u017bp\3\2\2\2\u017c\u017d\5\33\16\2\u017d\u017e\5\37\20\2\u017e\u017f"+
		"\5\t\5\2\u017fr\3\2\2\2\u0180\u0181\5\37\20\2\u0181\u0182\5%\23\2\u0182"+
		"t\3\2\2\2\u0183\u0184\5\3\2\2\u0184\u0185\5\35\17\2\u0185\u0186\5\t\5"+
		"\2\u0186v\3\2\2\2\u0187\u0188\5s:\2\u0188\u0189\5M\'\2\u0189x\3\2\2\2"+
		"\u018a\u018b\5u;\2\u018b\u018c\5K&\2\u018cz\3\2\2\2\u018d\u018e\7>\2\2"+
		"\u018e\u018f\7@\2\2\u018f|\3\2\2\2\u0190\u0191\7?\2\2\u0191~\3\2\2\2\u0192"+
		"\u0193\7>\2\2\u0193\u0080\3\2\2\2\u0194\u0195\7@\2\2\u0195\u0082\3\2\2"+
		"\2\u0196\u0197\7>\2\2\u0197\u0198\7?\2\2\u0198\u0084\3\2\2\2\u0199\u019a"+
		"\7@\2\2\u019a\u019b\7?\2\2\u019b\u0086\3\2\2\2\u019c\u019d\5\t\5\2\u019d"+
		"\u019e\5\23\n\2\u019e\u019f\5-\27\2\u019f\u0088\3\2\2\2\u01a0\u01a1\7"+
		"<\2\2\u01a1\u01a2\7?\2\2\u01a2\u008a\3\2\2\2\u01a3\u01a4\7]\2\2\u01a4"+
		"\u008c\3\2\2\2\u01a5\u01a6\7_\2\2\u01a6\u008e\3\2\2\2\u01a7\u01a8\7*\2"+
		"\2\u01a8\u0090\3\2\2\2\u01a9\u01aa\7+\2\2\u01aa\u0092\3\2\2\2\u01ab\u01ac"+
		"\7<\2\2\u01ac\u0094\3\2\2\2\u01ad\u01ae\7=\2\2\u01ae\u0096\3\2\2\2\u01af"+
		"\u01b0\7\60\2\2\u01b0\u01b1\7\60\2\2\u01b1\u0098\3\2\2\2\u01b2\u01b3\7"+
		".\2\2\u01b3\u009a\3\2\2\2\u01b4\u01b6\59\35\2\u01b5\u01b4\3\2\2\2\u01b6"+
		"\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u009c\3\2"+
		"\2\2\u01b9\u01bb\5\13\6\2\u01ba\u01bc\t\37\2\2\u01bb\u01ba\3\2\2\2\u01bb"+
		"\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bf\59\35\2\u01be\u01bd\3\2"+
		"\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1"+
		"\u009e\3\2\2\2\u01c2\u01c4\59\35\2\u01c3\u01c2\3\2\2\2\u01c4\u01c5\3\2"+
		"\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01ca\3\2\2\2\u01c7"+
		"\u01c9\5\u009dO\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8"+
		"\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u00a0\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd"+
		"\u01cf\59\35\2\u01ce\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2"+
		"\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01d4\t \2\2\u01d3"+
		"\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d7\5\u009f"+
		"P\2\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8"+
		"\u01d9\3\2\2\2\u01d9\u01ea\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dd\59"+
		"\35\2\u01dc\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de"+
		"\u01df\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3\t "+
		"\2\2\u01e2\u01e1\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4"+
		"\u01e6\5\u009fP\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5"+
		"\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01ce\3\2\2\2\u01e9"+
		"\u01de\3\2\2\2\u01ea\u00a2\3\2\2\2\u01eb\u01ee\5]/\2\u01ec\u01ee\5_\60"+
		"\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u00a4\3\2\2\2\u01ef\u01f4"+
		"\7$\2\2\u01f0\u01f3\n!\2\2\u01f1\u01f3\5;\36\2\u01f2\u01f0\3\2\2\2\u01f2"+
		"\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2"+
		"\2\2\u01f5\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\7$\2\2\u01f8"+
		"\u01f9\bS\2\2\u01f9\u00a6\3\2\2\2\u01fa\u01fb\5\5\3\2\u01fb\u01fc\5\37"+
		"\20\2\u01fc\u01fd\5\37\20\2\u01fd\u01fe\5\31\r\2\u01fe\u01ff\5\13\6\2"+
		"\u01ff\u0200\5\3\2\2\u0200\u0201\5\35\17\2\u0201\u00a8\3\2\2\2\u0202\u0203"+
		"\5\23\n\2\u0203\u0204\5\35\17\2\u0204\u0205\5)\25\2\u0205\u0206\5\13\6"+
		"\2\u0206\u0207\5\17\b\2\u0207\u0208\5\13\6\2\u0208\u0209\5%\23\2\u0209"+
		"\u00aa\3\2\2\2\u020a\u020b\5%\23\2\u020b\u020c\5\13\6\2\u020c\u020d\5"+
		"\3\2\2\u020d\u020e\5\31\r\2\u020e\u00ac\3\2\2\2\u020f\u0210\5\'\24\2\u0210"+
		"\u0211\5)\25\2\u0211\u0212\5%\23\2\u0212\u0213\5\23\n\2\u0213\u0214\5"+
		"\35\17\2\u0214\u0215\5\17\b\2\u0215\u00ae\3\2\2\2\u0216\u0217\7*\2\2\u0217"+
		"\u0218\7,\2\2\u0218\u021c\3\2\2\2\u0219\u021b\13\2\2\2\u021a\u0219\3\2"+
		"\2\2\u021b\u021e\3\2\2\2\u021c\u021d\3\2\2\2\u021c\u021a\3\2\2\2\u021d"+
		"\u021f\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0220\7,\2\2\u0220\u0221\7+\2"+
		"\2\u0221\u0222\3\2\2\2\u0222\u0223\bX\3\2\u0223\u00b0\3\2\2\2\u0224\u0228"+
		"\7}\2\2\u0225\u0227\13\2\2\2\u0226\u0225\3\2\2\2\u0227\u022a\3\2\2\2\u0228"+
		"\u0229\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022b\3\2\2\2\u022a\u0228\3\2"+
		"\2\2\u022b\u022c\7\177\2\2\u022c\u022d\3\2\2\2\u022d\u022e\bY\3\2\u022e"+
		"\u00b2\3\2\2\2\u022f\u0230\7\61\2\2\u0230\u0231\7\61\2\2\u0231\u0235\3"+
		"\2\2\2\u0232\u0234\n\"\2\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235"+
		"\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2\u0237\u0235\3\2"+
		"\2\2\u0238\u0239\bZ\3\2\u0239\u00b4\3\2\2\2\u023a\u023c\t#\2\2\u023b\u023a"+
		"\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e"+
		"\u023f\3\2\2\2\u023f\u0240\b[\3\2\u0240\u00b6\3\2\2\2\u0241\u0244\5\67"+
		"\34\2\u0242\u0244\7a\2\2\u0243\u0241\3\2\2\2\u0243\u0242\3\2\2\2\u0244"+
		"\u024a\3\2\2\2\u0245\u0249\5\67\34\2\u0246\u0249\59\35\2\u0247\u0249\7"+
		"a\2\2\u0248\u0245\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0247\3\2\2\2\u0249"+
		"\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u00b8\3\2"+
		"\2\2\u024c\u024a\3\2\2\2\u024d\u0251\7$\2\2\u024e\u0250\n$\2\2\u024f\u024e"+
		"\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252"+
		"\u0254\3\2\2\2\u0253\u0251\3\2\2\2\u0254\u0258\7^\2\2\u0255\u0257\n\36"+
		"\2\2\u0256\u0255\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258"+
		"\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\7$"+
		"\2\2\u025c\u025d\b]\4\2\u025d\u00ba\3\2\2\2\u025e\u0262\7$\2\2\u025f\u0261"+
		"\n%\2\2\u0260\u025f\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262"+
		"\u0263\3\2\2\2\u0263\u0265\3\2\2\2\u0264\u0262\3\2\2\2\u0265\u0266\7\2"+
		"\2\3\u0266\u0267\b^\5\2\u0267\u00bc\3\2\2\2\u0268\u0269\13\2\2\2\u0269"+
		"\u026a\b_\6\2\u026a\u00be\3\2\2\2\u026b\u026c\13\2\2\2\u026c\u026d\b`"+
		"\7\2\u026d\u00c0\3\2\2\2\34\2\u01b7\u01bb\u01c0\u01c5\u01ca\u01d0\u01d3"+
		"\u01d8\u01de\u01e2\u01e7\u01e9\u01ed\u01f2\u01f4\u021c\u0228\u0235\u023d"+
		"\u0243\u0248\u024a\u0251\u0258\u0262\b\3S\2\b\2\2\3]\3\3^\4\3_\5\3`\6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}