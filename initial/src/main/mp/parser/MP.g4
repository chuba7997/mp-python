/**
 * Student name: Nguyễn Hồng Hải
 * Student ID: 1770471
 */
grammar MP;

/**
 Updated
*/
@lexer::header {
from lexerror import *
}

program: decl* EOF;
decl: vDecl | fDecl ;
vDecl: VAR_KW (varList SEMICOLON)+;
varName: ID;
varList: varName (COMMA varName)* COLON mpType;
mpType: (primType|compType);
compType: ARRAY_KW LSB expr DDOT expr RSB OF_KW primType;
primType: INTEGER_KW | REAL_KW | BOOLEAN_KW | STRING_KW;
fDecl: funcDecl | procDecl;
paramList: varList (SEMICOLON varList)*;
funcDecl: FUNCTION_KW funcName LB paramList? RB COLON mpType SEMICOLON vDecl* compoundStmt;
funcName: ID;
procDecl: PROCEDURE_KW procName LB paramList? RB SEMICOLON vDecl* compoundStmt;
procName: ID;
compoundStmt: BEGIN_KW stmt* END_KW;
stmt: ifElseStmt | nonIfStmt;
ifElseStmt: matchStmt | unMatchStmt;
matchStmt: IF_KW expr THEN_KW (matchStmt | nonIfStmt) ELSE_KW stmt ;
unMatchStmt: IF_KW expr THEN_KW stmt;
nonIfStmt:  assignStmt SEMICOLON | withStmt |  forStmt | whileStmt | BREAK_KW SEMICOLON | CONTINUE_KW SEMICOLON | returnStmt SEMICOLON | callStmt SEMICOLON | compoundStmt;
assignLHS: varName | expr LSB expr RSB;
assignStmt: <assoc=right> (assignLHS ASSIGN_KW)+ expr;
invocationExpr: ID LB fParams RB;
forStmt: FOR_KW ID ASSIGN_KW expr (TO_KW|DOWNTO_KW) expr DO_KW stmt;
whileStmt: WHILE_KW expr DO_KW stmt;
withStmt: WITH_KW (varList SEMICOLON)+ DO_KW stmt;
callStmt: ID LB fParams RB;
returnStmt: RETURN_KW | RETURN_KW expr ;
dataTypeLit: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT ;
fParams: (expr (COMMA expr)*)?;
expr: LB expr RB
    | dataTypeLit | ID | invocationExpr | expr LSB expr RSB
    | <assoc=right> (SUB_KW | NOT_KW) expr
    | expr (MUL_KW | DIV_KW | DIVR_KW | MOD_KW | AND_KW) expr
    | expr (ADD_KW | SUB_KW | OR_KW) expr
    | expr (EQUAL_KW | NOTEQUAL_KW | LESSTHAN_KW | LESSOREQUAL_KW | GREATERTHAN_KW | GREATEROREQUAL_KW) expr
    | expr (ANDTHEN_KW | ORELSE_KW) expr
    ;

/* Lexical Specification */
fragment A : [aA]; 
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
fragment LETTERS: [a-zA-Z];

/* Keywords */
BREAK_KW: B R E A K;
CONTINUE_KW: C O N T I N U E;
FOR_KW: F O R;
TO_KW: T O;
DOWNTO_KW: D O W N T O;
DO_KW: D O;
IF_KW: I F;
THEN_KW: T H E N;
ELSE_KW: E L S E;
RETURN_KW: R E T U R N;
WHILE_KW: W H I L E;
BEGIN_KW: B E G I N;
END_KW: E N D;
FUNCTION_KW: F U N C T I O N;
PROCEDURE_KW: P R O C E D U R E;
VAR_KW: V A R;
ARRAY_KW: A R R A Y;
OF_KW: O F;
WITH_KW: W I T H;

/* Operators */
ADD_KW: '+';
SUB_KW: '-';
MUL_KW: '*';
DIVR_KW: '/';
NOT_KW: N O T;
MOD_KW: M O D;
OR_KW: O R;
AND_KW: A N D;
ORELSE_KW: O R' 'E L S E;
ANDTHEN_KW: A N D' 'T H E N;
NOTEQUAL_KW: '<>';
EQUAL_KW: '=';
LESSTHAN_KW: '<';
GREATERTHAN_KW: '>';
LESSOREQUAL_KW: '<=';
GREATEROREQUAL_KW: '>=';
DIV_KW: D I V;
ASSIGN_KW: ':=';

/* Separators */
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
COLON: ':';
SEMICOLON: ';';
DDOT: '..';
COMMA: ',';

/* Literals */
fragment NUMBER: [0-9];
INTLIT: NUMBER+;

fragment EXPONENT: E[-]?NUMBER+;
fragment FRACTION: NUMBER+EXPONENT*;
FLOATLIT: NUMBER+[.]?FRACTION* | NUMBER*[.]?FRACTION+;

BOOLEANLIT: T R U E | F A L S E;

STRINGLIT: '"' (~[\b\f\r\n\t'"\\] | '\\' [bfrnt'"\\])* '"' {self.text=self.text[1:-1]} ;

/* Types */
BOOLEAN_KW: B O O L E A N;
INTEGER_KW: I N T E G E R;
REAL_KW: R E A L;
STRING_KW: S T R I N G;

/* Comments */
T_COMMENT: '(*' .*? '*)' -> skip;
B_COMMENT: '{' .*? '}' -> skip;
L_COMMENT: '//' ~[\r\n]* -> skip;

/* Identifiers */
ID: (LETTERS | '_')(LETTERS | NUMBER | '_')*;

WS : [ \t\r\n]+ -> skip ;

//ILLEGAL_CHAR: '"' ('\\' ~[t'] | ~'\\')* {raise IllegalCharInString(self.text)};
//ILLEGAL_ESCAPE: '"' ~[\r\n"]* '\\' ~[bfrnt'"\\]* '"' {raise IllegalEscapeInString(self.text)};
//ILLEGAL_ESCAPE: '"' ('\\' ~[bfrnt'"\\] | ~'\\')* '"' {raise IllegalEscapeInString(self.text)};

ILLEGAL_CHAR: . {raise IllegalCharInString(self.text[1:])};

//UNCLOSE_STRING: '"' (~'"')* EOF {raise UnclosedString(self.text)};
//ILLEGAL_ESCAPE: '"' ~[\r\n"]* ('\\' ~[bfrnt'"\\] | ~'\\')* {raise IllegalEscapeInString(self.text[1:])};
ILLEGAL_ESCAPE: '"' ~[\r\n"]* '\\' ~[bfrnt'"\\]* '"' {raise IllegalEscapeInString(self.text[1:])};
UNCLOSE_STRING: '"' (~'"')* {raise UnclosedString(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};

