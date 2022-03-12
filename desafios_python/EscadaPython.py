n = int(input())
cont = 0
i = 0
while i <= n:
    while (cont<=i):
        print(((n-i)*" ")+((cont)*"*"))
        cont+=1
    i+=1
        