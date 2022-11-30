#input-->  a3z2b4
#Output--> aaaabbbcc


def convertNumToString(s):
    l=[]
    output=''
    for ch in s:
        if ch.isalpha():
            l.append(ch)
            x=ch
        else:
            d=int(ch)
            output=output+x*d
    k=sorted(output)
    p=''.join(k)
    return p


s=input("Enter the string:\n")                                       # a3z2b4 
ans=convertNumToString(s)
print(ans)                                                           # aaabbbbzz
