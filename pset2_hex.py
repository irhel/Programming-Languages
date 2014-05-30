import ply.lex as lex
tokens = ('NUM', 'ID')
def t_NUM_hex(token):
    r'0x[0-9a-f]+'
    s = token.value
    s = s[2:]
    res = 0
    l = len(s)
    p = 0
    for x in range(0, l):
        c = s[l - x - 1]
        res += (16**p) * int((ord(c) - ord('a') + 10) if c.isalpha() else c)
        p = p + 1
    token.value = res
    token.type = 'NUM'
    return token
def t_NUM_decimal(token):
    r'[0-9]+'
    token.value = int(token.value)
    token.type = 'NUM'
    return token
def t_ID(token):
    r'[a-zA-Z]+'
    return token
t_ignore = ' \t\v\r'
def t_error(t):
    print("Lexer: unexpecte character " + t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
s = "0x25 25823858235832 0x1 one two three"
lexer.input(s)
while True:
    t = lexer.token()
    if not t: break
    print(t)
    
