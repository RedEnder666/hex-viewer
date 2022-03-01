import string
FORMAT = 16
nonprintable = set([chr(i) for i in range(128)]).difference(string.printable)

def del_n(st):
    for i in nonprintable:
        st = st.replace('i', '█')
    st = st.replace('\n', '█')
    return st

        
def conv(n, ri, ro):
    digs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    acc = 0
    for a in n:
        k = digs.find(a)
        acc = acc * ri + k
    res = ""
    while(acc > 0):
        k = acc % ro
        res = digs[k] + res
        acc = acc // ro
    return res    
    
FILENAME = input()
f = [conv(str(i), 10, FORMAT) for i in open(FILENAME, 'rb').read()]
print('          ', end='')
print(*[f"{conv(str(i), 10, 16).rjust(2, '0')}" for i in range(FORMAT)])
print()
z = 0
for i in range(0, len(f), FORMAT):
    print(conv(str(z), 10, FORMAT).rjust(5, "0").ljust(6, "0"), end='    ')
    print(" ".join([str(i).rjust(2, '0') for i in f[i:i + FORMAT]]).ljust(52, ' '), end='')
    k = "p"
    t = [chr(int((conv(k, FORMAT, 10)))) if conv(k, FORMAT, 10) else '.' for k in f[i:i + FORMAT]]
    b = del_n("".join(t))
    print(*rf'{b}', sep='')
    z += 1
input()
