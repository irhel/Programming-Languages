import ply.lex as lex
import re

tokens = (
        'IDENTIFIER',   
        'NUMBER',       
        'STRING',       
)

def t_NUMBER(token):
    r'-?[0-9]+\.?[0-9]*'
    token.value = float(token.value)
    return token

def t_IDENTIFIER(token):
    r'[a-zA-Z]+(?:_?[a-zA-Z]*)*'
    return token

def t_STRING(token):
    r'"(?:[^"]|[\"])*"'
    token.value = token.value[1 : -1]
    return token



t_ignore = ' \t\v\r'

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
    result = result + [tok.type,tok.value]
  return result

input1 = 'some_identifier -12.34 "a \\"escape\\" b"'
output1 = ['IDENTIFIER', 'some_identifier', 'NUMBER', -12.34, 'STRING', 
'a \\"escape\\" b']
print(test_lexer(input1) == output1)


input2 = '-12x34' 
output2 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
print(test_lexer(input2) == output2)
