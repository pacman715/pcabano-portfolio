d = {
    'a':'o',
    'b':'p',
    'c':'q',
    'd':'r',
    'e':'s',
    'f':'t',
    'g':'u',
    'h':'v',
    'i':'w',
    'j':'x',
    'k':'y',
    'l':'z',
    'm':'a',
    'n':'b',
    'o':'c',
    'p':'d',
    'q':'e',
    'r':'f',
    's':'g',
    't':'h',
    'u':'i',
    'v':'j',
    'w':'k',
    'x':'l',
    'y':'m',
    'z':'n'
}
text = 'bkftazdaowe'
answer = ''
for i in text:
    answer = answer + d[i]

print (answer)

    