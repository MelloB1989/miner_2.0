txt = "alicemartin!dfjhfjcgh"
ch = 0
ps = 0
work = ""
pswd = ""
st = str(txt)
length = len(st)
while ch != length:
    cuch = st[ch]
    if cuch == "!":
         ps = ch + 1
         while ps != length:
            pswd = pswd + st[ps]
            ps = ps + 1
    '''
    else:
        work = work + cuch
    '''
    ch = ch + 1
ch = 0
while ch != length:
    cuch = st[ch]
    #print(cuch)
    if cuch == "!":
        break
    else:
        work = work + cuch
    ch = ch + 1
print(work)
print(pswd)