s="AbCDEfghI"
def convert(s):
    if not s:
        return 0
    count=0
    for i in range(len(s)-1):
        if s[i].isupper()!=s[i+1].isupper():
            count+=1
    return count
print(convert(s))
