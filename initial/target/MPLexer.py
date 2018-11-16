# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexerror import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0289\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\68\u0175\n8\r8\168\u0176")
        buf.write("\38\38\38\38\38\39\39\39\39\69\u0182\n9\r9\169\u0183\3")
        buf.write("9\39\39\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3")
        buf.write("?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3")
        buf.write("F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3K\6K\u01b5\nK\rK\16K\u01b6")
        buf.write("\3L\3L\5L\u01bb\nL\3L\6L\u01be\nL\rL\16L\u01bf\3M\6M\u01c3")
        buf.write("\nM\rM\16M\u01c4\3M\7M\u01c8\nM\fM\16M\u01cb\13M\3N\6")
        buf.write("N\u01ce\nN\rN\16N\u01cf\3N\5N\u01d3\nN\3N\7N\u01d6\nN")
        buf.write("\fN\16N\u01d9\13N\3N\7N\u01dc\nN\fN\16N\u01df\13N\3N\5")
        buf.write("N\u01e2\nN\3N\6N\u01e5\nN\rN\16N\u01e6\5N\u01e9\nN\3O")
        buf.write("\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u01f6\nO\3P\3P\3P\3")
        buf.write("P\7P\u01fc\nP\fP\16P\u01ff\13P\3P\3P\3P\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\3U\3U\3U\3U\7U\u0224\nU\fU\16U\u0227")
        buf.write("\13U\3U\3U\3U\3U\3U\3V\3V\7V\u0230\nV\fV\16V\u0233\13")
        buf.write("V\3V\3V\3V\3V\3W\3W\3W\3W\7W\u023d\nW\fW\16W\u0240\13")
        buf.write("W\3W\3W\3X\3X\5X\u0246\nX\3X\3X\3X\7X\u024b\nX\fX\16X")
        buf.write("\u024e\13X\3Y\6Y\u0251\nY\rY\16Y\u0252\3Y\3Y\3Z\3Z\7Z")
        buf.write("\u0259\nZ\fZ\16Z\u025c\13Z\3Z\3Z\7Z\u0260\nZ\fZ\16Z\u0263")
        buf.write("\13Z\3Z\3Z\3Z\3[\3[\7[\u026a\n[\f[\16[\u026d\13[\3[\3")
        buf.write("[\7[\u0271\n[\f[\16[\u0274\13[\3[\7[\u0277\n[\f[\16[\u027a")
        buf.write("\13[\3[\3[\3\\\3\\\7\\\u0280\n\\\f\\\16\\\u0283\13\\\3")
        buf.write("\\\3\\\3]\3]\3]\4\u0225\u0231\2^\3\2\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#")
        buf.write("\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\3;\4=\5?\6")
        buf.write("A\7C\bE\tG\nI\13K\fM\rO\16Q\17S\20U\21W\22Y\23[\24]\25")
        buf.write("_\26a\27c\30e\31g\32i\33k\34m\35o\36q\37s u!w\"y#{$}%")
        buf.write("\177&\u0081\'\u0083(\u0085)\u0087*\u0089+\u008b,\u008d")
        buf.write("-\u008f.\u0091/\u0093\2\u0095\60\u0097\2\u0099\2\u009b")
        buf.write("\61\u009d\62\u009f\63\u00a1\64\u00a3\65\u00a5\66\u00a7")
        buf.write("\67\u00a98\u00ab9\u00ad:\u00af;\u00b1<\u00b3=\u00b5>\u00b7")
        buf.write("?\u00b9@\3\2(\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg")
        buf.write("\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2N")
        buf.write("Nnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4")
        buf.write("\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{")
        buf.write("{\4\2\\\\||\4\2C\\c|\3\2\62;\3\2//\3\2\60\60\7\2\n\f\16")
        buf.write("\17$$))^^\n\2$$))^^ddhhppttvv\4\2\f\f\17\17\5\2\13\f\16")
        buf.write("\17\"\"\4\2\13\13))\5\2\f\f\17\17$$\b\2$$^^ddhhpptt\3")
        buf.write("\2$$\2\u0289\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0095\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\3\u00bb\3\2\2\2\5\u00bd\3\2\2\2\7\u00bf\3\2\2")
        buf.write("\2\t\u00c1\3\2\2\2\13\u00c3\3\2\2\2\r\u00c5\3\2\2\2\17")
        buf.write("\u00c7\3\2\2\2\21\u00c9\3\2\2\2\23\u00cb\3\2\2\2\25\u00cd")
        buf.write("\3\2\2\2\27\u00cf\3\2\2\2\31\u00d1\3\2\2\2\33\u00d3\3")
        buf.write("\2\2\2\35\u00d5\3\2\2\2\37\u00d7\3\2\2\2!\u00d9\3\2\2")
        buf.write("\2#\u00db\3\2\2\2%\u00dd\3\2\2\2\'\u00df\3\2\2\2)\u00e1")
        buf.write("\3\2\2\2+\u00e3\3\2\2\2-\u00e5\3\2\2\2/\u00e7\3\2\2\2")
        buf.write("\61\u00e9\3\2\2\2\63\u00eb\3\2\2\2\65\u00ed\3\2\2\2\67")
        buf.write("\u00ef\3\2\2\29\u00f1\3\2\2\2;\u00f7\3\2\2\2=\u0100\3")
        buf.write("\2\2\2?\u0104\3\2\2\2A\u0107\3\2\2\2C\u010e\3\2\2\2E\u0111")
        buf.write("\3\2\2\2G\u0114\3\2\2\2I\u0119\3\2\2\2K\u011e\3\2\2\2")
        buf.write("M\u0125\3\2\2\2O\u012b\3\2\2\2Q\u0131\3\2\2\2S\u0135\3")
        buf.write("\2\2\2U\u013e\3\2\2\2W\u0148\3\2\2\2Y\u014c\3\2\2\2[\u0152")
        buf.write("\3\2\2\2]\u0155\3\2\2\2_\u015a\3\2\2\2a\u015c\3\2\2\2")
        buf.write("c\u015e\3\2\2\2e\u0160\3\2\2\2g\u0162\3\2\2\2i\u0166\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u016d\3\2\2\2o\u0171\3\2\2\2q\u017d")
        buf.write("\3\2\2\2s\u018a\3\2\2\2u\u018d\3\2\2\2w\u018f\3\2\2\2")
        buf.write("y\u0191\3\2\2\2{\u0193\3\2\2\2}\u0196\3\2\2\2\177\u0199")
        buf.write("\3\2\2\2\u0081\u019d\3\2\2\2\u0083\u01a0\3\2\2\2\u0085")
        buf.write("\u01a2\3\2\2\2\u0087\u01a4\3\2\2\2\u0089\u01a6\3\2\2\2")
        buf.write("\u008b\u01a8\3\2\2\2\u008d\u01aa\3\2\2\2\u008f\u01ac\3")
        buf.write("\2\2\2\u0091\u01af\3\2\2\2\u0093\u01b1\3\2\2\2\u0095\u01b4")
        buf.write("\3\2\2\2\u0097\u01b8\3\2\2\2\u0099\u01c2\3\2\2\2\u009b")
        buf.write("\u01e8\3\2\2\2\u009d\u01f5\3\2\2\2\u009f\u01f7\3\2\2\2")
        buf.write("\u00a1\u0203\3\2\2\2\u00a3\u020b\3\2\2\2\u00a5\u0213\3")
        buf.write("\2\2\2\u00a7\u0218\3\2\2\2\u00a9\u021f\3\2\2\2\u00ab\u022d")
        buf.write("\3\2\2\2\u00ad\u0238\3\2\2\2\u00af\u0245\3\2\2\2\u00b1")
        buf.write("\u0250\3\2\2\2\u00b3\u0256\3\2\2\2\u00b5\u0267\3\2\2\2")
        buf.write("\u00b7\u027d\3\2\2\2\u00b9\u0286\3\2\2\2\u00bb\u00bc\t")
        buf.write("\2\2\2\u00bc\4\3\2\2\2\u00bd\u00be\t\3\2\2\u00be\6\3\2")
        buf.write("\2\2\u00bf\u00c0\t\4\2\2\u00c0\b\3\2\2\2\u00c1\u00c2\t")
        buf.write("\5\2\2\u00c2\n\3\2\2\2\u00c3\u00c4\t\6\2\2\u00c4\f\3\2")
        buf.write("\2\2\u00c5\u00c6\t\7\2\2\u00c6\16\3\2\2\2\u00c7\u00c8")
        buf.write("\t\b\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\t\t\2\2\u00ca\22")
        buf.write("\3\2\2\2\u00cb\u00cc\t\n\2\2\u00cc\24\3\2\2\2\u00cd\u00ce")
        buf.write("\t\13\2\2\u00ce\26\3\2\2\2\u00cf\u00d0\t\f\2\2\u00d0\30")
        buf.write("\3\2\2\2\u00d1\u00d2\t\r\2\2\u00d2\32\3\2\2\2\u00d3\u00d4")
        buf.write("\t\16\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\t\17\2\2\u00d6")
        buf.write("\36\3\2\2\2\u00d7\u00d8\t\20\2\2\u00d8 \3\2\2\2\u00d9")
        buf.write("\u00da\t\21\2\2\u00da\"\3\2\2\2\u00db\u00dc\t\22\2\2\u00dc")
        buf.write("$\3\2\2\2\u00dd\u00de\t\23\2\2\u00de&\3\2\2\2\u00df\u00e0")
        buf.write("\t\24\2\2\u00e0(\3\2\2\2\u00e1\u00e2\t\25\2\2\u00e2*\3")
        buf.write("\2\2\2\u00e3\u00e4\t\26\2\2\u00e4,\3\2\2\2\u00e5\u00e6")
        buf.write("\t\27\2\2\u00e6.\3\2\2\2\u00e7\u00e8\t\30\2\2\u00e8\60")
        buf.write("\3\2\2\2\u00e9\u00ea\t\31\2\2\u00ea\62\3\2\2\2\u00eb\u00ec")
        buf.write("\t\32\2\2\u00ec\64\3\2\2\2\u00ed\u00ee\t\33\2\2\u00ee")
        buf.write("\66\3\2\2\2\u00ef\u00f0\t\34\2\2\u00f08\3\2\2\2\u00f1")
        buf.write("\u00f2\5\5\3\2\u00f2\u00f3\5%\23\2\u00f3\u00f4\5\13\6")
        buf.write("\2\u00f4\u00f5\5\3\2\2\u00f5\u00f6\5\27\f\2\u00f6:\3\2")
        buf.write("\2\2\u00f7\u00f8\5\7\4\2\u00f8\u00f9\5\37\20\2\u00f9\u00fa")
        buf.write("\5\35\17\2\u00fa\u00fb\5)\25\2\u00fb\u00fc\5\23\n\2\u00fc")
        buf.write("\u00fd\5\35\17\2\u00fd\u00fe\5+\26\2\u00fe\u00ff\5\13")
        buf.write("\6\2\u00ff<\3\2\2\2\u0100\u0101\5\r\7\2\u0101\u0102\5")
        buf.write("\37\20\2\u0102\u0103\5%\23\2\u0103>\3\2\2\2\u0104\u0105")
        buf.write("\5)\25\2\u0105\u0106\5\37\20\2\u0106@\3\2\2\2\u0107\u0108")
        buf.write("\5\t\5\2\u0108\u0109\5\37\20\2\u0109\u010a\5/\30\2\u010a")
        buf.write("\u010b\5\35\17\2\u010b\u010c\5)\25\2\u010c\u010d\5\37")
        buf.write("\20\2\u010dB\3\2\2\2\u010e\u010f\5\t\5\2\u010f\u0110\5")
        buf.write("\37\20\2\u0110D\3\2\2\2\u0111\u0112\5\23\n\2\u0112\u0113")
        buf.write("\5\r\7\2\u0113F\3\2\2\2\u0114\u0115\5)\25\2\u0115\u0116")
        buf.write("\5\21\t\2\u0116\u0117\5\13\6\2\u0117\u0118\5\35\17\2\u0118")
        buf.write("H\3\2\2\2\u0119\u011a\5\13\6\2\u011a\u011b\5\31\r\2\u011b")
        buf.write("\u011c\5\'\24\2\u011c\u011d\5\13\6\2\u011dJ\3\2\2\2\u011e")
        buf.write("\u011f\5%\23\2\u011f\u0120\5\13\6\2\u0120\u0121\5)\25")
        buf.write("\2\u0121\u0122\5+\26\2\u0122\u0123\5%\23\2\u0123\u0124")
        buf.write("\5\35\17\2\u0124L\3\2\2\2\u0125\u0126\5/\30\2\u0126\u0127")
        buf.write("\5\21\t\2\u0127\u0128\5\23\n\2\u0128\u0129\5\31\r\2\u0129")
        buf.write("\u012a\5\13\6\2\u012aN\3\2\2\2\u012b\u012c\5\5\3\2\u012c")
        buf.write("\u012d\5\13\6\2\u012d\u012e\5\17\b\2\u012e\u012f\5\23")
        buf.write("\n\2\u012f\u0130\5\35\17\2\u0130P\3\2\2\2\u0131\u0132")
        buf.write("\5\13\6\2\u0132\u0133\5\35\17\2\u0133\u0134\5\t\5\2\u0134")
        buf.write("R\3\2\2\2\u0135\u0136\5\r\7\2\u0136\u0137\5+\26\2\u0137")
        buf.write("\u0138\5\35\17\2\u0138\u0139\5\7\4\2\u0139\u013a\5)\25")
        buf.write("\2\u013a\u013b\5\23\n\2\u013b\u013c\5\37\20\2\u013c\u013d")
        buf.write("\5\35\17\2\u013dT\3\2\2\2\u013e\u013f\5!\21\2\u013f\u0140")
        buf.write("\5%\23\2\u0140\u0141\5\37\20\2\u0141\u0142\5\7\4\2\u0142")
        buf.write("\u0143\5\13\6\2\u0143\u0144\5\t\5\2\u0144\u0145\5+\26")
        buf.write("\2\u0145\u0146\5%\23\2\u0146\u0147\5\13\6\2\u0147V\3\2")
        buf.write("\2\2\u0148\u0149\5-\27\2\u0149\u014a\5\3\2\2\u014a\u014b")
        buf.write("\5%\23\2\u014bX\3\2\2\2\u014c\u014d\5\3\2\2\u014d\u014e")
        buf.write("\5%\23\2\u014e\u014f\5%\23\2\u014f\u0150\5\3\2\2\u0150")
        buf.write("\u0151\5\63\32\2\u0151Z\3\2\2\2\u0152\u0153\5\37\20\2")
        buf.write("\u0153\u0154\5\r\7\2\u0154\\\3\2\2\2\u0155\u0156\5/\30")
        buf.write("\2\u0156\u0157\5\23\n\2\u0157\u0158\5)\25\2\u0158\u0159")
        buf.write("\5\21\t\2\u0159^\3\2\2\2\u015a\u015b\7-\2\2\u015b`\3\2")
        buf.write("\2\2\u015c\u015d\7/\2\2\u015db\3\2\2\2\u015e\u015f\7,")
        buf.write("\2\2\u015fd\3\2\2\2\u0160\u0161\7\61\2\2\u0161f\3\2\2")
        buf.write("\2\u0162\u0163\5\35\17\2\u0163\u0164\5\37\20\2\u0164\u0165")
        buf.write("\5)\25\2\u0165h\3\2\2\2\u0166\u0167\5\33\16\2\u0167\u0168")
        buf.write("\5\37\20\2\u0168\u0169\5\t\5\2\u0169j\3\2\2\2\u016a\u016b")
        buf.write("\5\37\20\2\u016b\u016c\5%\23\2\u016cl\3\2\2\2\u016d\u016e")
        buf.write("\5\3\2\2\u016e\u016f\5\35\17\2\u016f\u0170\5\t\5\2\u0170")
        buf.write("n\3\2\2\2\u0171\u0172\5\37\20\2\u0172\u0174\5%\23\2\u0173")
        buf.write("\u0175\7\"\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3")
        buf.write("\2\2\2\u0178\u0179\5\13\6\2\u0179\u017a\5\31\r\2\u017a")
        buf.write("\u017b\5\'\24\2\u017b\u017c\5\13\6\2\u017cp\3\2\2\2\u017d")
        buf.write("\u017e\5\3\2\2\u017e\u017f\5\35\17\2\u017f\u0181\5\t\5")
        buf.write("\2\u0180\u0182\7\"\2\2\u0181\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0186\5)\25\2\u0186\u0187\5\21\t")
        buf.write("\2\u0187\u0188\5\13\6\2\u0188\u0189\5\35\17\2\u0189r\3")
        buf.write("\2\2\2\u018a\u018b\7>\2\2\u018b\u018c\7@\2\2\u018ct\3")
        buf.write("\2\2\2\u018d\u018e\7?\2\2\u018ev\3\2\2\2\u018f\u0190\7")
        buf.write(">\2\2\u0190x\3\2\2\2\u0191\u0192\7@\2\2\u0192z\3\2\2\2")
        buf.write("\u0193\u0194\7>\2\2\u0194\u0195\7?\2\2\u0195|\3\2\2\2")
        buf.write("\u0196\u0197\7@\2\2\u0197\u0198\7?\2\2\u0198~\3\2\2\2")
        buf.write("\u0199\u019a\5\t\5\2\u019a\u019b\5\23\n\2\u019b\u019c")
        buf.write("\5-\27\2\u019c\u0080\3\2\2\2\u019d\u019e\7<\2\2\u019e")
        buf.write("\u019f\7?\2\2\u019f\u0082\3\2\2\2\u01a0\u01a1\7]\2\2\u01a1")
        buf.write("\u0084\3\2\2\2\u01a2\u01a3\7_\2\2\u01a3\u0086\3\2\2\2")
        buf.write("\u01a4\u01a5\7*\2\2\u01a5\u0088\3\2\2\2\u01a6\u01a7\7")
        buf.write("+\2\2\u01a7\u008a\3\2\2\2\u01a8\u01a9\7<\2\2\u01a9\u008c")
        buf.write("\3\2\2\2\u01aa\u01ab\7=\2\2\u01ab\u008e\3\2\2\2\u01ac")
        buf.write("\u01ad\7\60\2\2\u01ad\u01ae\7\60\2\2\u01ae\u0090\3\2\2")
        buf.write("\2\u01af\u01b0\7.\2\2\u01b0\u0092\3\2\2\2\u01b1\u01b2")
        buf.write("\t\35\2\2\u01b2\u0094\3\2\2\2\u01b3\u01b5\5\u0093J\2\u01b4")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u0096\3\2\2\2\u01b8\u01ba\5")
        buf.write("\13\6\2\u01b9\u01bb\t\36\2\2\u01ba\u01b9\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01be\5\u0093")
        buf.write("J\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u0098\3\2\2\2\u01c1")
        buf.write("\u01c3\5\u0093J\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2")
        buf.write("\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c9")
        buf.write("\3\2\2\2\u01c6\u01c8\5\u0097L\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write("\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2")
        buf.write("\u01ca\u009a\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01ce\5")
        buf.write("\u0093J\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2")
        buf.write("\u01d1\u01d3\t\37\2\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d7\3\2\2\2\u01d4\u01d6\5\u0099M\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01e9\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01dc\5\u0093J\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e2\t")
        buf.write("\37\2\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("\u01e4\3\2\2\2\u01e3\u01e5\5\u0099M\2\u01e4\u01e3\3\2")
        buf.write("\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01cd\3\2\2\2\u01e8")
        buf.write("\u01dd\3\2\2\2\u01e9\u009c\3\2\2\2\u01ea\u01eb\5)\25\2")
        buf.write("\u01eb\u01ec\5%\23\2\u01ec\u01ed\5+\26\2\u01ed\u01ee\5")
        buf.write("\13\6\2\u01ee\u01f6\3\2\2\2\u01ef\u01f0\5\r\7\2\u01f0")
        buf.write("\u01f1\5\3\2\2\u01f1\u01f2\5\31\r\2\u01f2\u01f3\5\'\24")
        buf.write("\2\u01f3\u01f4\5\13\6\2\u01f4\u01f6\3\2\2\2\u01f5\u01ea")
        buf.write("\3\2\2\2\u01f5\u01ef\3\2\2\2\u01f6\u009e\3\2\2\2\u01f7")
        buf.write("\u01fd\7$\2\2\u01f8\u01fc\n \2\2\u01f9\u01fa\7^\2\2\u01fa")
        buf.write("\u01fc\t!\2\2\u01fb\u01f8\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3")
        buf.write("\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201")
        buf.write("\7$\2\2\u0201\u0202\bP\2\2\u0202\u00a0\3\2\2\2\u0203\u0204")
        buf.write("\5\5\3\2\u0204\u0205\5\37\20\2\u0205\u0206\5\37\20\2\u0206")
        buf.write("\u0207\5\31\r\2\u0207\u0208\5\13\6\2\u0208\u0209\5\3\2")
        buf.write("\2\u0209\u020a\5\35\17\2\u020a\u00a2\3\2\2\2\u020b\u020c")
        buf.write("\5\23\n\2\u020c\u020d\5\35\17\2\u020d\u020e\5)\25\2\u020e")
        buf.write("\u020f\5\13\6\2\u020f\u0210\5\17\b\2\u0210\u0211\5\13")
        buf.write("\6\2\u0211\u0212\5%\23\2\u0212\u00a4\3\2\2\2\u0213\u0214")
        buf.write("\5%\23\2\u0214\u0215\5\13\6\2\u0215\u0216\5\3\2\2\u0216")
        buf.write("\u0217\5\31\r\2\u0217\u00a6\3\2\2\2\u0218\u0219\5\'\24")
        buf.write("\2\u0219\u021a\5)\25\2\u021a\u021b\5%\23\2\u021b\u021c")
        buf.write("\5\23\n\2\u021c\u021d\5\35\17\2\u021d\u021e\5\17\b\2\u021e")
        buf.write("\u00a8\3\2\2\2\u021f\u0220\7*\2\2\u0220\u0221\7,\2\2\u0221")
        buf.write("\u0225\3\2\2\2\u0222\u0224\13\2\2\2\u0223\u0222\3\2\2")
        buf.write("\2\u0224\u0227\3\2\2\2\u0225\u0226\3\2\2\2\u0225\u0223")
        buf.write("\3\2\2\2\u0226\u0228\3\2\2\2\u0227\u0225\3\2\2\2\u0228")
        buf.write("\u0229\7,\2\2\u0229\u022a\7+\2\2\u022a\u022b\3\2\2\2\u022b")
        buf.write("\u022c\bU\3\2\u022c\u00aa\3\2\2\2\u022d\u0231\7}\2\2\u022e")
        buf.write("\u0230\13\2\2\2\u022f\u022e\3\2\2\2\u0230\u0233\3\2\2")
        buf.write("\2\u0231\u0232\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0234")
        buf.write("\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0235\7\177\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0237\bV\3\2\u0237\u00ac\3\2\2\2")
        buf.write("\u0238\u0239\7\61\2\2\u0239\u023a\7\61\2\2\u023a\u023e")
        buf.write("\3\2\2\2\u023b\u023d\n\"\2\2\u023c\u023b\3\2\2\2\u023d")
        buf.write("\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0241\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\b")
        buf.write("W\3\2\u0242\u00ae\3\2\2\2\u0243\u0246\5\67\34\2\u0244")
        buf.write("\u0246\7a\2\2\u0245\u0243\3\2\2\2\u0245\u0244\3\2\2\2")
        buf.write("\u0246\u024c\3\2\2\2\u0247\u024b\5\67\34\2\u0248\u024b")
        buf.write("\5\u0093J\2\u0249\u024b\7a\2\2\u024a\u0247\3\2\2\2\u024a")
        buf.write("\u0248\3\2\2\2\u024a\u0249\3\2\2\2\u024b\u024e\3\2\2\2")
        buf.write("\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u00b0\3")
        buf.write("\2\2\2\u024e\u024c\3\2\2\2\u024f\u0251\t#\2\2\u0250\u024f")
        buf.write("\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0250\3\2\2\2\u0252")
        buf.write("\u0253\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0255\bY\3\2")
        buf.write("\u0255\u00b2\3\2\2\2\u0256\u025a\7$\2\2\u0257\u0259\n")
        buf.write("$\2\2\u0258\u0257\3\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025d\3\2\2\2\u025c")
        buf.write("\u025a\3\2\2\2\u025d\u0261\t$\2\2\u025e\u0260\n$\2\2\u025f")
        buf.write("\u025e\3\2\2\2\u0260\u0263\3\2\2\2\u0261\u025f\3\2\2\2")
        buf.write("\u0261\u0262\3\2\2\2\u0262\u0264\3\2\2\2\u0263\u0261\3")
        buf.write("\2\2\2\u0264\u0265\7$\2\2\u0265\u0266\bZ\4\2\u0266\u00b4")
        buf.write("\3\2\2\2\u0267\u026b\7$\2\2\u0268\u026a\n%\2\2\u0269\u0268")
        buf.write("\3\2\2\2\u026a\u026d\3\2\2\2\u026b\u0269\3\2\2\2\u026b")
        buf.write("\u026c\3\2\2\2\u026c\u026e\3\2\2\2\u026d\u026b\3\2\2\2")
        buf.write("\u026e\u0272\7^\2\2\u026f\u0271\n&\2\2\u0270\u026f\3\2")
        buf.write("\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0273")
        buf.write("\3\2\2\2\u0273\u0278\3\2\2\2\u0274\u0272\3\2\2\2\u0275")
        buf.write("\u0277\n\'\2\2\u0276\u0275\3\2\2\2\u0277\u027a\3\2\2\2")
        buf.write("\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027b\3")
        buf.write("\2\2\2\u027a\u0278\3\2\2\2\u027b\u027c\b[\5\2\u027c\u00b6")
        buf.write("\3\2\2\2\u027d\u0281\7$\2\2\u027e\u0280\n\'\2\2\u027f")
        buf.write("\u027e\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2")
        buf.write("\u0281\u0282\3\2\2\2\u0282\u0284\3\2\2\2\u0283\u0281\3")
        buf.write("\2\2\2\u0284\u0285\b\\\6\2\u0285\u00b8\3\2\2\2\u0286\u0287")
        buf.write("\13\2\2\2\u0287\u0288\b]\7\2\u0288\u00ba\3\2\2\2!\2\u0176")
        buf.write("\u0183\u01b6\u01ba\u01bf\u01c4\u01c9\u01cf\u01d2\u01d7")
        buf.write("\u01dd\u01e1\u01e6\u01e8\u01f5\u01fb\u01fd\u0225\u0231")
        buf.write("\u023e\u0245\u024a\u024c\u0252\u025a\u0261\u026b\u0272")
        buf.write("\u0278\u0281\b\3P\2\b\2\2\3Z\3\3[\4\3\\\5\3]\6")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK_KW = 1
    CONTINUE_KW = 2
    FOR_KW = 3
    TO_KW = 4
    DOWNTO_KW = 5
    DO_KW = 6
    IF_KW = 7
    THEN_KW = 8
    ELSE_KW = 9
    RETURN_KW = 10
    WHILE_KW = 11
    BEGIN_KW = 12
    END_KW = 13
    FUNCTION_KW = 14
    PROCEDURE_KW = 15
    VAR_KW = 16
    ARRAY_KW = 17
    OF_KW = 18
    WITH_KW = 19
    ADD_KW = 20
    SUB_KW = 21
    MUL_KW = 22
    DIVR_KW = 23
    NOT_KW = 24
    MOD_KW = 25
    OR_KW = 26
    AND_KW = 27
    ORELSE_KW = 28
    ANDTHEN_KW = 29
    NOTEQUAL_KW = 30
    EQUAL_KW = 31
    LESSTHAN_KW = 32
    GREATERTHAN_KW = 33
    LESSOREQUAL_KW = 34
    GREATEROREQUAL_KW = 35
    DIV_KW = 36
    ASSIGN_KW = 37
    LSB = 38
    RSB = 39
    LB = 40
    RB = 41
    COLON = 42
    SEMICOLON = 43
    DDOT = 44
    COMMA = 45
    INTLIT = 46
    FLOATLIT = 47
    BOOLEANLIT = 48
    STRINGLIT = 49
    BOOLEAN_KW = 50
    INTEGER_KW = 51
    REAL_KW = 52
    STRING_KW = 53
    T_COMMENT = 54
    B_COMMENT = 55
    L_COMMENT = 56
    ID = 57
    WS = 58
    ILLEGAL_CHAR = 59
    ILLEGAL_ESCAPE = 60
    UNCLOSE_STRING = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "':='", "'['", "']'", "'('", "')'", "':'", "';'", "'..'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "BREAK_KW", "CONTINUE_KW", "FOR_KW", "TO_KW", "DOWNTO_KW", "DO_KW", 
            "IF_KW", "THEN_KW", "ELSE_KW", "RETURN_KW", "WHILE_KW", "BEGIN_KW", 
            "END_KW", "FUNCTION_KW", "PROCEDURE_KW", "VAR_KW", "ARRAY_KW", 
            "OF_KW", "WITH_KW", "ADD_KW", "SUB_KW", "MUL_KW", "DIVR_KW", 
            "NOT_KW", "MOD_KW", "OR_KW", "AND_KW", "ORELSE_KW", "ANDTHEN_KW", 
            "NOTEQUAL_KW", "EQUAL_KW", "LESSTHAN_KW", "GREATERTHAN_KW", 
            "LESSOREQUAL_KW", "GREATEROREQUAL_KW", "DIV_KW", "ASSIGN_KW", 
            "LSB", "RSB", "LB", "RB", "COLON", "SEMICOLON", "DDOT", "COMMA", 
            "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEAN_KW", 
            "INTEGER_KW", "REAL_KW", "STRING_KW", "T_COMMENT", "B_COMMENT", 
            "L_COMMENT", "ID", "WS", "ILLEGAL_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "LETTERS", "BREAK_KW", "CONTINUE_KW", 
                  "FOR_KW", "TO_KW", "DOWNTO_KW", "DO_KW", "IF_KW", "THEN_KW", 
                  "ELSE_KW", "RETURN_KW", "WHILE_KW", "BEGIN_KW", "END_KW", 
                  "FUNCTION_KW", "PROCEDURE_KW", "VAR_KW", "ARRAY_KW", "OF_KW", 
                  "WITH_KW", "ADD_KW", "SUB_KW", "MUL_KW", "DIVR_KW", "NOT_KW", 
                  "MOD_KW", "OR_KW", "AND_KW", "ORELSE_KW", "ANDTHEN_KW", 
                  "NOTEQUAL_KW", "EQUAL_KW", "LESSTHAN_KW", "GREATERTHAN_KW", 
                  "LESSOREQUAL_KW", "GREATEROREQUAL_KW", "DIV_KW", "ASSIGN_KW", 
                  "LSB", "RSB", "LB", "RB", "COLON", "SEMICOLON", "DDOT", 
                  "COMMA", "NUMBER", "INTLIT", "EXPONENT", "FRACTION", "FLOATLIT", 
                  "BOOLEANLIT", "STRINGLIT", "BOOLEAN_KW", "INTEGER_KW", 
                  "REAL_KW", "STRING_KW", "T_COMMENT", "B_COMMENT", "L_COMMENT", 
                  "ID", "WS", "ILLEGAL_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[78] = self.STRINGLIT_action 
            actions[88] = self.ILLEGAL_CHAR_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.UNCLOSE_STRING_action 
            actions[91] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:-1]
     

    def ILLEGAL_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            pos = tab = self.text.find('\t')
            sq = self.text.find('\'')
            if tab == -1:
                pos = sq
            raise IllegalCharInString(self.text[1: pos+1])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            slash = self.text.find('\\')
            raise IllegalEscapeInString(self.text[1: slash +2])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UnclosedString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


