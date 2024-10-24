from ply import lex, yacc


# Lexer
class LispLexer:
    # List of token names
    tokens = (
        "LPAREN",
        "RPAREN",
        "IF",
        "DEFUN",
        "SETQ",
        "IDENTIFIER",
        "NUMBER",
        "STRING",
        "T",
        "NIL",
    )

    # Regular expression rules for simple tokens
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    # Ignored characters (spaces and tabs)
    t_ignore = " \t\n"

    # Reserved words
    reserved = {"if": "IF", "defun": "DEFUN", "setq": "SETQ", "t": "T", "nil": "NIL"}

    def t_IDENTIFIER(self, t):
        r"[a-zA-Z][a-zA-Z0-9\-]*"
        # Check for reserved words
        t.type = self.reserved.get(t.value.lower(), "IDENTIFIER")
        return t

    def t_NUMBER(self, t):
        r"\d*\.?\d+"
        t.value = float(t.value) if "." in t.value else int(t.value)
        return t

    def t_STRING(self, t):
        r"\"[^\"]*\" "
        t.value = t.value[1:-1]  # Remove quotes
        return t

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)


# Parser
class LispParser:
    tokens = LispLexer.tokens

    def __init__(self):
        self.lexer = lex.lex(module=LispLexer())
        self.parser = yacc.yacc(module=self)

    def p_program(self, p):
        """program : form
        | program form"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_form(self, p):
        """form : function_definition
        | variable_definition
        | function_call
        | if_condition
        | literal"""
        p[0] = p[1]

    def p_function_definition(self, p):
        "function_definition : LPAREN DEFUN IDENTIFIER parameter_list body RPAREN"
        p[0] = {
            "type": "function_definition",
            "name": p[3],
            "parameters": p[4],
            "body": p[5],
        }

    def p_parameter_list(self, p):
        "parameter_list : LPAREN parameters RPAREN"
        p[0] = p[2]

    def p_parameters(self, p):
        """parameters :
        | IDENTIFIER parameters"""
        if len(p) == 1:
            p[0] = []
        else:
            p[0] = [p[1]] + p[2]

    def p_body(self, p):
        """body : form
        | form body"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[2]

    def p_variable_definition(self, p):
        "variable_definition : LPAREN SETQ IDENTIFIER form RPAREN"
        p[0] = {"type": "variable_definition", "name": p[3], "value": p[4]}

    def p_function_call(self, p):
        "function_call : LPAREN IDENTIFIER arguments RPAREN"
        p[0] = {"type": "function_call", "name": p[2], "arguments": p[3]}

    def p_arguments(self, p):
        """arguments :
        | form arguments"""
        if len(p) == 1:
            p[0] = []
        else:
            p[0] = [p[1]] + p[2]

    def p_if_condition(self, p):
        """if_condition : LPAREN IF test_form then_form RPAREN
        | LPAREN IF test_form then_form else_form RPAREN"""
        if len(p) == 6:
            p[0] = {"type": "if_condition", "test": p[3], "then": p[4], "else": None}
        else:
            p[0] = {"type": "if_condition", "test": p[3], "then": p[4], "else": p[5]}

    def p_test_form(self, p):
        "test_form : form"
        p[0] = p[1]

    def p_then_form(self, p):
        "then_form : form"
        p[0] = p[1]

    def p_else_form(self, p):
        "else_form : form"
        p[0] = p[1]

    def p_literal(self, p):
        """literal : NUMBER
        | STRING
        | T
        | NIL
        | IDENTIFIER"""
        if isinstance(p[1], (int, float)):
            p[0] = {"type": "number", "value": p[1]}
        elif p[1] == "t":
            p[0] = {"type": "boolean", "value": True}
        elif p[1] == "nil":
            p[0] = {"type": "boolean", "value": False}
        elif isinstance(p[1], str):
            if p.slice[1].type == "STRING":
                p[0] = {"type": "string", "value": p[1]}
            else:  # IDENTIFIER
                p[0] = {"type": "identifier", "value": p[1]}

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}'")
        else:
            print("Syntax error at EOF")

    def parse(self, text):
        return self.parser.parse(text)


if __name__ == "__main__":
    parser = LispParser()

    # # Test cases
    # test_cases = [
    #     # Function definition
    #     """(defun factorial (n)
    #         (if (= n 0)
    #             1
    #             (* n (factorial (- n 1)))))""",
    #     # Variable definition
    #     "(setq x 42)",
    #     # If condition
    #     '(if (> x 0) "positive" "non-positive")',
    #     # Function call
    #     '(print "Hello, World!")',
    # ]
    #
    while True:
        try:
            s = input("CL > ")
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)
