import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_simple_keyword(self):
    #     """test keywords"""
    #     self.assertTrue(TestLexer.test("end","end,<EOF>",1))
    #
    # def test_multi_keywords(self):
    #     self.assertTrue(TestLexer.test("while true THEN faLse","while,true,THEN,faLse,<EOF>",2))
    #
    # def test_simple_white_space_skip(self):
    #     self.assertTrue(TestLexer.test("abc def   _hj12","abc,def,_hj12,<EOF>",3))
    #
    # def test_keyword_Double_Dot(self):
    #     self.assertTrue(TestLexer.test("abc def ....  _hj12","abc,def,..,..,_hj12,<EOF>",4))
    #
    # def test_simple_array_declaration(self):
    #     self.assertTrue(TestLexer.test("var d: array [1 .. 5] of integer;","var,d,:,array,[,1,..,5,],of,integer,;,<EOF>",5))
    #
    # def test_simple_assignment_statement(self):
    #     self.assertTrue(TestLexer.test("""var d: array [1 .. 5] of integer;
    #                                         a:=5*4;
    #                                         d[1] := a;""",
    #                                    """var,d,:,array,[,1,..,5,],of,integer,;,a,:=,5,*,4,;,d,[,1,],:=,a,;,<EOF>""",6))
    #
    # def test_multi_assignment_statement_and_function_call(self):
    #     self.assertTrue(TestLexer.test("""  result   :=a   := b:=c:=5*4;
    #                                         print(a);""",
    #                                    """result,:=,a,:=,b,:=,c,:=,5,*,4,;,print,(,a,),;,<EOF>""",7))
    #
    # def test_for_statement_and_function_call(self):
    #     self.assertTrue(TestLexer.test("""  for i:= 1 to 10 do writeln(i);
    #                                     """,
    #                                    """for,i,:=,1,to,10,do,writeln,(,i,),;,<EOF>""",8))
    #
    # def test_for_statement_with_expression_and_function_call(self):
    #     self.assertTrue(TestLexer.test("""  for i:= a+1 downto b*10 do writeln(i);
    #                                     """,
    #                                    """for,i,:=,a,+,1,downto,b,*,10,do,writeln,(,i,),;,<EOF>""",9))
    #
    # def test_simple_function_declararion(self):
    #     self.assertTrue(TestLexer.test("""function max(num1, num2: Real): reaL;
    #                                         begin
    #                                             return 1;
    #                                         end
    #                                     """,
    #                                    """function,max,(,num1,,,num2,:,Real,),:,reaL,;,begin,return,1,;,end,<EOF>""",10))
    #
    # def test_complex_function_declararion(self):
    #     self.assertTrue(TestLexer.test("""function max(num1, num2: integer): integer;
    #                                         var
    #                                         result: integer;
    #                                         begin
    #                                             if (num1 > num2) then
    #                                                 result := num1
    #                                             else
    #                                                 result := num2;
    #                                             max := result;
    #                                         end
    #                                     """,
    #                                    """function,max,(,num1,,,num2,:,integer,),:,integer,;,var,result,:,integer,;,begin,if,(,num1,>,num2,),then,result,:=,num1,else,result,:=,num2,;,max,:=,result,;,end,<EOF>""",11))
    #
    # def test_simple_procedure_declararion(self):
    #     self.assertTrue(TestLexer.test("""procedure findMin(x, y, z: integer; var m: integer);
    #                                     begin
    #                                     end
    #                                     """,
    #                                    """procedure,findMin,(,x,,,y,,,z,:,integer,;,var,m,:,integer,),;,begin,end,<EOF>""",12))
    #
    # def test_complex_procedure_declararion(self):
    #     self.assertTrue(TestLexer.test("""procedure findMin(x, y, z: integer; var m: integer);
    #                                     begin
    #                                         if x < y then
    #                                             m := x
    #                                         else
    #                                             m := y;
    #
    #                                         if z <m then
    #                                             m := z;
    #                                     end
    #                                     """,
    #                                    """procedure,findMin,(,x,,,y,,,z,:,integer,;,var,m,:,integer,),;,begin,if,x,<,y,then,m,:=,x,else,m,:=,y,;,if,z,<,m,then,m,:=,z,;,end,<EOF>""",13))
    #
    # def test_line_comment(self):
    #     self.assertTrue(TestLexer.test("""a[10]:=10*c;// this is line comment;
    #                                     """,
    #                                    """a,[,10,],:=,10,*,c,;,<EOF>""",14))
    #
    # def test_block_comment(self):
    #     self.assertTrue(TestLexer.test(""" { This is block comment}
    #                                     a[10]:=10*c;
    #                                     { This is
    #                                     another
    #                                     block comment}
    #                                     """,
    #                                    """a,[,10,],:=,10,*,c,;,<EOF>""",15))
    #
    # def test_traditional_block_comment(self):
    #     self.assertTrue(TestLexer.test(""" (* This is traditional block comment  ; *)
    #                                     a[10]:=10*c;
    #                                     (* This is
    #                                     another
    #                                     traditional block comment  ; *)
    #                                     """,
    #                                    """a,[,10,],:=,10,*,c,;,<EOF>""",16))
    #
    # def test_block_comment_with_line_comment_inside(self):
    #     self.assertTrue(TestLexer.test(""" { A block comment with //a line comment inside}
    #                                         { Another
    #                                         block comment
    #                                         with //a line comment inside}
    #                                     """,
    #                                    """<EOF>""",17))
    #
    # def test_line_comment_with_block_comment_inside(self):
    #     self.assertTrue(TestLexer.test(""" // Line comment with {block comment inside}
    #                                     """,
    #                                    """<EOF>""",18))
    #
    # def test_line_comment_with_traditional_block_comment_inside(self):
    #     self.assertTrue(TestLexer.test(""" // Line comment with (*traditional block comment inside*)
    #                                     """,
    #                                    """<EOF>""",19))
    #
    # def test_traditional_block_comment_with_line_comment_inside(self):
    #     self.assertTrue(TestLexer.test(""" (* A block comment with //a line comment inside*)
    #                                     """,
    #                                    """<EOF>""",20))
    #
    # def test_multi_comments(self):
    #     self.assertTrue(TestLexer.test(""" (* A block comment with //a line comment inside*) a:=b+c;
    #                                         // Line comment with (*traditional block comment inside
    #                                         print(a);{ block comment}
    #                                     """,
    #                                    """a,:=,b,+,c,;,print,(,a,),;,<EOF>""",21))
    #
    # def test_error_token_block_comments(self):
    #     self.assertTrue(TestLexer.test(""" { A block comment with //a line comment inside a:=b+c;
    #                                     """,
    #                                    """Error Token {""",22))
    #
    # def test_error_token_traditional_block_comments(self):
    #     self.assertTrue(TestLexer.test(""" (* A block comment with //a line comment inside a:=b+c;
    #                                     """,
    #                                    """(,*,A,block,comment,with,<EOF>""",23))
    #
    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc","abc,<EOF>",24))
    #
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",25))
    #
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",26))
    #
    # def test_id_in_assignment_statement(self):
    #     self.assertTrue(TestLexer.test("aAsVN3:=__2ff*h3_h","aAsVN3,:=,__2ff,*,h3_h,<EOF>",27))
    #
    # def test_array_declaration(self):
    #     self.assertTrue(TestLexer.test("var arr:array[1 .. 10] of string;","var,arr,:,array,[,1,..,10,],of,string,;,<EOF>",28))
    #
    # def test_array_declaration_with_the_space_between_2_dots_error_token(self):
    #     self.assertTrue(TestLexer.test("var arr:array[1 . . 10] of string;","var,arr,:,array,[,1,Error Token .",29))
    #
    # def test_simple_if_statement(self):
    #     self.assertTrue(TestLexer.test("""if (arr[1]<>NULL) THEN
    #                                             print(a[1]);
    #                                             eLse
    #                                             print(a[10];""",
    #                                    """if,(,arr,[,1,],<>,NULL,),THEN,print,(,a,[,1,],),;,eLse,print,(,a,[,10,],;,<EOF>""",30))
    #
    # def test_assignment_statement_with_equal_token(self):
    #     self.assertTrue(TestLexer.test("""var b: boolean;
    #                                             b:=1=1;
    #                                             ""","""var,b,:,boolean,;,b,:=,1,=,1,;,<EOF>""",31))
    #
    # def test_if_statement_with_not_token(self):
    #     self.assertTrue(TestLexer.test("""If not(n1 = 0) Then Halt;
    #                                             ""","""If,not,(,n1,=,0,),Then,Halt,;,<EOF>""",32))
    #
    # def test_integer(self):
    #     self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",33))
    #
    # def test_integer_in_an_expression(self):
    #     self.assertTrue(TestLexer.test("1/10","1,/,10,<EOF>",34))
    #
    # def test_float_number_1(self):
    #     self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",35))
    #
    # def test_float_number_2(self):
    #     self.assertTrue(TestLexer.test("1e-12","1e-12,<EOF>",36))
    #
    # def test_float_number_3(self):
    #     self.assertTrue(TestLexer.test("1.0e-12","1.0e-12,<EOF>",37))
    #
    # def test_float_number_4(self):
    #     self.assertTrue(TestLexer.test("0.000000001","0.000000001,<EOF>",38))
    #
    # def test_float_number_5(self):
    #     self.assertTrue(TestLexer.test("1.","1.,<EOF>",39))
    #
    # def test_float_number_6(self):
    #     self.assertTrue(TestLexer.test(".1",".1,<EOF>",40))
    #
    # def test_float_number_7(self):
    #     self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",41))
    #
    # def test_float_number_8(self):
    #     self.assertTrue(TestLexer.test("1.2E-2","1.2E-2,<EOF>",42))
    #
    # def test_float_number_9(self):
    #     self.assertTrue(TestLexer.test("1.2e-2","1.2e-2,<EOF>",43))
    #
    # def test_float_number_10(self):
    #     self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",44))
    #
    # def test_float_number_11(self):
    #     self.assertTrue(TestLexer.test("9.0","9.0,<EOF>",45))
    #
    # def test_float_number_12(self):
    #     self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",46))
    #
    # def test_float_number_13(self):
    #     self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",47))
    #
    # def test_float_number_14(self):
    #     self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",48))
    #
    # def test_error_token(self):
    #     self.assertTrue(TestLexer.test("abc?def","abc,Error Token ?",49))
    #
    # def test_assignment_token(self):
    #     self.assertTrue(TestLexer.test("number:=5;","number,:=,5,;,<EOF>",50))
    #
    # def test_float_number_15(self):
    #     self.assertTrue(TestLexer.test("1..5","1.,.5,<EOF>",51))
    #
    # def test_string_lit(self):
    #     self.assertTrue(TestLexer.test("""s := "I like programming a lot";""","s,:=,I like programming a lot,;,<EOF>",52))
    #
    # def test_empty_string_lit(self):
    #     self.assertTrue(TestLexer.test("""s := "";""","s,:=,,;,<EOF>",53))
    #
    # def test_string_lit_with_blanks(self):
    #     self.assertTrue(TestLexer.test("""s := "   ";""","s,:=,   ,;,<EOF>",54))
    #
    # def test_string_lit_with_error_token_newline_and_return(self):
    #     self.assertTrue(TestLexer.test("""s := "I
    #                                             love you";
    #                                     ""","""s,:=,Error Token \"""",55))
    #
    # def test_string_lit_with_double_quotes_inside(self):
    #     self.assertTrue(TestLexer.test("""s := "I \\"love\\" you";
    #                                     ""","""s,:=,I \\"love\\" you,;,<EOF>""",56))
    #
    # def test_string_lit_with_escape_sequence_tokens(self):
    #     self.assertTrue(TestLexer.test("""s := "I\t\b\f\'love\' you";""","""s,:=,I	'love' you,;,<EOF>""",57))
    #
    # def test_boolean_lit(self):
    #     self.assertTrue(TestLexer.test("""while result=false do begin _true := tRUe; end;""","""while,result,=,false,do,begin,_true,:=,tRUe,;,end,;,<EOF>""",58))
    #
    # def test_boolean_lit_and_string_lit(self):
    #     self.assertTrue(TestLexer.test("""while result=True do print("True");""","""while,result,=,True,do,print,(,True,),;,<EOF>""",59))
    #
    # def test_token_IF_statement(self):
    #     self.assertTrue(TestLexer.test("""if a=b and c-d=b or f=false and g=true then ;""","""if,a,=,b,and,c,-,d,=,b,or,f,=,false,and,g,=,true,then,;,<EOF>""",60))
    #
    # def test_token_IF_statement_1(self):
    #     self.assertTrue(TestLexer.test("""if a=b then _if:=true; else i_f=false;""","""if,a,=,b,then,_if,:=,true,;,else,i_f,=,false,;,<EOF>""",61))
    #
    # def test_token_for_statement(self):
    #     self.assertTrue(TestLexer.test("""for i:= 10 downto 1 do print("*");""","""for,i,:=,10,downto,1,do,print,(,*,),;,<EOF>""",62))
    #
    # def test_token_for_statement_1(self):
    #     self.assertTrue(TestLexer.test("""for (i:= a*2) to (b+c)/2 do print("*");""","""for,(,i,:=,a,*,2,),to,(,b,+,c,),/,2,do,print,(,*,),;,<EOF>""",63))
    #
    # def test_token_break(self):
    #     self.assertTrue(TestLexer.test("""for i:= 10 downto 1 do
    #                                             begin
    #                                                 if i=5 then
    #                                                     break;
    #                                                 print("break");
    #                                             end"""
    #                                     ,"""for,i,:=,10,downto,1,do,begin,if,i,=,5,then,break,;,print,(,break,),;,end,<EOF>""",64))
    #
    # def test_token_continue_statement(self):
    #     self.assertTrue(TestLexer.test("""for i:= 10 downto 1 do
    #                                             begin
    #                                                 if i mod 2=1 then
    #                                                     continue;
    #                                                 print("continue");
    #                                             end""","""for,i,:=,10,downto,1,do,begin,if,i,mod,2,=,1,then,continue,;,print,(,continue,),;,end,<EOF>""",65))
    #
    # def test_token_return_statement(self):
    #     self.assertTrue(TestLexer.test("""function foo(a,b:integer):integer;
    #                                         begin
    #                                             return a+b;
    #                                         end;"""
    #                                    ,"""function,foo,(,a,,,b,:,integer,),:,integer,;,begin,return,a,+,b,;,end,;,<EOF>""",66))
    #
    # def test_token_compound_statement(self):
    #     self.assertTrue(TestLexer.test("""procedure foo(a,b:integer);
    #                                         begin
    #                                             print("sum = ",a+b);
    #                                             return;
    #                                         end;"""
    #                                    ,"""procedure,foo,(,a,,,b,:,integer,),;,begin,print,(,sum = ,,,a,+,b,),;,return,;,end,;,<EOF>""",67))
    #
    # def test_token_with_statement(self):
    #     self.assertTrue(TestLexer.test("""procedure foo();
    #                                         begin
    #                                             with a,b:integer;c:array[1 .. 2] of real; do
    #                                                 d=c[a] + b;
    #                                             return;
    #                                         end;"""
    #                                    ,"""procedure,foo,(,),;,begin,with,a,,,b,:,integer,;,c,:,array,[,1,..,2,],of,real,;,do,d,=,c,[,a,],+,b,;,return,;,end,;,<EOF>""",68))
    #
    # def test_token_call_statement(self):
    #     self.assertTrue(TestLexer.test("""foo(3, a+1, m(2));"""
    #                                    ,"""foo,(,3,,,a,+,1,,,m,(,2,),),;,<EOF>""",69))
    #
    # def test_token_main_procedure(self):
    #     self.assertTrue(TestLexer.test("""procedure main(); // no parameters are allowed
    #                                         begin
    #                                         end;"""
    #                                    ,"""procedure,main,(,),;,begin,end,;,<EOF>""",70))
    #
    # def test_token_AND_OR(self):
    #     self.assertTrue(TestLexer.test("""if a=true and b=true or a=false and b=false then;"""
    #                                    ,"""if,a,=,true,and,b,=,true,or,a,=,false,and,b,=,false,then,;,<EOF>""",71))
    #
    # def test_token_NOT(self):
    #     self.assertTrue(TestLexer.test("""if not a then;"""
    #                                    ,"""if,not,a,then,;,<EOF>""",72))
    # def test_token_NOT_AND_OR(self):
    #     self.assertTrue(TestLexer.test("""if not a and not b or c and not d then;"""
    #                                    ,"""if,not,a,and,not,b,or,c,and,not,d,then,;,<EOF>""",73))
    #
    # def test_token_wrong_NOT_no_spaces_between_NOT_AND_OR_THEN_and_ID(self):
    #     self.assertTrue(TestLexer.test("""if nota andnot borcand not dthen;"""
    #                                    ,"""if,nota,andnot,borcand,not,dthen,;,<EOF>""",74))
    #
    # def test_token_UNARY_NEGATIVE(self):
    #     self.assertTrue(TestLexer.test("""a:=-b+c;"""
    #                                    ,"""a,:=,-,b,+,c,;,<EOF>""",75))
    #
    # def test_token_COMPARISON(self):
    #     self.assertTrue(TestLexer.test("""if a>b+c and a <> e or e<=f and j=k then;"""
    #                                    ,"""if,a,>,b,+,c,and,a,<>,e,or,e,<=,f,and,j,=,k,then,;,<EOF>""",76))
    #
    # def test_token_arithmetic_operator(self):
    #     self.assertTrue(TestLexer.test("""a:= b / c * d + e div f mod g - h;"""
    #                                    ,"""a,:=,b,/,c,*,d,+,e,div,f,mod,g,-,h,;,<EOF>""",77))
    #
    # def test_token_arithmetic_operator_with_no_spaces_between_ID_and_operator(self):
    #     self.assertTrue(TestLexer.test("""a:= b/c*d+edivfmodg-h;"""
    #                                    ,"""a,:=,b,/,c,*,d,+,edivfmodg,-,h,;,<EOF>""",78))
    #
    # def test_token_AND_THEN_operator(self):
    #     self.assertTrue(TestLexer.test("""if a and then b = false then;"""
    #                                    ,"""if,a,and then,b,=,false,then,;,<EOF>""",79))
    #
    # def test_token_OR_ELSE_operator(self):
    #     self.assertTrue(TestLexer.test("""if a OR eLSe b = false then;"""
    #                                    ,"""if,a,OR eLSe,b,=,false,then,;,<EOF>""",80))
    #
    # def test_token_AND_THEN_OR_ELSE_operators_together(self):
    #     self.assertTrue(TestLexer.test("""if a AND THEN b OR ELSE c = TRUE then;"""
    #                                    ,"""if,a,AND THEN,b,OR ELSE,c,=,TRUE,then,;,<EOF>""",81))
    #
    # def test_a_complex_token_AND_THEN_OR_ELSE_operators(self):
    #     self.assertTrue(TestLexer.test("""if a+b>0 aNd c+d<>0 AND THEN e*f<100 OR g/h=10 OR ELSE flag = FALSE then;"""
    #                                    ,"""if,a,+,b,>,0,aNd,c,+,d,<>,0,AND THEN,e,*,f,<,100,OR,g,/,h,=,10,OR ELSE,flag,=,FALSE,then,;,<EOF>""",82))
    #
    # def test_token_INDEX_operators(self):
    #     self.assertTrue(TestLexer.test("""foo()[3+x] := foo()[3+x]/2+(a[b[2]] +3);"""
    #                                    ,"""foo,(,),[,3,+,x,],:=,foo,(,),[,3,+,x,],/,2,+,(,a,[,b,[,2,],],+,3,),;,<EOF>""",83))
    #
    # def test_stringlit_with_unclosed_string_missing_closed_quotes(self):
    #     self.assertTrue(TestLexer.test("""s:=\"Principle Of Programming Language;"""
    #                                    ,"""s,:=,Unclosed String: "Principle Of Programming Language;""",84))
    #
    # def test_stringlit_with_unclosed_string_missing_open_quotes(self):
    #     self.assertTrue(TestLexer.test("""s:=Principle Of Programming Language\";"""
    #                                    ,"""s,:=,Principle,Of,Programming,Language,Unclosed String: ";""",85))
    #
    # def test_stringlit_with_one_double_quotes_inside(self):
    #     self.assertTrue(TestLexer.test("""s:=\"Principle Of \\"Programming Language\";"""
    #                                    ,"""s,:=,Principle Of \\"Programming Language,;,<EOF>""",86))
    #
    # def test_stringlit_with_one_single_quotes_inside_1(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \'Programming Language";"""
    #                                    ,"""s,:=,Principle Of 'Programming Language,;,<EOF>""",87))
    #
    # def test_stringlit_with_one_single_quotes_inside_2(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of 'Programming Language";"""
    #                                    ,"""s,:=,Principle Of 'Programming Language,;,<EOF>""",88))
    #
    # def test_stringlit_with_tabs(self):
    #     self.assertTrue(TestLexer.test("""s:=\"      Principle   Of      Programming         Language    \";"""
    #                                    ,"""s,:=,      Principle   Of      Programming         Language    ,;,<EOF>""",89))
    #
    # def test_error_stringlit_with_backslashes_inside_1(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \Programming Language";"""
    #                                    ,"""s,:=,Error Token \"""",90))
    #
    # def test_error_stringlit_with_backslashes_inside_2(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \\Programming Language";"""
    #                                    ,"""s,:=,Error Token \"""",91))
    #
    # def test_stringlit_with_backslashes_inside_3(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \\\Programming Language";"""
    #                                    ,"""s,:=,Principle Of \\\Programming Language,;,<EOF>""",92))
    #
    # def test_stringlit_with_backslashes_inside_4(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \\\\Programming Language";"""
    #                                    ,"""s,:=,Principle Of \\\\Programming Language,;,<EOF>""",93))
    #
    # def test_error_stringlit_with_backslashes_inside_5(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \\\\\Programming Language";"""
    #                                    ,"""s,:=,Error Token \"""",94))
    #
    # def test_error_stringlit_with_backslashes_inside_6(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \\\\\\Programming Language";"""
    #                                    ,"""s,:=,Error Token \"""",95))
    #
    # def test_stringlit_with_backslashes_inside_7(self):
    #     self.assertTrue(TestLexer.test("""s:="Principle Of \\\\\\\Programming Language";"""
    #                                    ,"""s,:=,Principle Of \\\\\\\Programming Language,;,<EOF>""",96))
    #
    # def test_another_legal_string(self):
    #     self.assertTrue(TestLexer.test("""s:="My name is Hai. His name's Nam.Her name is Su...";"""
    #                                    ,"""s,:=,My name is Hai. His name's Nam.Her name is Su...,;,<EOF>""",97))
    #
    # def test_another_correct_string(self):
    #     self.assertTrue(TestLexer.test("""s:="My name is Hai.\\n\tHis name's Nam.\\nHer name is Su...";"""
    #                                    ,"""s,:=,My name is Hai.\\n	His name's Nam.\\nHer name is Su...,;,<EOF>""",98))
    #
    # def test_an_illegal_string_with_new_line_character_inside(self):
    #     self.assertTrue(TestLexer.test("""s:="My name is Hai.\nHis name's Nam.Her name is Su...";"""
    #                                    ,"""s,:=,Error Token \"""",99))

    def test_another_illegal_string_with_carriage_return_insde(self):
        self.assertTrue(TestLexer.test(""" s:="hello, My \tname is Hai." """
                                       ,"""s,:=,Error Token \"""",100))


