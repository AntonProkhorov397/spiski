#4
spisok2=[]
for element in spisok:
    spisok2.append(abs(element))
print(spisok2.sort())
print(spisok2.sort(reverse=True))

#3
spisok=[]
N=randint(2,20)
for i in range(N):
    spisok.append(randint(-50,50))
print(spisok)
max=-50
for element in spisok:
    if element>max: max=element
new_max=max/N #len(spisok)
spisok.index(max)
ind=spisok.insert(max)
spisok.insert(ind,new_max)
print(spisok)


#2
from random import *
spisok=[]
N=randint(2,20)
for i in range(N):
    spisok.append(randint(-50,50))
print(spisok)
while 1:
    try:
        k=int(input("Mis positsioonist alustada vahemust"))
        if k<=N//2:
            break
    except ValueError:
        print("Arv peab olema väiksem kui",N//2)
k-=1
for i in range(k,-1,-1):
    print(spisok[i],end="<->")
    print(spisok[N-i-1])
    a=spisok.pop(i)
    spisok.insert(N-i-1-1,a)
    a=spisok.pop(N-i-1)
    spisok.insert(a,a)
print(spisok)



#1 задание
maakonnad=["Tallinn","Narva","Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa","Lääne-Virumaa","Jõgevamaa","Tartu linn","Tartumaa","Põlvamaa","Võrumaa","Valgamaa","Viljandimaa","Järvamaa","Harjumaa","Raplamaa","Pärnumaa","Läänemaa","Hiiumaa","Saaremaa"]
while 1:
    try:
        index=int(input())
        if 10000<=index<=99999:
            break
    except ValueError:
        print("Vale index!")
index_1=index//10000
print(maakonnad[index_1-1])
if index_1<=3:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")



nimed=["Maks","BOT"]
for i in range(3):
    nimi=input("Sisesta nimi  ")
    nimed.append(nimi)
print(nimed)
nimed.sort(reverse=True)
print(nimed)
nimed.insert(1,input("Sisesta veel nimi"))
print(nimed)
nimed.remove("BOT")
print(nimed)
nimed.pop(2)
print(nimed)
print(len(nimed))
nimed.count(nimed[0])