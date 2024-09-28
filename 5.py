n=int(input('輸入三位數字:'))
a=n//100
b=(n%100)//10
c=n%10
a,c=c,a
f=a*100+b*10+c
print('結果:',f)