from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])

    def visitFuncDecl(self,ctx:MPParser.FuncDeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt,
                        self.visit(ctx.mtype()))

    def visitProcDecl(self,ctx:MPParser.ProcDeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt)

    def visitBody(self,ctx:MPParser.BodyContext):
        return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    def visitStmt(self,ctx:MPParser.StmtContext):
        return self.visit(ctx.nonIfStmt().funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallStmt(Id(ctx.invocationExpr().ID.getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MPParser.ExprContext):
        return IntLiteral(int(ctx.dataTypeLit().INTLIT().getText()))

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return IntType()
        

