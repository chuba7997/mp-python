import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_an_error_simple_program_declararion(self):
        input = """int main() {}"""
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,101))

    def test_another_error__program_declaration(self):
        input = """procedure main () {
        }"""
        expect = "Error on line 2 col 9: <EOF>"
        self.assertTrue(TestParser.test(input,expect,102))

    def test_a_simple_program(self):
        input = """procedure main(); begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,103))

    def test_var_declare(self):
        """Simple program: int main() {} """
        input = """var a , b , c : integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,104))

    def test_multi_var_declare(self):
        input = """var a , b , c : integer ; e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 105))

    def test_multi_var_declare_with_multi_VAR(self):
        input = """var a , b , c : integer ; VAR e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_array_declare_a_simple_array(self):
        input = """var d: array [1 .. 5] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_array_declaration_with_real_in_lower_bound(self):
        input = """var arr: array[1.5 .. 5] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,108))

    def test_array_declaration_without_double_dot(self):
        input = """var arr: array [1 5] of integer;"""
        expect = "Error on line 1 col 18: 5"
        self.assertTrue(TestParser.test(input,expect,109))

    def test_array_declaration_without_upper_bound(self):
        input = """var d: array [1 .. ] of integer;"""
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input,expect,110))

    def test_array_declaration_without_lower_bound(self):
        input = """var d: array [ .. 5] of real;"""
        expect = "Error on line 1 col 15: .."
        self.assertTrue(TestParser.test(input,expect,111))

    def test_MP_error_var_declare(self):
        input = """a , b , c : integer ;"""
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input,expect,112))

    def test_MP_simple_array_declare(self):
        input = """var a,b,c:integer;
                            d: array [1 .. 5] of integer;
                            e,f : real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,113))

    def test_MP_simple_array_declare_with_full_VAR(self):
        input = """var a,b,c:integer;
                           vAr d: array [1 .. 5] of integer;
                           vaR e,f : real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,114))

    def test_MP_simple_array_declare_with_multi_VAR(self):
        input = """var a,b,c:integer;
                            d: array [1 .. 5] of integer;
                           VAR e,f : real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,115))

    def test_array_declare_without_array_keyword(self):
        input = """var d: [1 .. 5] of real;"""
        expect = "Error on line 1 col 7: ["
        self.assertTrue(TestParser.test(input,expect,116))

    def test_array_declare_without_Primitive_Type(self):
        input = """var d: array [ 1 .. 5] of ;"""
        expect = "Error on line 1 col 26: ;"
        self.assertTrue(TestParser.test(input,expect,117))

    def test_array_declare_without_OF_keyword(self):
        input = """var d: array [ 1 .. 5] string;"""
        expect = "Error on line 1 col 23: string"
        self.assertTrue(TestParser.test(input,expect,118))

    def test_array_declare_without_VAR_keyword(self):
        input = """d: array [ 1 .. 5] of string;"""
        expect = "Error on line 1 col 0: d"
        self.assertTrue(TestParser.test(input,expect,119))

    def test_another_correct_array_declare(self):
        input = """function foo(): array [ 1 .. 2 ] of integer;
                    var number: integer;
                    begin
                        number:=5;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,120))

    def test_simple_function_declare(self):
        input = """function foo(): array [ 1 .. 2 ] of integer;
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,121))

    def test_simple_function_declare_with_param(self):
        input = """function foo(a,b: integer; c:real):real;
                    begin
                        x:=y:=z:=1+2;
                        result:=x*3.5;
                        print(y);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,122))

    def test_function_declare_with_array_declare_in_param(self):
        input = """function foo(a,b: integer; c:real;d: array [ 1 .. 5] of string):array [1 .. 2] of integer;
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,123))

    def test_complex_function_declare(self):
        input = """function foo(a,b: integer; c:real;d: array [ 1 .. 5] of string):array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin

                        return 3;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,124))

    def test_function_declare_error_missing_function_keyword(self):
        input = """foo(a,b: integer; c:real;d: array [ 1 .. 5] of string):array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 0: foo"
        self.assertTrue(TestParser.test(input,expect,125))

    def test_function_declare_error_missing_function_name(self):
        input = """function (a,b: integer; c:real;d: array [ 1 .. 5] of string):array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 9: ("
        self.assertTrue(TestParser.test(input,expect,126))

    def test_function_declare_error_missing_opening_bracket(self):
        input = """function foo a,b: integer; c:real;d: array [ 1 .. 5] of string):array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 13: a"
        self.assertTrue(TestParser.test(input,expect,127))

    def test_function_declare_error_missing_ending_bracket(self):
        input = """function foo(a,b: integer; c:real;d: array [ 1 .. 5] of string :array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 63: :"
        self.assertTrue(TestParser.test(input,expect,128))

    def test_function_declare_error_missing_a_semicolon_in_param_list(self):
        input = """function foo(a,b: integer c:real;d: array [1 .. 5] of string) :array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 26: c"
        self.assertTrue(TestParser.test(input,expect,129))

    def test_function_declare_error_missing_mptype_in_param_list(self):
        input = """function foo(a,b: integer; c:;d: array [1 .. 5] of string) :array [1 .. 2] of integer;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,130))

    def test_function_declare_error_missing_return_type(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string) :;
                    vaR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 64: ;"
        self.assertTrue(TestParser.test(input,expect,131))

    def test_simple_procedure_declare(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,132))

    def test_simple_procedure_declare_without_variable_declaration(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,133))

    def test_procedure_declare_error_with_return_type(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                    end"""
        expect = "Error on line 1 col 63: :"
        self.assertTrue(TestParser.test(input,expect,134))

    def test_compound_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                        s: string;
                        arr_1,arr_2: array[10 .. 100] of integer;
                    begin
                        a:=b*2;

                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 135))

    def test_simple_if_statement_with_compound_statement_in_body(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                    begin
                        if (x <= 1.5) AND (x>=5.5) AND (y>9) then
                            begin
                                y:=y+1;
                                print(y);
                            end

                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 136))

    def test_another_simple_if_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                    begin
                        if (x <= 1.5) then
                            y:=y+1;
                            print(y);

                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 137))

    def test_simple_if_else_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                    begin
                        if (x <= 1.5) then
                            print(y);
                        else
                            begin
                                y:=y+1.0;
                                print(y);
                            end
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 138))

    def test_an_error_if_else_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                    begin
                        if (x <= 1.5) then
                            begin
                                y:=y+1.0;
                                print(y);
                            end
                            print(y);
                        else
                            begin
                                y:=y+1.0;
                                print(y);
                            end
                        return;
                    end"""
        expect = "Error on line 10 col 24: else"
        self.assertTrue(TestParser.test(input, expect, 139))

    def test_another_error_if_else_statement_with_conditional_expression_after_ELSE(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y: real;
                    begin
                        if (x <= 1.5) then
                            begin
                                y:=y+1.0;
                                print(y);
                            end
                        else (x > 2)
                            begin
                                y:=y+1.0;
                                print(y);
                            end
                            print(y);
                        return;
                    end"""
        expect = "Error on line 9 col 24: else"
        self.assertTrue(TestParser.test(input, expect, 140))

    def test_nested_if_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y,z: integer;
                    result: string;
                    begin
                        if (x <= 1) then
                            if (y < 1) then
                                if (z <1) then
                                begin
                                    result:="fail";
                                    print(x+y+z);
                                end

                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 141))

    def test_nested_if_else_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y,z: integer;
                    result: string;
                    begin
                        if (x > 5) then
                            print("OK");
                        else
                            if y < 1 then
                                if(z <1)then
                                begin
                                    result:="fail";
                                    print(x+y+z,"=> NOT OK");
                                end

                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 142))

    def test_dangling_else(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y,z: real;
                    input: string;
                    begin
                        writeln("Are you 2017 student? Type:Yes/No: ");
                        readln(input);
                        if (input = "Yes") then
                            if ((x>=5.5) AND (y>=5.5)) then
                                if ((x+y)/2>=5.5) then
                                    print("PASSED => Medium");
                                else
                                    Print("FAIL");
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 143))

    def test_another_dangling_else(self):
        input = """function foo(result : integer) : integer;
                    begin
                        if count = 0 then
                            if count = 1 then
                                if (count = 2) then
                                    result := 0;
                            else
                                result := 1;
                        else
                            result := 2;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 144))

    def test_another_nested_if_else_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR x,y,z: real;
                    input: string;
                    begin
                        writeln("Are you 2017 student? Type:Yes/No: ");
                        readln(input);
                        if (input = "Yes") then
                            if ((x>=5.5) AND (y>=5.5)) then
                                if ((x+y)/2>=5.5) then
                                    print("AFTER 2017: PASSED => Medium");
                                else
                                    Print("AFTER 2017: FAIL");
                        else
                            if ((x>=5.0) AND (y>=5.0)) then
                                if ((x+y)/2>=4.95) then
                                    print("BEFORE 2017: PASSED => Medium");
                                else
                                    Print("BEFORE 2017: FAIL");

                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 145))

    def test_simple_for_to_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        For i := 1 to Length(myIntArray) do
                        Begin
                            myIntArray[i] := 1;
                            myBoolArray[i] := true;
                        End
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 146))

    def test_simple_for_downto_statement(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i :=  100 downto 1 do
                        Begin
                            myIntArray[i] := 10;
                            myBoolArray[i] := true;
                        End
                        return 1;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 147))

    def test_simple_for_statement_missing_expression1(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i :=  downto 1 do
                        Begin
                            myIntArray[i] := 10;
                            myBoolArray[i] := true;
                        End
                        return 1;
                    end"""
        expect = "Error on line 5 col 34: downto"
        self.assertTrue(TestParser.test(input, expect, 148))

    def test_simple_for_statement_with_wrong_assignment_expression(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i = 100 downto 1 do
                        Begin
                            myIntArray[i] := 10;
                            myBoolArray[i] := true;
                        End
                        return 1;
                    end"""
        expect = "Error on line 5 col 30: ="
        self.assertTrue(TestParser.test(input, expect, 149))

    def test_simple_for_statement_missing_expression_2(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i := 100 downto  do
                        Begin
                            myIntArray[i] := 10;
                            myBoolArray[i] := true;
                        End
                        return 1;
                    end"""
        expect = "Error on line 5 col 45: do"
        self.assertTrue(TestParser.test(input, expect, 150))

    def test_simple_for_statement_missing_DO_keyword(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i := 100 downto 1
                        Begin
                            myIntArray[i] := 10;
                            myBoolArray[i] := true;
                        End
                        return 1;
                    end"""
        expect = "Error on line 6 col 24: Begin"
        self.assertTrue(TestParser.test(input, expect, 151))

    def test_another_simple_for_statement(self):
        input = """function foo(a,b: integer; c:real;d: array [1 .. 5] of string): integer;
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i := 100 downto 1 do
                            myIntArray[i] := 10;
                        return 1;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 152))

    def test_2_nested_for_statement(self):
        input = """procedure foo(a,b: integer; c:real;d: array [1 .. 5] of string);
                    VAR myIntArray: array [ 1 .. 100] of integer;
                    myBoolArray: array [ 1 .. 100] of Boolean;
                    begin
                        fOr i := 100 downto 1 do
                            for j:= 1 to i do
                                print("*");
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 153))

    def test_3_nested_for_statement(self):
        input = """procedure foo();
                    begin
                        fOr i := 100 downto 1 do
                            for j:= 1 to i do
                                for k:= 1 to j do
                                    print("*");
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 154))

    def test_simple_while_statement(self):
        input = """procedure foo();
                    var i:integer;
                    begin
                        i := 0;
                        while (i < 100) do
                            print(i);
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 155))

    def test_another_simple_while_statement(self):
        input = """procedure foo();
                    var i:integer;
                    begin
                        i := 0;
                        while i < 100 do
                        begin
                            print(i);
                            writeln("&");
                        end
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 156))

    def test_while_statement_with_infinite_looping(self):
        input = """procedure foo();
                    begin
                        while true do
                        begin
                            print(i);
                            writeln("&");
                        end
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 157))

    def test_another_simple_while_statement_with_if_in_body(self):
        input = """procedure foo();
                    var stop: boolean;
                    i: integer;
                    begin
                        i:=0;
                        while (stop=false) do
                        begin
                            if (i<100) then
                            begin
                                print(i);
                                writeln("&");
                            end
                            else
                                stop:=true;

                            i:=i+1;
                        end
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 158))

    def test_while_statement_missing_conditional_expression(self):
        input = """procedure foo();
                    var stop: boolean;
                    i: integer;
                    begin
                        i:=0;
                        while do
                        begin
                            i:=i+1;
                        end
                        return;
                    end"""
        expect = "Error on line 6 col 30: do"
        self.assertTrue(TestParser.test(input, expect, 159))

    def test_while_statement_missing_DO_keyword(self):
        input = """procedure foo();
                    var stop: boolean;
                    i: integer;
                    begin
                        i:=0;
                        while true
                        begin
                            i:=i+1;
                        end
                        return;
                    end"""
        expect = "Error on line 7 col 24: begin"
        self.assertTrue(TestParser.test(input, expect, 160))

    def test_2_nested_while_loops(self):
        input = """procedure foo();
                    var stop: boolean;
                    i,j: integer;
                    begin
                        i:=0;
                        j:=0;
                        while i<100 do
                            while (j<100) do
                                print("*");
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 161))

    def test_3_nested_while_loops(self):
        input = """procedure foo();
                    var stop: boolean;
                    i,j: integer;
                    begin
                        i:=0;
                        j:=0;
                        while i<100 do
                            while j<100 do
                                while k < 100 do
                                    print("*");
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 162))

    def test_complex_for_loops(self):
        input = """procedure foo();
                    var stop: boolean;
                    i,j: integer;
                    begin
                        for i:=0 to 1000/2-1+1 do
                            if i>300 and i<500 then
                                break;
                            else if i mod 2 = 0 then
                                    print(i);
                                else
                                    continue;
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_complex_for_loops(self):
        input = """procedure foo();
                    var stop: boolean;
                    i,j: integer;
                    begin
                        for i:=0 to 1000/2-1+1 do
                            if i>300 and i<500 then
                                break;
                            else if i mod 2 = 0 then
                                    print(i);
                                else
                                    continue;
                        return;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_complex_array_assignment(self):
        input = """procedure main();
                    var a: array [1 .. 5] of integer;
                    begin
                        a[0] := a[1] := a[2] := n := b := 10;
                        a[3] := callAnyFunction();
                        a[4] := 1-5*2+4/6;
                        a[5] := 1-a[1]+a[2]*2-4+5*6;
                        z:=-foo(2);
                        y:=not true;
                        prime1:=not(isPrime(4));
                        prime2:=not isPrime(5);
                        prime3:=notisPrime(5);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 164))

    def test_multiple_assignment_with_function(self):
        input = """procedure main();
                    var a,b,c,d: integer;
                    begin
                        a:=b:=c:=d:=foo(a);                   
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 165))

    def test_multiple_compound_statement_inside_a_procedure(self):
        input = """procedure main();
                    var a,b,c:integer; s1,s2,s3:string;
                    begin
                        print("main compound statement");
                         begin
                            s1:="1th sub-compound statement";
                            print(s1);
                            a:=1;
                         end
                         begin
                            s2:="2th sub-compound statement";
                            print(s2);
                            b:=1;
                         end
                         begin
                            s3:="3th sub-compound statement";
                            print(s3);
                            c:=1;
                         end                 
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 166))

    def test_error_variable_declaration_with_initiation_value(self):
        input = """procedure main();
                    var a: integer := 1;
                    begin
                        print(a);
                    end"""
        expect = "Error on line 2 col 35: :="
        self.assertTrue(TestParser.test(input, expect, 167))

    def test_index_expression(self):
        input = """procedure main();
                    var a: array [1 .. 5] of integer;
                    begin
                        foo(2)[3+x] := a[b[2]] +3;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 168))

    def test_another_index_expression(self):
        input = """procedure main();
                    var a: array [1 .. 5] of integer;
                    begin
                        foo()[3+x] := foo()[3+x]/2+(a[b[2+i]] +3);
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 169))

    def test_another_function_declaration_with_param_and_return_with_an_expression(self):
        input = """function foo(a,b,c:integer;d,e:real;s:string): integer;
                    var x,y,z: integer; h,i,k:real;
                    begin
                        return a+b+c;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))

    def test_another_function_declaration_with_param_and_return_with_a_constant(self):
        input = """function foo(a,b,c:integer;d,e:real;s:string): integer;
                    var x,y,z: integer; h,i,k:real;
                    begin
                        return 1;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 171))

    def test_another_function_declaration_with_param_and_return_with_a_boolean_constant(self):
        input = """function foo(a,b,c:integer;d,e:real;s:string): boolean;
                    var x,y,z: integer; h,i,k:real;
                    begin
                        return true;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 172))

    def test_function_declaration_with_error_in_param(self):
        input = """function foo(a,b,c:integer;d,e:real;s:string;): integer;
                    var x,y,z: integer; h,i,k:real;
                    begin
                        return a+b+c;
                    end"""
        expect = "Error on line 1 col 45: )"
        self.assertTrue(TestParser.test(input, expect, 173))

    def test_simple_function_calls_function(self):
        input = """function foo(x,y,z:integer): integer;
                    begin
                        return x+y+z;
                    end
                    function goo(e:real;s:string): real;
                    var a: integer; h,i,k:real;
                    begin
                        a:=foo(1,2,3);
                        return a;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 174))

    def test_simple_procedure_calls_function(self):
        input = """function foo(x,y,z:integer): integer;
                    begin
                        return x+y+z;
                    end
                    procedure goo(e:real;s:string);
                    var a: integer; h,i,k:real;
                    begin
                        a:=foo(1,2,3);
                        return ;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 175))

    def test_simple_function_calls_procedure(self):
        input = """procedure foo(x,y,z:integer);
                    begin
                        print(x+y+z);
                        return;
                    end
                    function goo(e:real;s:string): integer;
                    var a: integer; h,i,k:real;
                    begin
                        a:=foo(1,2,3);
                        return a;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 176))

    def test_simple_procedure_calls_procedure(self):
        input = """procedure foo(x,y,z:integer);
                    begin
                        print(x+y+z);
                        return;
                    end
                    procedure goo(e:real;s:string);
                    var a: integer; h,i,k:real;
                    begin
                        a:=foo(1,2,3);
                        return ;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 177))

    def test_main_program_calls_function(self):  # gives correct result
        input = """function foo(x,y,z:integer):integer;
                    begin
                        return (x+y+z);
                    end
                    procedure main();
                    var a,b,c,d: integer; h,i,k:real;
                    begin
                        if not(foo(b,c,d)<=10) and then a<>0 then
                            print(a);
                        else
                            print("FAIL");
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 178))

    def test_another_main_program_calls_function_gives_different_parse_tree(self):  # gives wrong result
        input = """function foo(x,y,z:integer):integer;
                    begin
                        return (x+y+z);
                    end
                    procedure main();
                    var a,b,c,d: integer; h,i,k:real;
                    begin
                        if not foo(b,c,d)<=10 and then a<>0 then
                            print(a);
                        else
                            print("FAIL");
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 179))

    def test_another_main_program_calls_function_with_if_statement_inside(self):
        input = """function foo(x,y,z:integer):integer;
                    begin
                        return (x+y+z);
                    end
                    procedure main();
                    var a,b,c,d: integer; h,i,k:real;
                    begin
                        if not(a<>0) and (b<>c) or (c>=100) or else foo(b,c,d)<=10  then
                            print(a);
                        else
                            print("FAIL");
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 180))

    def test_declare_variables_after_declare_functions(self):
        input = """function foo(x,y,z:integer):integer;
                    begin
                        return (x+y+z);
                    end
                    procedure main();
                    var a,b,c,d: integer; h,i,k:real;
                    begin
                    end
                    var a,b,c:integer;x,y:real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 181))

    def test_declare_variables_between_function_declarations(self):
        input = """function foo(x,y,z:integer):integer;
                    begin
                        return (x+y+z);
                    end
                    var a,b,c:integer;x,y:real;
                    procedure main();
                    var a,b,c,d: integer; h,i,k:real;
                    begin
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 182))

    def test_call_function_and_missing_the_semi_after(self):
        input = """function foo(x,y,z:integer):integer;
                    begin
                        return (x+y+z);
                    end
                    var a,b,c:integer;x,y:real;
                    procedure main();
                    var a,b,c,d: integer;
                    begin
                        a:=foo(b+c+d)
                    end
                    """
        expect = "Error on line 10 col 20: end"
        self.assertTrue(TestParser.test(input, expect, 183))

    def test_test_variable_declaration_in_function_body(self):
        input = """ procedure main();                   
                    begin
                        var a,b,c,d: integer;
                        foo(b+c+d);
                    end
                    """
        expect = "Error on line 3 col 24: var"
        self.assertTrue(TestParser.test(input, expect, 184))

    def test_Illegal_escape(self):
        input = """ procedure main();
                    var a:string;
                    begin
                        a:="Nguyen Hong Hai\n\n\\";
                    end
                    """
        expect = """\""""
        self.assertTrue(TestParser.test(input, expect, 185))

    def test_a_legal_string_with_double_forward_slash(self):
        input = """ procedure main();
                    var a:string;
                    begin
                        a:="//Nguyen Hong Hai";
                    end
                    """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 186))

    def test_a_complex_array_assignment(self):
        input = """ procedure main();
                    var a:array [1 .. 5] of string;
                    begin
                        a[0] := a[1] := a[2] := n := b := 10;
                        a[3] := callAnyFunction();
                        a[4] := 1-2-4+5*6;
                    end
                    """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 187))

    def test_test_another_variable_declaration_in_function_body(self):
        input = """ procedure main();                   
                    begin
                        a,b,c,d: integer;
                        foo(b+c+d);
                    end
                    """
        expect = "Error on line 3 col 25: ,"
        self.assertTrue(TestParser.test(input, expect, 188))

    def test_array_declarartion_with_lower_bound_and_upper_bound_are_expressions(self):
        input = """var arr: array[1+2 .. 5*2] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,189))

    def test_another_array_declarartion_with_lower_bound_and_upper_bound_are_expressions(self):
        input = """var arr: array[(a+b+c)/3 .. (100 mod 11)] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,190))

    def test_a_completed_program_is_prime_number(self):
        input = """function isPrimeNumber(n:integer):boolean;
                        var i:integer;
                        begin
                            if (n<2) then return false;
                            for i:=2 to sqrt(n) do
                                if (n mod i = 0) then
                                    return false;
                            return true;
                        end
                    procedure main();
                        begin
                            print(isPrimeNumber(13));
                        end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,191))

    def test_a_completed_program_Fibonacci(self):
        input = """function fibonacciLoop(a:integer):integer;
                        var i,gt,lt:integer;
                        begin
                            gt:=lt:=1;
                            i:=0;
                            while i<a do
                            begin
                                gt:=gt+1;
                                lt := gt;
                                
                                i:=i+1;
                            end
                            return gt;
                        end
                    function fibonacciRecursive(a:integer):integer;
                        begin
                            if (a=1 or a=2) then 
                                return 1;
                            return fibonacciRecursive(a-1) + fibonacciRecursive(a-2);
                        end
                    function fibonacciTailRecursive(a:integer;gt:integer;lt:integer):integer;
                        begin
                            if a=1 then 
                                return gt;
                            return fibonacciTailRecursive(a-1,gt+lt,gt);
                        end
                    
                    var a:integer;
                    
                    procedure main();
                    var fibonacciNumber:integer;
                    begin                       
                        writeln("Input a: ");
                        a := getInt();
                        
                        fibonacciNumber:= fibonacciLoop(a);
                        print(fibonacciNumber);
                        
                        fibonacciNumber := fibonacciRecursive(a);
                        print(fibonacciNumber);
            
                        fibonacciNumber := fibonacciTailRecursive(a, 1, 1);
                        print(fibonacciNumber);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,192))

    def test_a_completed_program_solving_a_quadratic_equations(self):
        input = """
                    var a,b,c:real;
        
                    function getDelta(a,b,c:real):real;
                        begin
                            return b * b - 4 * a * c;
                        end
                        
                    procedure main();
                        var delta:real;
                        begin
                            writeln("Input a: ");
                            a := getInt();
                            writeln("Input b: ");
                            b := getInt();
                            writeln("Input c: ");
                            c := getInt();
                            
                            delta := getDelta(a, b, c);
                            if (delta < 0) then
                                writeln("Phuong trinh vo nghiem");
                                
                            if (delta = 0) then
                            begin
                                writeln("Phuong trinh co nghiem kep: ");
                                writeln((-b - sqrt(delta)) / (2 * a));
                            end
                            
                            if delta > 0 then
                            begin
                                writeln("Phuong trinh co 2 nghiem phan biet: ");
                                writeln("x1 = ");
                                writeln((-b + sqrt(delta)) / (2 * a));
                                writeln((-b - sqrt(delta)) / (2 * a));
                            end                            
                        end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,193))

    def test_with_statement(self):
        input = """       
                    procedure main();
                    begin
                        with a,b:integer;c:array[1 .. 2] of real; do
                            d := x:= y:= c [ a ] + b ;
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 194))

    def test_a_completed_MP_program_in_slide_15th_of_MP_specification_document(self):
        input = """
                    var i:integer;

                    function f():integer;
                    begin
                        return 200;
                    end

                    procedure main();
                    var main:integer;
                    begin
                        main:= f();
                        putIntLn(main);

                        with
                            i:integer;
                            main:integer;
                            f:integer;
                        do begin
                            main:=f:=i:=100;
                            putIntLn(i);
                            putIntLn(main);
                            putIntLn(f);
                        end

                        putIntLn(main);
                    end

                    var g:real;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 195))

    def test_another_simple_short_MP_program_PassOrFailSystem(self):
        input = """Procedure Main();
                    Var 
                        ActualMark : Integer;
                    
                        PossibleMark : Integer;
                    
                        PercentageMark : Real;
                    
                    Begin //{ PassOrFailSystem }
                                       
                        Writeln("Please type the student''s actual mark: ");
                        putIntLn (ActualMark);
                        
                        Writeln ("Please type the total possible mark of the exam : ");
                        putIntLn (PossibleMark);
                        
                        PercentageMark := (ActualMark / PossibleMark) * 100;
                        
                        If (PercentageMark >= 50) And Not(ActualMark<50) Then
                        Begin
                            Writeln();
                            Writeln ("Pass");
                        End
                        Else
                        Begin
                            Writeln(); 
                            Writeln ("Fail");
                        End
                        //{ EndIf }
                    
                    End //{ PassOrFailSystem }

                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 196))

    def test_another_simple_short_MP_program_TemperatureConversion(self):
        input = """
                    {****************************************}
                    FUNCTION ToFahrenheit(x: REAL): REAL;
                    { Function to convert degrees Celcius to }
                    { degree Fahrenheit.                     }
                    BEGIN
                         ToFahrenheit := 9/5 * x + 32;
                    END

                    {****************************************}
                    FUNCTION ToCelcius(x: REAL): REAL;
                    { Function to convert degrees Fahrenheit }
                    { to degree Celcius.                     }
                    BEGIN
                         ToCelcius := 5/9 * (x - 32);
                    END

                    Procedure Main();     
                    VAR answer,userInput:REAL; UserChoice:string;           
                    BEGIN
                         WRITELN("Choice a-ToFahrenheit or b-ToCelcius for conversion: ");
                         PutIntLn(UserChoice);

                         WRITELN("Enter a value for conversion: ");
                         PutIntLn(userInput);

                         IF (UserChoice = "a") THEN
                            answer := ToFahrenheit(UserInput);
                            
                         IF (UserChoice = "b") THEN
                            answer := ToCelcius(UserInput);

                        WRITELN();
                        WRITELN("        Degree");

                        IF (UserChoice = "a") THEN
                            WRITELN("Celcius    | Fahrenheit");
                            
                        IF (UserChoice = "b") THEN
                            WRITELN("FahrenHeit |   Celcius");

                        WRITELN("------------------------");
                        WRITE(UserInput);
                        WRITE("   |   ");
                        WRITE(Answer);
                        WRITELN();
                        WRITELN();

                    END
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 197))

    def test_a_complex_code_of_MP_program(self):
        input = """
                    Procedure Main();          
                    BEGIN
                         writeln(foo(arr[(b+c-h)/2])[3+x[5*(f/2)]] - goo(foo(1)[i+j]) + 5);
                    END

                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 198))  # goo(foo(1)[i+j]) + 5

    def test_invalid_MP_code_program_assignment_in_params_of_procedure_writeln(self):
        input = """
                    Procedure Main();          
                    BEGIN
                         writeln(a:=foo(arr[(b+c-h)/2])[3+x[5*(f/2)]-goo(foo(1)[i+j]) + 5);
                    END

                """
        expect = "Error on line 4 col 34: :="
        self.assertTrue(TestParser.test(input, expect, 199))

    def test_valid_MP_code_program_assignment_in_string_params_of_procedure_writeln(self):
        input = """
                    Procedure Main();          
                    BEGIN
                         writeln("a:=foo(arr[(b+c-h)/2])[3+x[5*(f/2)]-goo(foo(1)[i+j]) + 5");
                    END

                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_Invocation_expression(self):
        input = """
                    procedure foo ( a : array [ 1 .. 2 ] of real ); begin end
                    procedure goo ( x : array [ 1 .. 2 ] of real );
                    var
                        y : array [ 2 .. 3 ] of real ;
                        z : array [ 1 .. 2 ] of integer ;
                    begin
                        foo ( x ) ; //CORRECT
                        foo ( y ) ; //WRONG
                        foo ( z ) ; //WRONG
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_Invocation_expression(self):
        input = """
                    function goo ( ) : real;
                    begin
                        if a=true or else b=true then return 2.3 ; //CORRECT
                        else return 2 ; //CORRECT
                    end
                    
                    function foo (b : array [ 1 .. 2 ] of integer) : array [ 2 .. 3 ] of real;
                    var
                        a : array [ 2 .. 3 ] of real;
                    begin
                        if (a[5-3]=NULL) then return a ; //CORRECT
                        else return b ; //WRONG
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_Calling_fuction_statement(self):
        input = """
                    function goo (a:integer;b:real;c:string;d:integer) : real;
                    begin
                        if a=true or else b=true then return 2.3 ; //CORRECT
                        else return 2 ; //CORRECT
                    end
                    
                    procedure main ( );  
                    var x:array [1 .. 5] of integer;   
                        y:real;               
                    begin
                        y:=goo (3,a+1,m(2), x[4]) ;
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_another_testing_invalid_If_statement_with_assignment_in_condition_expression(self):
        input = """                    
                    procedure main ( );  
                    var x:array [1 .. 5] of integer;   
                        y:real;               
                    begin
                        if x:=3 then
                            print(x);
                    end
                """
        expect = "Error on line 6 col 28: :="
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_another_MP_program_isPrime(self):
        input = """                    
                    function isPrime(n: integer): boolean; 
                    var prime: boolean;  i,j: integer;
                    begin
                        prime := true;
                        if n<2 then primer := false;
                        else if n>3 then if (n mod 2 = 0) then primer := false;
                        else if n>5 then
                            begin k := round(n/6);
                                if (n<>(6*k-1) and n<>(6*k+1)) then primer := false;
                                else
                                    begin i := round(sqrt(n))+1; j := 3;
                                        while prime and (j<i) do
                                            begin prime := (n mod j)<>0; j := j+2; end
                                    end
                            end
                            
                            return prime;
                    end
                    procedure main(); 
                    begin 
                        for n:=0 to 1234567898765 do
                            if isPrime ( n ) then writeln(n, "is Prime");
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_another_test_MP_assignment_statement(self):
        input = """                                      
                    procedure main(); 
                    begin 
                        a:=b:=c:=2+5*4;
                        arr[1]:=10*2;
                        arr[2]:=arr[1+1]-100;
                        arr[3]:=foo(2)[2+1]-100;
                        foo(2)[3+x] := a[b[2]] +3;
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_another_test_MP_assignment_statement_1(self):
        input = """                                      
                    procedure main(); 
                    begin 
                        a:=b:=c:=2+5*4;
                        3-2*10:=2+5*4;
                        3-2*10:=a;
                    end
                """
        expect = "Error on line 5 col 30: :="
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_Call_statement_and_call_expression(self):
        input = """                                      
                    procedure foo(a : integer);
                    begin
                    end
                    function goo( a : integer): integer;
                    begin
                    end
                    procedure main();
                    begin
                         a:=foo(2);
                         goo(4);
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    # def test_Call_statement_and_call_expression_temp(self):
    #     input = """
    #                 procedure main();
    #                 begin
    #                     with a, b : integer; c : array [1 .. 2] of real; do
    #                         d = c [a] + b;
    #                 end
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 209))



