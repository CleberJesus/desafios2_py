
N = int(input())
list = []
while(N > 0):
    
    a = input()

    b = input()
    ar = len(a) - len(b)
    a = a[ar:]
    
    
    if b in a:
        list.append('encaixa')
    else:
        list.append('nao encaixa')
    
    N -= 1

for x in list:
    print(x)