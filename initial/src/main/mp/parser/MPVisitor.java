// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecl(MPParser.DeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVDecl(MPParser.VDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#varName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarName(MPParser.VarNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#varList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarList(MPParser.VarListContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#mpType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMpType(MPParser.MpTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#compType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompType(MPParser.CompTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#primType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimType(MPParser.PrimTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#fDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFDecl(MPParser.FDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#paramList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParamList(MPParser.ParamListContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#funcDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncDecl(MPParser.FuncDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#funcName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncName(MPParser.FuncNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#procDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProcDecl(MPParser.ProcDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#procName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProcName(MPParser.ProcNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#compoundStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompoundStmt(MPParser.CompoundStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmt(MPParser.StmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#ifElseStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfElseStmt(MPParser.IfElseStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#matchStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMatchStmt(MPParser.MatchStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#unMatchStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnMatchStmt(MPParser.UnMatchStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#nonIfStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNonIfStmt(MPParser.NonIfStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#assignLHS}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignLHS(MPParser.AssignLHSContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#assignStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignStmt(MPParser.AssignStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#invocationExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInvocationExpr(MPParser.InvocationExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#forStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStmt(MPParser.ForStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#whileStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStmt(MPParser.WhileStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#withStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWithStmt(MPParser.WithStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#callStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallStmt(MPParser.CallStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#returnStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStmt(MPParser.ReturnStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#dataTypeLit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDataTypeLit(MPParser.DataTypeLitContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#fParams}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFParams(MPParser.FParamsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(MPParser.ExprContext ctx);
}