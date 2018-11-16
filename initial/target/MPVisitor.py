# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vDecl.
    def visitVDecl(self, ctx:MPParser.VDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varName.
    def visitVarName(self, ctx:MPParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varList.
    def visitVarList(self, ctx:MPParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mtype.
    def visitMtype(self, ctx:MPParser.MtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compType.
    def visitCompType(self, ctx:MPParser.CompTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primType.
    def visitPrimType(self, ctx:MPParser.PrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramList.
    def visitParamList(self, ctx:MPParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcDecl.
    def visitFuncDecl(self, ctx:MPParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procDecl.
    def visitProcDecl(self, ctx:MPParser.ProcDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifElseStmt.
    def visitIfElseStmt(self, ctx:MPParser.IfElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#matchStmt.
    def visitMatchStmt(self, ctx:MPParser.MatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unMatchStmt.
    def visitUnMatchStmt(self, ctx:MPParser.UnMatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#nonIfStmt.
    def visitNonIfStmt(self, ctx:MPParser.NonIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignLHS.
    def visitAssignLHS(self, ctx:MPParser.AssignLHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignStmt.
    def visitAssignStmt(self, ctx:MPParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invocationExpr.
    def visitInvocationExpr(self, ctx:MPParser.InvocationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forStmt.
    def visitForStmt(self, ctx:MPParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whileStmt.
    def visitWhileStmt(self, ctx:MPParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withStmt.
    def visitWithStmt(self, ctx:MPParser.WithStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnStmt.
    def visitReturnStmt(self, ctx:MPParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#dataTypeLit.
    def visitDataTypeLit(self, ctx:MPParser.DataTypeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#fParams.
    def visitFParams(self, ctx:MPParser.FParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)



del MPParser