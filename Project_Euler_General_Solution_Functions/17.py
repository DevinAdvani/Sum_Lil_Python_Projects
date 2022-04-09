d = {
0 : '',
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten',
11 : 'eleven',
12 : 'twelve',
13 : 'thirteen',
14 : 'fourteen',
15 : 'fifteen',
16 : 'sixteen',
17 : 'seventeen',
18 : 'eighteen',
19 : 'nineteen',
20 : 'twenty',
30 : 'thirty',
40 : 'fourty',
50 : 'fifty',
60 : 'sixty',
70 : 'seventy',
80 : 'eighty',
90 : 'ninety',
100 : 'hundred',
1000 : 'thousand'
}

def STW(x):#need to convert to physical words
    if x <= 20:
        return d[x]
    elif len(str(x)) == 2:
        a = d[int(str(x)[0] + '0')]
        b = d[int(str(x)[1])]
        return a + b
    elif len(str(x)) == 3:
        a = d[int(str(x)[0] + '00')]
        b = d[int(str(x)[1] + '0')]
        c = d[int(str(x)[2])]
        return a + b + c





for i in range(1,1000):
    print(STW(i))
