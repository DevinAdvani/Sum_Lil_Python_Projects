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

def STW(x):#symbol to word count
    if x < 20 or x == 1000:
        return len(str(d[x]))
    elif len(str(x)) == 2:
        return len(d[int(str(x)[1])]) + len(d[int(str(x)[0] + '0')])
    elif x == 100 or 200 or 300 or 400 or 500 or 600 or 700 or 800 or 900:
        return len(d[int(str(x)[0])]) + d[100]
    elif len(str(x)) == 3:
        return len(d[int(str(x)[2])]) + len(d[int(str(x)[1] + '0')]) + d[100] + len(d[int(str(x)[0])]) + 3#and


#just painful


print(STW(100))
