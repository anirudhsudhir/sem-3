# Parse functions, if, variables
#
#
# <s-expression> ::= <atom> | <list>
#
# <list> ::= "(" <s-expressions> ")" | "(" ")"
#
# <s-expressions> ::= <s-expression> | <s-expression> <s-expressions>
#
# <atom> ::= <symbol> | <number> | <string> | <character>
#
# <symbol> ::= <identifier> | <keyword>
#
# <identifier> ::= <initial> <subsequent>* | <special-initial> <subsequent>*
#
# <initial> ::= <letter> | <special-initial>
#
# <special-initial> ::= "!" | "$" | "%" | "&" | "*" | "+" | "-" | "/" | ":" | "<" | "=" | ">" | "?" | "@" | "^" | "_" | "~"
#
# <subsequent> ::= <initial> | <digit> | "."
#
# <keyword> ::= ":" <identifier>
#
# <number> ::= <integer> | <float> | <ratio>
#
# <integer> ::= ["+"|"-"] <digit>+
#
# <float> ::= ["+"|"-"] <digit>+ "." <digit>+ ["e" ["+"|"-"] <digit>+]
#
# <ratio> ::= ["+"|"-"] <digit>+ "/" <digit>+
#
# <string> ::= '"' <string-character>* '"'
#
# <string-character> ::= <any-character-except-quote> | '\"'
#
# <character> ::= "#\" <any-character> | "#\" <character-name>
#
# <character-name> ::= "Space" | "Newline" | "Tab" | "Page" | "Rubout" | "Linefeed" | "Return" | "Backspace"
#
# <if> ::= "(if" <s-expression> <s-expression> [<s-expression>] ")"
#
# <lambda> ::= "(lambda" "(" <lambda-list> ")" <s-expressions> ")"
#
# <let> ::= "(let" "(" <binding>* ")" <s-expressions> ")"
#
# <binding> ::= "(" <symbol> <s-expression> ")"
#
# ; Function Application
# <function-call> ::= "(" <function-name> <s-expression>* ")"
#
# <function-name> ::= <symbol>

#
# def p_s_expression_atomic(p):
#     "s_expression : atomic_symbol"
#     p[0] = p[1]
#
#
# def p_s_expression_expression(p):
#     "s_expression : LPAREN s_expression DOT s_expression RPAREN"
#     # todo!
#
#
# def p_s_expression_list(p):
#     "s_expression : list"
#     p[0] = p[1]
#
#
# def p_list(p):
#     # Doubtful about second s_expression
#     "list : LPAREN s_expression s_expression RPAREN"
#     # todo!
#
#
# def p_atomic_symbol(p):
#     "atomic_symbol : letter atom_part"
#
#
# def p_atom_part_empty(p):
#     "atom_part : empty"
#     p[0] = p[1]
#
#
# def p_atom_part_letter_atom(p):
#     "atom_part : letter atom_part"
#     # todo!
#
#
# def p_atom_part_num_atom(p):
#     "atom_part : number atom_part"
#     # todo!
#
#
# def p_letter(p):
#     "letter : LETTER"
#     p[0] = p[1]
#
#
# def p_number(p):
#     "number : NUMBER"
#     p[0] = p[1]
#
#
# def p_empty(p):
#     "empty :"
#     pass
#

import ply.yacc as yacc

from lisp_lex import tokens


def p_s_expression_basic(p):
    """s_expression : atom
    | list
    | s_expression"""
    p[0] = p[1]


def p_s_expression_expressions(p):
    "s_expression : s_expression s_expression"
    # todo!


def p_list_expression(p):
    "list : LPAREN s_expression RPAREN"
    p[0] = p[1]


def p_list_empty(p):
    "list : LPAREN empty RPAREN"
    p[0] = []


def p_atom(p):
    """atom : symbol
    | number
    | string
    | char
    """
    p[0] = p[1]


def p_symbol(p):
    """symbol : identifier
    | keyword
    """
    p[0] = p[1]


def p_identifier(p):
    """identifier : initial subsequent
    | special_initial subsequent
    """
    # todo!


def p_initial(p):
    """initial : LETTER
    | special_initial
    """
    p[0] = p[1]


def p_special_initial(p):
    """special_initial : PLUS
    | MINUS
    | MULTIPLY
    | DIVIDE
    """
    p[0] = p[1]


def p_subsequent(p):
    """subsequent : subsequent
    | initial
    | DIGIT
    | DOT
    """
    p[0] = p[1]


def p_keyword(p):
    "keyword : COLON identifier"
    p[0] = p[1] + p[2]


def p_number(p):
    """number : integer"""
    p[0] = p[1]


def p_integer(p):
    "integer : digit"
    p[0] = int(p[1] + p[2])


def p_digit(p):
    """digit : digit
    | DIGIT"""
    p[0] = p[1]


def p_string(p):
    "string : DQUOTE chars DQUOTE"
    p[0] = p[1]


def p_chars(p):
    """chars : chars
    | LETTER
    """
    p[0] = p[1]


def p_char(p):
    """char : LETTER
    | DQUOTE
    """
    p[0] = p[1]


def p_if(p):
    "if : LPAREN IF s_expression s_expression s_expression RPAREN"
    # todo!


def p_let(p):
    "let : LPAREN LET LPAREN bindings RPAREN s_expression RPAREN"
    # todo!


def p_bindings(p):
    """bindings : bindings
    | binding
    """
    p[0] = p[1]


def p_binding(p):
    "binding : LPAREN symbol s_expression RPAREN"
    # todo!


def p_function_call(p):
    "function_call : LPAREN function_name s_expression RPAREN"
    # todo!


def p_function_name(p):
    "function_name : symbol"
    p[0] = p[1]


def p_empty(p):
    "empty :"
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()
while True:
    try:
        s = input("CL > ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
