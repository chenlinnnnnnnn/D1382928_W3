n=int(input('請輸入一個五位數:'))
a=n//10000
b=(n%10000)//1000
c=(n%1000)//100
d=(n%100)//10
e=n%10
print('結果',end='\n')
print(a,end='\n')
print(b,end='\n')
print(c,end='\n')
print(d,end='\n')
print(e,end='\n')