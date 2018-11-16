# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u012b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\6\2")
        buf.write("<\n\2\r\2\16\2=\3\2\3\2\3\3\3\3\3\3\5\3E\n\3\3\4\3\4\3")
        buf.write("\4\3\4\6\4K\n\4\r\4\16\4L\3\5\3\5\3\6\3\6\3\6\7\6T\n\6")
        buf.write("\f\6\16\6W\13\6\3\6\3\6\3\6\3\7\3\7\5\7^\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\7\nn\n")
        buf.write("\n\f\n\16\nq\13\n\3\13\3\13\3\13\3\13\5\13w\n\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\7\13~\n\13\f\13\16\13\u0081\13\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u0089\n\f\3\f\3\f\3\f\7")
        buf.write("\f\u008e\n\f\f\f\16\f\u0091\13\f\3\f\3\f\3\r\3\r\7\r\u0097")
        buf.write("\n\r\f\r\16\r\u009a\13\r\3\r\3\r\3\16\3\16\5\16\u00a0")
        buf.write("\n\16\3\17\3\17\5\17\u00a4\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00ab\n\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u00c4\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00cc\n\23\3\24\3\24\3\24\6\24")
        buf.write("\u00d1\n\24\r\24\16\24\u00d2\3\24\3\24\3\25\3\25\3\25")
        buf.write("\5\25\u00da\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\6\30\u00f0\n\30\r\30\16\30\u00f1\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\5\32\u00fd\n\32\3")
        buf.write("\33\3\33\3\34\3\34\3\34\7\34\u0104\n\34\f\34\16\34\u0107")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u0113\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u0126\n\35\f\35\16\35\u0129\13\35\3\35\2\38\36\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8\2\n\3\2\64\67\3\2\6\7\3\2\60\63\4\2\27\27\32\32\6\2")
        buf.write("\30\31\33\33\35\35&&\4\2\26\27\34\34\3\2 %\3\2\36\37\2")
        buf.write("\u0134\2;\3\2\2\2\4D\3\2\2\2\6F\3\2\2\2\bN\3\2\2\2\nP")
        buf.write("\3\2\2\2\f]\3\2\2\2\16_\3\2\2\2\20h\3\2\2\2\22j\3\2\2")
        buf.write("\2\24r\3\2\2\2\26\u0084\3\2\2\2\30\u0094\3\2\2\2\32\u009f")
        buf.write("\3\2\2\2\34\u00a3\3\2\2\2\36\u00a5\3\2\2\2 \u00af\3\2")
        buf.write("\2\2\"\u00c3\3\2\2\2$\u00cb\3\2\2\2&\u00d0\3\2\2\2(\u00d6")
        buf.write("\3\2\2\2*\u00dd\3\2\2\2,\u00e6\3\2\2\2.\u00eb\3\2\2\2")
        buf.write("\60\u00f6\3\2\2\2\62\u00fc\3\2\2\2\64\u00fe\3\2\2\2\66")
        buf.write("\u0100\3\2\2\28\u0112\3\2\2\2:<\5\4\3\2;:\3\2\2\2<=\3")
        buf.write("\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7\2\2\3@\3\3\2")
        buf.write("\2\2AE\5\6\4\2BE\5\24\13\2CE\5\26\f\2DA\3\2\2\2DB\3\2")
        buf.write("\2\2DC\3\2\2\2E\5\3\2\2\2FJ\7\22\2\2GH\5\n\6\2HI\7-\2")
        buf.write("\2IK\3\2\2\2JG\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M")
        buf.write("\7\3\2\2\2NO\7;\2\2O\t\3\2\2\2PU\5\b\5\2QR\7/\2\2RT\5")
        buf.write("\b\5\2SQ\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2")
        buf.write("\2WU\3\2\2\2XY\7,\2\2YZ\5\f\7\2Z\13\3\2\2\2[^\5\20\t\2")
        buf.write("\\^\5\16\b\2][\3\2\2\2]\\\3\2\2\2^\r\3\2\2\2_`\7\23\2")
        buf.write("\2`a\7(\2\2ab\58\35\2bc\7.\2\2cd\58\35\2de\7)\2\2ef\7")
        buf.write("\24\2\2fg\5\20\t\2g\17\3\2\2\2hi\t\2\2\2i\21\3\2\2\2j")
        buf.write("o\5\n\6\2kl\7-\2\2ln\5\n\6\2mk\3\2\2\2nq\3\2\2\2om\3\2")
        buf.write("\2\2op\3\2\2\2p\23\3\2\2\2qo\3\2\2\2rs\7\20\2\2st\7;\2")
        buf.write("\2tv\7*\2\2uw\5\22\n\2vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2x")
        buf.write("y\7+\2\2yz\7,\2\2z{\5\f\7\2{\177\7-\2\2|~\5\6\4\2}|\3")
        buf.write("\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\5\30\r\2")
        buf.write("\u0083\25\3\2\2\2\u0084\u0085\7\21\2\2\u0085\u0086\7;")
        buf.write("\2\2\u0086\u0088\7*\2\2\u0087\u0089\5\22\n\2\u0088\u0087")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008b\7+\2\2\u008b\u008f\7-\2\2\u008c\u008e\5\6\4\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0092\u0093\5\30\r\2\u0093\27\3\2\2\2\u0094\u0098")
        buf.write("\7\16\2\2\u0095\u0097\5\32\16\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\7")
        buf.write("\17\2\2\u009c\31\3\2\2\2\u009d\u00a0\5\34\17\2\u009e\u00a0")
        buf.write("\5\"\22\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\33\3\2\2\2\u00a1\u00a4\5\36\20\2\u00a2\u00a4\5 \21\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\35\3\2")
        buf.write("\2\2\u00a5\u00a6\7\t\2\2\u00a6\u00a7\58\35\2\u00a7\u00aa")
        buf.write("\7\n\2\2\u00a8\u00ab\5\36\20\2\u00a9\u00ab\5\"\22\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\7\13\2\2\u00ad\u00ae\5\32\16\2\u00ae\37\3")
        buf.write("\2\2\2\u00af\u00b0\7\t\2\2\u00b0\u00b1\58\35\2\u00b1\u00b2")
        buf.write("\7\n\2\2\u00b2\u00b3\5\32\16\2\u00b3!\3\2\2\2\u00b4\u00b5")
        buf.write("\5&\24\2\u00b5\u00b6\7-\2\2\u00b6\u00c4\3\2\2\2\u00b7")
        buf.write("\u00c4\5.\30\2\u00b8\u00c4\5*\26\2\u00b9\u00c4\5,\27\2")
        buf.write("\u00ba\u00bb\7\3\2\2\u00bb\u00c4\7-\2\2\u00bc\u00bd\7")
        buf.write("\4\2\2\u00bd\u00c4\7-\2\2\u00be\u00bf\5\62\32\2\u00bf")
        buf.write("\u00c0\7-\2\2\u00c0\u00c4\3\2\2\2\u00c1\u00c4\5\60\31")
        buf.write("\2\u00c2\u00c4\5\30\r\2\u00c3\u00b4\3\2\2\2\u00c3\u00b7")
        buf.write("\3\2\2\2\u00c3\u00b8\3\2\2\2\u00c3\u00b9\3\2\2\2\u00c3")
        buf.write("\u00ba\3\2\2\2\u00c3\u00bc\3\2\2\2\u00c3\u00be\3\2\2\2")
        buf.write("\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4#\3\2\2")
        buf.write("\2\u00c5\u00cc\5\b\5\2\u00c6\u00c7\58\35\2\u00c7\u00c8")
        buf.write("\7(\2\2\u00c8\u00c9\58\35\2\u00c9\u00ca\7)\2\2\u00ca\u00cc")
        buf.write("\3\2\2\2\u00cb\u00c5\3\2\2\2\u00cb\u00c6\3\2\2\2\u00cc")
        buf.write("%\3\2\2\2\u00cd\u00ce\5$\23\2\u00ce\u00cf\7\'\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3")
        buf.write("\2\2\2\u00d4\u00d5\58\35\2\u00d5\'\3\2\2\2\u00d6\u00d7")
        buf.write("\7;\2\2\u00d7\u00d9\7*\2\2\u00d8\u00da\5\66\34\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db\u00dc\7+\2\2\u00dc)\3\2\2\2\u00dd\u00de\7\5\2\2")
        buf.write("\u00de\u00df\7;\2\2\u00df\u00e0\7\'\2\2\u00e0\u00e1\5")
        buf.write("8\35\2\u00e1\u00e2\t\3\2\2\u00e2\u00e3\58\35\2\u00e3\u00e4")
        buf.write("\7\b\2\2\u00e4\u00e5\5\32\16\2\u00e5+\3\2\2\2\u00e6\u00e7")
        buf.write("\7\r\2\2\u00e7\u00e8\58\35\2\u00e8\u00e9\7\b\2\2\u00e9")
        buf.write("\u00ea\5\32\16\2\u00ea-\3\2\2\2\u00eb\u00ef\7\25\2\2\u00ec")
        buf.write("\u00ed\5\n\6\2\u00ed\u00ee\7-\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00ec\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00ef\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4")
        buf.write("\7\b\2\2\u00f4\u00f5\5\32\16\2\u00f5/\3\2\2\2\u00f6\u00f7")
        buf.write("\5(\25\2\u00f7\u00f8\7-\2\2\u00f8\61\3\2\2\2\u00f9\u00fd")
        buf.write("\7\f\2\2\u00fa\u00fb\7\f\2\2\u00fb\u00fd\58\35\2\u00fc")
        buf.write("\u00f9\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\63\3\2\2\2\u00fe")
        buf.write("\u00ff\t\4\2\2\u00ff\65\3\2\2\2\u0100\u0105\58\35\2\u0101")
        buf.write("\u0102\7/\2\2\u0102\u0104\58\35\2\u0103\u0101\3\2\2\2")
        buf.write("\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106\67\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109")
        buf.write("\b\35\1\2\u0109\u010a\7*\2\2\u010a\u010b\58\35\2\u010b")
        buf.write("\u010c\7+\2\2\u010c\u0113\3\2\2\2\u010d\u0113\5\64\33")
        buf.write("\2\u010e\u0113\7;\2\2\u010f\u0113\5(\25\2\u0110\u0111")
        buf.write("\t\5\2\2\u0111\u0113\58\35\7\u0112\u0108\3\2\2\2\u0112")
        buf.write("\u010d\3\2\2\2\u0112\u010e\3\2\2\2\u0112\u010f\3\2\2\2")
        buf.write("\u0112\u0110\3\2\2\2\u0113\u0127\3\2\2\2\u0114\u0115\f")
        buf.write("\6\2\2\u0115\u0116\t\6\2\2\u0116\u0126\58\35\7\u0117\u0118")
        buf.write("\f\5\2\2\u0118\u0119\t\7\2\2\u0119\u0126\58\35\6\u011a")
        buf.write("\u011b\f\4\2\2\u011b\u011c\t\b\2\2\u011c\u0126\58\35\5")
        buf.write("\u011d\u011e\f\3\2\2\u011e\u011f\t\t\2\2\u011f\u0126\5")
        buf.write("8\35\4\u0120\u0121\f\b\2\2\u0121\u0122\7(\2\2\u0122\u0123")
        buf.write("\58\35\2\u0123\u0124\7)\2\2\u0124\u0126\3\2\2\2\u0125")
        buf.write("\u0114\3\2\2\2\u0125\u0117\3\2\2\2\u0125\u011a\3\2\2\2")
        buf.write("\u0125\u011d\3\2\2\2\u0125\u0120\3\2\2\2\u0126\u0129\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u01289")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\32=DLU]ov\177\u0088\u008f")
        buf.write("\u0098\u009f\u00a3\u00aa\u00c3\u00cb\u00d2\u00d9\u00f1")
        buf.write("\u00fc\u0105\u0112\u0125\u0127")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<>'", "'='", "'<'", "'>'", "'<='", "'>='", "<INVALID>", 
                     "':='", "'['", "']'", "'('", "')'", "':'", "';'", "'..'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "BREAK_KW", "CONTINUE_KW", "FOR_KW", 
                      "TO_KW", "DOWNTO_KW", "DO_KW", "IF_KW", "THEN_KW", 
                      "ELSE_KW", "RETURN_KW", "WHILE_KW", "BEGIN_KW", "END_KW", 
                      "FUNCTION_KW", "PROCEDURE_KW", "VAR_KW", "ARRAY_KW", 
                      "OF_KW", "WITH_KW", "ADD_KW", "SUB_KW", "MUL_KW", 
                      "DIVR_KW", "NOT_KW", "MOD_KW", "OR_KW", "AND_KW", 
                      "ORELSE_KW", "ANDTHEN_KW", "NOTEQUAL_KW", "EQUAL_KW", 
                      "LESSTHAN_KW", "GREATERTHAN_KW", "LESSOREQUAL_KW", 
                      "GREATEROREQUAL_KW", "DIV_KW", "ASSIGN_KW", "LSB", 
                      "RSB", "LB", "RB", "COLON", "SEMICOLON", "DDOT", "COMMA", 
                      "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEAN_KW", 
                      "INTEGER_KW", "REAL_KW", "STRING_KW", "T_COMMENT", 
                      "B_COMMENT", "L_COMMENT", "ID", "WS", "ILLEGAL_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vDecl = 2
    RULE_varName = 3
    RULE_varList = 4
    RULE_mtype = 5
    RULE_compType = 6
    RULE_primType = 7
    RULE_paramList = 8
    RULE_funcDecl = 9
    RULE_procDecl = 10
    RULE_body = 11
    RULE_stmt = 12
    RULE_ifElseStmt = 13
    RULE_matchStmt = 14
    RULE_unMatchStmt = 15
    RULE_nonIfStmt = 16
    RULE_assignLHS = 17
    RULE_assignStmt = 18
    RULE_invocationExpr = 19
    RULE_forStmt = 20
    RULE_whileStmt = 21
    RULE_withStmt = 22
    RULE_funcall = 23
    RULE_returnStmt = 24
    RULE_dataTypeLit = 25
    RULE_fParams = 26
    RULE_expr = 27

    ruleNames =  [ "program", "decl", "vDecl", "varName", "varList", "mtype", 
                   "compType", "primType", "paramList", "funcDecl", "procDecl", 
                   "body", "stmt", "ifElseStmt", "matchStmt", "unMatchStmt", 
                   "nonIfStmt", "assignLHS", "assignStmt", "invocationExpr", 
                   "forStmt", "whileStmt", "withStmt", "funcall", "returnStmt", 
                   "dataTypeLit", "fParams", "expr" ]

    EOF = Token.EOF
    BREAK_KW=1
    CONTINUE_KW=2
    FOR_KW=3
    TO_KW=4
    DOWNTO_KW=5
    DO_KW=6
    IF_KW=7
    THEN_KW=8
    ELSE_KW=9
    RETURN_KW=10
    WHILE_KW=11
    BEGIN_KW=12
    END_KW=13
    FUNCTION_KW=14
    PROCEDURE_KW=15
    VAR_KW=16
    ARRAY_KW=17
    OF_KW=18
    WITH_KW=19
    ADD_KW=20
    SUB_KW=21
    MUL_KW=22
    DIVR_KW=23
    NOT_KW=24
    MOD_KW=25
    OR_KW=26
    AND_KW=27
    ORELSE_KW=28
    ANDTHEN_KW=29
    NOTEQUAL_KW=30
    EQUAL_KW=31
    LESSTHAN_KW=32
    GREATERTHAN_KW=33
    LESSOREQUAL_KW=34
    GREATEROREQUAL_KW=35
    DIV_KW=36
    ASSIGN_KW=37
    LSB=38
    RSB=39
    LB=40
    RB=41
    COLON=42
    SEMICOLON=43
    DDOT=44
    COMMA=45
    INTLIT=46
    FLOATLIT=47
    BOOLEANLIT=48
    STRINGLIT=49
    BOOLEAN_KW=50
    INTEGER_KW=51
    REAL_KW=52
    STRING_KW=53
    T_COMMENT=54
    B_COMMENT=55
    L_COMMENT=56
    ID=57
    WS=58
    ILLEGAL_CHAR=59
    ILLEGAL_ESCAPE=60
    UNCLOSE_STRING=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.DeclContext)
            else:
                return self.getTypedRuleContext(MPParser.DeclContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.decl()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.FUNCTION_KW) | (1 << MPParser.PROCEDURE_KW) | (1 << MPParser.VAR_KW))) != 0)):
                    break

            self.state = 61
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vDecl(self):
            return self.getTypedRuleContext(MPParser.VDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MPParser.FuncDeclContext,0)


        def procDecl(self):
            return self.getTypedRuleContext(MPParser.ProcDeclContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MPParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.VAR_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.vDecl()
                pass
            elif token in [MPParser.FUNCTION_KW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.funcDecl()
                pass
            elif token in [MPParser.PROCEDURE_KW]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.procDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KW(self):
            return self.getToken(MPParser.VAR_KW, 0)

        def varList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VarListContext)
            else:
                return self.getTypedRuleContext(MPParser.VarListContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SEMICOLON)
            else:
                return self.getToken(MPParser.SEMICOLON, i)

        def getRuleIndex(self):
            return MPParser.RULE_vDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVDecl" ):
                return visitor.visitVDecl(self)
            else:
                return visitor.visitChildren(self)




    def vDecl(self):

        localctx = MPParser.VDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MPParser.VAR_KW)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.varList()
                self.state = 70
                self.match(MPParser.SEMICOLON)
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def getRuleIndex(self):
            return MPParser.RULE_varName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarName" ):
                return visitor.visitVarName(self)
            else:
                return visitor.visitChildren(self)




    def varName(self):

        localctx = MPParser.VarNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VarNameContext)
            else:
                return self.getTypedRuleContext(MPParser.VarNameContext,i)


        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def mtype(self):
            return self.getTypedRuleContext(MPParser.MtypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COMMA)
            else:
                return self.getToken(MPParser.COMMA, i)

        def getRuleIndex(self):
            return MPParser.RULE_varList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarList" ):
                return visitor.visitVarList(self)
            else:
                return visitor.visitChildren(self)




    def varList(self):

        localctx = MPParser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.varName()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.COMMA:
                self.state = 79
                self.match(MPParser.COMMA)
                self.state = 80
                self.varName()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(MPParser.COLON)
            self.state = 87
            self.mtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primType(self):
            return self.getTypedRuleContext(MPParser.PrimTypeContext,0)


        def compType(self):
            return self.getTypedRuleContext(MPParser.CompTypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_mtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMtype" ):
                return visitor.visitMtype(self)
            else:
                return visitor.visitChildren(self)




    def mtype(self):

        localctx = MPParser.MtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.BOOLEAN_KW, MPParser.INTEGER_KW, MPParser.REAL_KW, MPParser.STRING_KW]:
                self.state = 89
                self.primType()
                pass
            elif token in [MPParser.ARRAY_KW]:
                self.state = 90
                self.compType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_KW(self):
            return self.getToken(MPParser.ARRAY_KW, 0)

        def LSB(self):
            return self.getToken(MPParser.LSB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def DDOT(self):
            return self.getToken(MPParser.DDOT, 0)

        def RSB(self):
            return self.getToken(MPParser.RSB, 0)

        def OF_KW(self):
            return self.getToken(MPParser.OF_KW, 0)

        def primType(self):
            return self.getTypedRuleContext(MPParser.PrimTypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_compType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompType" ):
                return visitor.visitCompType(self)
            else:
                return visitor.visitChildren(self)




    def compType(self):

        localctx = MPParser.CompTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(MPParser.ARRAY_KW)
            self.state = 94
            self.match(MPParser.LSB)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.match(MPParser.DDOT)
            self.state = 97
            self.expr(0)
            self.state = 98
            self.match(MPParser.RSB)
            self.state = 99
            self.match(MPParser.OF_KW)
            self.state = 100
            self.primType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_KW(self):
            return self.getToken(MPParser.INTEGER_KW, 0)

        def REAL_KW(self):
            return self.getToken(MPParser.REAL_KW, 0)

        def BOOLEAN_KW(self):
            return self.getToken(MPParser.BOOLEAN_KW, 0)

        def STRING_KW(self):
            return self.getToken(MPParser.STRING_KW, 0)

        def getRuleIndex(self):
            return MPParser.RULE_primType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimType" ):
                return visitor.visitPrimType(self)
            else:
                return visitor.visitChildren(self)




    def primType(self):

        localctx = MPParser.PrimTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.BOOLEAN_KW) | (1 << MPParser.INTEGER_KW) | (1 << MPParser.REAL_KW) | (1 << MPParser.STRING_KW))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VarListContext)
            else:
                return self.getTypedRuleContext(MPParser.VarListContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SEMICOLON)
            else:
                return self.getToken(MPParser.SEMICOLON, i)

        def getRuleIndex(self):
            return MPParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MPParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.varList()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.SEMICOLON:
                self.state = 105
                self.match(MPParser.SEMICOLON)
                self.state = 106
                self.varList()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_KW(self):
            return self.getToken(MPParser.FUNCTION_KW, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def COLON(self):
            return self.getToken(MPParser.COLON, 0)

        def mtype(self):
            return self.getTypedRuleContext(MPParser.MtypeContext,0)


        def SEMICOLON(self):
            return self.getToken(MPParser.SEMICOLON, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MPParser.ParamListContext,0)


        def vDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VDeclContext)
            else:
                return self.getTypedRuleContext(MPParser.VDeclContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MPParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MPParser.FUNCTION_KW)
            self.state = 113
            self.match(MPParser.ID)
            self.state = 114
            self.match(MPParser.LB)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID:
                self.state = 115
                self.paramList()


            self.state = 118
            self.match(MPParser.RB)
            self.state = 119
            self.match(MPParser.COLON)
            self.state = 120
            self.mtype()
            self.state = 121
            self.match(MPParser.SEMICOLON)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.VAR_KW:
                self.state = 122
                self.vDecl()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_KW(self):
            return self.getToken(MPParser.PROCEDURE_KW, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def SEMICOLON(self):
            return self.getToken(MPParser.SEMICOLON, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MPParser.ParamListContext,0)


        def vDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VDeclContext)
            else:
                return self.getTypedRuleContext(MPParser.VDeclContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_procDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcDecl" ):
                return visitor.visitProcDecl(self)
            else:
                return visitor.visitChildren(self)




    def procDecl(self):

        localctx = MPParser.ProcDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_procDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MPParser.PROCEDURE_KW)
            self.state = 131
            self.match(MPParser.ID)
            self.state = 132
            self.match(MPParser.LB)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID:
                self.state = 133
                self.paramList()


            self.state = 136
            self.match(MPParser.RB)
            self.state = 137
            self.match(MPParser.SEMICOLON)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.VAR_KW:
                self.state = 138
                self.vDecl()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_KW(self):
            return self.getToken(MPParser.BEGIN_KW, 0)

        def END_KW(self):
            return self.getToken(MPParser.END_KW, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.StmtContext)
            else:
                return self.getTypedRuleContext(MPParser.StmtContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MPParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MPParser.BEGIN_KW)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.BREAK_KW) | (1 << MPParser.CONTINUE_KW) | (1 << MPParser.FOR_KW) | (1 << MPParser.IF_KW) | (1 << MPParser.RETURN_KW) | (1 << MPParser.WHILE_KW) | (1 << MPParser.BEGIN_KW) | (1 << MPParser.WITH_KW) | (1 << MPParser.SUB_KW) | (1 << MPParser.NOT_KW) | (1 << MPParser.LB) | (1 << MPParser.INTLIT) | (1 << MPParser.FLOATLIT) | (1 << MPParser.BOOLEANLIT) | (1 << MPParser.STRINGLIT) | (1 << MPParser.ID))) != 0):
                self.state = 147
                self.stmt()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(MPParser.END_KW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElseStmt(self):
            return self.getTypedRuleContext(MPParser.IfElseStmtContext,0)


        def nonIfStmt(self):
            return self.getTypedRuleContext(MPParser.NonIfStmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MPParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.IF_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.ifElseStmt()
                pass
            elif token in [MPParser.BREAK_KW, MPParser.CONTINUE_KW, MPParser.FOR_KW, MPParser.RETURN_KW, MPParser.WHILE_KW, MPParser.BEGIN_KW, MPParser.WITH_KW, MPParser.SUB_KW, MPParser.NOT_KW, MPParser.LB, MPParser.INTLIT, MPParser.FLOATLIT, MPParser.BOOLEANLIT, MPParser.STRINGLIT, MPParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.nonIfStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfElseStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matchStmt(self):
            return self.getTypedRuleContext(MPParser.MatchStmtContext,0)


        def unMatchStmt(self):
            return self.getTypedRuleContext(MPParser.UnMatchStmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_ifElseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseStmt" ):
                return visitor.visitIfElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifElseStmt(self):

        localctx = MPParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifElseStmt)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.matchStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.unMatchStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MatchStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KW(self):
            return self.getToken(MPParser.IF_KW, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def THEN_KW(self):
            return self.getToken(MPParser.THEN_KW, 0)

        def ELSE_KW(self):
            return self.getToken(MPParser.ELSE_KW, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def matchStmt(self):
            return self.getTypedRuleContext(MPParser.MatchStmtContext,0)


        def nonIfStmt(self):
            return self.getTypedRuleContext(MPParser.NonIfStmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_matchStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchStmt" ):
                return visitor.visitMatchStmt(self)
            else:
                return visitor.visitChildren(self)




    def matchStmt(self):

        localctx = MPParser.MatchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_matchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MPParser.IF_KW)
            self.state = 164
            self.expr(0)
            self.state = 165
            self.match(MPParser.THEN_KW)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.IF_KW]:
                self.state = 166
                self.matchStmt()
                pass
            elif token in [MPParser.BREAK_KW, MPParser.CONTINUE_KW, MPParser.FOR_KW, MPParser.RETURN_KW, MPParser.WHILE_KW, MPParser.BEGIN_KW, MPParser.WITH_KW, MPParser.SUB_KW, MPParser.NOT_KW, MPParser.LB, MPParser.INTLIT, MPParser.FLOATLIT, MPParser.BOOLEANLIT, MPParser.STRINGLIT, MPParser.ID]:
                self.state = 167
                self.nonIfStmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 170
            self.match(MPParser.ELSE_KW)
            self.state = 171
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnMatchStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KW(self):
            return self.getToken(MPParser.IF_KW, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def THEN_KW(self):
            return self.getToken(MPParser.THEN_KW, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_unMatchStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnMatchStmt" ):
                return visitor.visitUnMatchStmt(self)
            else:
                return visitor.visitChildren(self)




    def unMatchStmt(self):

        localctx = MPParser.UnMatchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_unMatchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MPParser.IF_KW)
            self.state = 174
            self.expr(0)
            self.state = 175
            self.match(MPParser.THEN_KW)
            self.state = 176
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NonIfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(MPParser.AssignStmtContext,0)


        def SEMICOLON(self):
            return self.getToken(MPParser.SEMICOLON, 0)

        def withStmt(self):
            return self.getTypedRuleContext(MPParser.WithStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MPParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MPParser.WhileStmtContext,0)


        def BREAK_KW(self):
            return self.getToken(MPParser.BREAK_KW, 0)

        def CONTINUE_KW(self):
            return self.getToken(MPParser.CONTINUE_KW, 0)

        def returnStmt(self):
            return self.getTypedRuleContext(MPParser.ReturnStmtContext,0)


        def funcall(self):
            return self.getTypedRuleContext(MPParser.FuncallContext,0)


        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_nonIfStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonIfStmt" ):
                return visitor.visitNonIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def nonIfStmt(self):

        localctx = MPParser.NonIfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nonIfStmt)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.assignStmt()
                self.state = 179
                self.match(MPParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.withStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.match(MPParser.BREAK_KW)
                self.state = 185
                self.match(MPParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.match(MPParser.CONTINUE_KW)
                self.state = 187
                self.match(MPParser.SEMICOLON)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 188
                self.returnStmt()
                self.state = 189
                self.match(MPParser.SEMICOLON)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 191
                self.funcall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 192
                self.body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignLHSContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varName(self):
            return self.getTypedRuleContext(MPParser.VarNameContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def LSB(self):
            return self.getToken(MPParser.LSB, 0)

        def RSB(self):
            return self.getToken(MPParser.RSB, 0)

        def getRuleIndex(self):
            return MPParser.RULE_assignLHS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignLHS" ):
                return visitor.visitAssignLHS(self)
            else:
                return visitor.visitChildren(self)




    def assignLHS(self):

        localctx = MPParser.AssignLHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignLHS)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.varName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.expr(0)
                self.state = 197
                self.match(MPParser.LSB)
                self.state = 198
                self.expr(0)
                self.state = 199
                self.match(MPParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def assignLHS(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.AssignLHSContext)
            else:
                return self.getTypedRuleContext(MPParser.AssignLHSContext,i)


        def ASSIGN_KW(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ASSIGN_KW)
            else:
                return self.getToken(MPParser.ASSIGN_KW, i)

        def getRuleIndex(self):
            return MPParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MPParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 203
                    self.assignLHS()
                    self.state = 204
                    self.match(MPParser.ASSIGN_KW)

                else:
                    raise NoViableAltException(self)
                self.state = 208 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 210
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InvocationExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def fParams(self):
            return self.getTypedRuleContext(MPParser.FParamsContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_invocationExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocationExpr" ):
                return visitor.visitInvocationExpr(self)
            else:
                return visitor.visitChildren(self)




    def invocationExpr(self):

        localctx = MPParser.InvocationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_invocationExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MPParser.ID)
            self.state = 213
            self.match(MPParser.LB)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.SUB_KW) | (1 << MPParser.NOT_KW) | (1 << MPParser.LB) | (1 << MPParser.INTLIT) | (1 << MPParser.FLOATLIT) | (1 << MPParser.BOOLEANLIT) | (1 << MPParser.STRINGLIT) | (1 << MPParser.ID))) != 0):
                self.state = 214
                self.fParams()


            self.state = 217
            self.match(MPParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_KW(self):
            return self.getToken(MPParser.FOR_KW, 0)

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def ASSIGN_KW(self):
            return self.getToken(MPParser.ASSIGN_KW, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def DO_KW(self):
            return self.getToken(MPParser.DO_KW, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def TO_KW(self):
            return self.getToken(MPParser.TO_KW, 0)

        def DOWNTO_KW(self):
            return self.getToken(MPParser.DOWNTO_KW, 0)

        def getRuleIndex(self):
            return MPParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MPParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MPParser.FOR_KW)
            self.state = 220
            self.match(MPParser.ID)
            self.state = 221
            self.match(MPParser.ASSIGN_KW)
            self.state = 222
            self.expr(0)
            self.state = 223
            _la = self._input.LA(1)
            if not(_la==MPParser.TO_KW or _la==MPParser.DOWNTO_KW):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 224
            self.expr(0)
            self.state = 225
            self.match(MPParser.DO_KW)
            self.state = 226
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_KW(self):
            return self.getToken(MPParser.WHILE_KW, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def DO_KW(self):
            return self.getToken(MPParser.DO_KW, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MPParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MPParser.WHILE_KW)
            self.state = 229
            self.expr(0)
            self.state = 230
            self.match(MPParser.DO_KW)
            self.state = 231
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH_KW(self):
            return self.getToken(MPParser.WITH_KW, 0)

        def DO_KW(self):
            return self.getToken(MPParser.DO_KW, 0)

        def stmt(self):
            return self.getTypedRuleContext(MPParser.StmtContext,0)


        def varList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VarListContext)
            else:
                return self.getTypedRuleContext(MPParser.VarListContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SEMICOLON)
            else:
                return self.getToken(MPParser.SEMICOLON, i)

        def getRuleIndex(self):
            return MPParser.RULE_withStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithStmt" ):
                return visitor.visitWithStmt(self)
            else:
                return visitor.visitChildren(self)




    def withStmt(self):

        localctx = MPParser.WithStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_withStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MPParser.WITH_KW)
            self.state = 237 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.varList()
                self.state = 235
                self.match(MPParser.SEMICOLON)
                self.state = 239 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.ID):
                    break

            self.state = 241
            self.match(MPParser.DO_KW)
            self.state = 242
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def invocationExpr(self):
            return self.getTypedRuleContext(MPParser.InvocationExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MPParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MPParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MPParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.invocationExpr()
            self.state = 245
            self.match(MPParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KW(self):
            return self.getToken(MPParser.RETURN_KW, 0)

        def expr(self):
            return self.getTypedRuleContext(MPParser.ExprContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MPParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_returnStmt)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(MPParser.RETURN_KW)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(MPParser.RETURN_KW)
                self.state = 249
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataTypeLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MPParser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(MPParser.BOOLEANLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MPParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MPParser.RULE_dataTypeLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataTypeLit" ):
                return visitor.visitDataTypeLit(self)
            else:
                return visitor.visitChildren(self)




    def dataTypeLit(self):

        localctx = MPParser.DataTypeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dataTypeLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.INTLIT) | (1 << MPParser.FLOATLIT) | (1 << MPParser.BOOLEANLIT) | (1 << MPParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COMMA)
            else:
                return self.getToken(MPParser.COMMA, i)

        def getRuleIndex(self):
            return MPParser.RULE_fParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFParams" ):
                return visitor.visitFParams(self)
            else:
                return visitor.visitChildren(self)




    def fParams(self):

        localctx = MPParser.FParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expr(0)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.COMMA:
                self.state = 255
                self.match(MPParser.COMMA)
                self.state = 256
                self.expr(0)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MPParser.ExprContext,i)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def dataTypeLit(self):
            return self.getTypedRuleContext(MPParser.DataTypeLitContext,0)


        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def invocationExpr(self):
            return self.getTypedRuleContext(MPParser.InvocationExprContext,0)


        def SUB_KW(self):
            return self.getToken(MPParser.SUB_KW, 0)

        def NOT_KW(self):
            return self.getToken(MPParser.NOT_KW, 0)

        def MUL_KW(self):
            return self.getToken(MPParser.MUL_KW, 0)

        def DIV_KW(self):
            return self.getToken(MPParser.DIV_KW, 0)

        def DIVR_KW(self):
            return self.getToken(MPParser.DIVR_KW, 0)

        def MOD_KW(self):
            return self.getToken(MPParser.MOD_KW, 0)

        def AND_KW(self):
            return self.getToken(MPParser.AND_KW, 0)

        def ADD_KW(self):
            return self.getToken(MPParser.ADD_KW, 0)

        def OR_KW(self):
            return self.getToken(MPParser.OR_KW, 0)

        def EQUAL_KW(self):
            return self.getToken(MPParser.EQUAL_KW, 0)

        def NOTEQUAL_KW(self):
            return self.getToken(MPParser.NOTEQUAL_KW, 0)

        def LESSTHAN_KW(self):
            return self.getToken(MPParser.LESSTHAN_KW, 0)

        def LESSOREQUAL_KW(self):
            return self.getToken(MPParser.LESSOREQUAL_KW, 0)

        def GREATERTHAN_KW(self):
            return self.getToken(MPParser.GREATERTHAN_KW, 0)

        def GREATEROREQUAL_KW(self):
            return self.getToken(MPParser.GREATEROREQUAL_KW, 0)

        def ANDTHEN_KW(self):
            return self.getToken(MPParser.ANDTHEN_KW, 0)

        def ORELSE_KW(self):
            return self.getToken(MPParser.ORELSE_KW, 0)

        def LSB(self):
            return self.getToken(MPParser.LSB, 0)

        def RSB(self):
            return self.getToken(MPParser.RSB, 0)

        def getRuleIndex(self):
            return MPParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(MPParser.LB)
                self.state = 264
                self.expr(0)
                self.state = 265
                self.match(MPParser.RB)
                pass

            elif la_ == 2:
                self.state = 267
                self.dataTypeLit()
                pass

            elif la_ == 3:
                self.state = 268
                self.match(MPParser.ID)
                pass

            elif la_ == 4:
                self.state = 269
                self.invocationExpr()
                pass

            elif la_ == 5:
                self.state = 270
                _la = self._input.LA(1)
                if not(_la==MPParser.SUB_KW or _la==MPParser.NOT_KW):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.expr(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 291
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 274
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 275
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.MUL_KW) | (1 << MPParser.DIVR_KW) | (1 << MPParser.MOD_KW) | (1 << MPParser.AND_KW) | (1 << MPParser.DIV_KW))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 276
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 277
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 278
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.ADD_KW) | (1 << MPParser.SUB_KW) | (1 << MPParser.OR_KW))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 279
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 280
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 281
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.NOTEQUAL_KW) | (1 << MPParser.EQUAL_KW) | (1 << MPParser.LESSTHAN_KW) | (1 << MPParser.GREATERTHAN_KW) | (1 << MPParser.LESSOREQUAL_KW) | (1 << MPParser.GREATEROREQUAL_KW))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 282
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 283
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 284
                        _la = self._input.LA(1)
                        if not(_la==MPParser.ORELSE_KW or _la==MPParser.ANDTHEN_KW):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 285
                        self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = MPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 286
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 287
                        self.match(MPParser.LSB)
                        self.state = 288
                        self.expr(0)
                        self.state = 289
                        self.match(MPParser.RSB)
                        pass

             
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




