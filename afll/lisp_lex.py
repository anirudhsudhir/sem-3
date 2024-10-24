import ply.lex as lex

reserved = {"if": "IF", "let": "LET"}

tokens = [
    "DIGIT",
    "LETTER",
    "LPAREN",
    "RPAREN",
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "DOT",
    "COLON",
    "DQUOTE",
] + list(reserved.values())

t_DIGIT = r"\d"
t_LETTER = r"[a-zA-Z]"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_PLUS = r"\+"
t_MINUS = r"\-"
t_MULTIPLY = r"\*"
t_DIVIDE = r"\/"
t_DOT = r"\."
t_COLON = r"\:"
t_DQUOTE = r"\""


# tokens = [
#     "NUMBER",
#     "LETTER",
#     "LPAREN",
#     "RPAREN",
#     "DOT",
# ]
#
# # todo!
# t_LETTER = r"[a-zA-Z]"
# t_LPAREN = r"\("
# t_RPAREN = r"\)"
# t_DOT = r"\."


# def t_NUMBER(t):
#     r"\d+"
#     t.value = int(t.value)
#     return t


# matching reserved tokens
def t_ID(t):
    # todo!
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
