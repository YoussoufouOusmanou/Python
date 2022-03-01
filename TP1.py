def loulou():
    print("welcome")
    for i in range (1, 100) :
        if (i % 3) ==0 and (i % 5) == 0:
         print(i, "est modulo 3 et 5  loulou")
        elif (i % 3 ) == 0: 
         print(i, "est modulo 3 riri")
        elif (i % 5) == 0:
         print(i, "est modulo 5 fifi")
       
def lis (tab):
    i = 1
    j = 0
    for i in tab:
        i = i*2
        tab[j]=i
        j=j+1
    return print(tab)
    
loulou()
lis([1,2,4,6])
