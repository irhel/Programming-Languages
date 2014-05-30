import ply.lex as lex
import re 

def addresses(haystack):
    r = r'[a-zA-Z]+@[a-zA-Z]+(?:\.[a-zA-Z]+)+'
    s = haystack
    x = s.find("NOSPAM")
    while x != -1:
        s = s[0:x] + s[x:]
        s = s[:x] + s[(x + 6) :]
        x = s.find("NOSPAM")
    haystack = s
    return re.findall(r, haystack)
    

 
input1 = """louiseNOSPAMaston@germany.de (1814-1871) was an advocate for
democracy. irmgardNOSPAMkeun@NOSPAMweimar.NOSPAMde (1905-1982) wrote about
the early nazi era. rahelNOSPAMvarnhagen@berlin.de was honored with a 1994
deutsche bundespost stamp. seti@home is not actually an email address."""

output1 = ['louiseaston@germany.de', 'irmgardkeun@weimar.de', 'rahelvarnhagen@berlin.de']

print(addresses(input1) == output1)
