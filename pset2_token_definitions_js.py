import ply.lex as lex

def test_lexer(lexer,input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result
states = (
    
    ('commentD', 'exclusive'), #delimited comments
    ('commentI', 'exclusive'), #inline comments
)

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem. 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

t_ANDAND = r'\&\&'
t_COMMA = r'\,'
t_DIVIDE = r'/'
t_ELSE = r'else'
t_EQUAL = r'='
t_EQUALEQUAL = r'=='
t_FALSE = r'false'
t_FUNCTION = r'function'
t_GE = r'>='
t_GT = r'>'
t_IF = r'if'
t_LBRACE = r'{'
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE = r'}'
t_RETURN = r'return'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_TIMES = r'\*'
t_TRUE = r'true'
t_VAR = r'var'

t_ignore = ' \t\v\r'
t_commentD_ignore = ' '
t_commentI_ignore = ' '
def t_commentD(token):
    r'/\*'
    token.lexer.begin('commentD')

def t_commentD_end(token):
    r'\*/'
    token.lexer.begin('INITIAL')

def t_commentD_error(token):
    token.lexer.skip(1)



def t_commentI(token):
    r'//'
    token.lexer.begin('commentI')

def t_commentI_end(token):
    r'\n'
    token.lexer.begin('INITIAL')

def t_commentI_error(token):
    token.lexer.skip(1)

    
def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print("JavaScript Lexer: Illegal character " + t.value[0])
        t.lexer.skip(1)
        


lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    print(tok)
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print(test_lexer(input1) == output1)

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print(test_lexer(input2) == output2)

