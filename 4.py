n=int(input('請輸入一個三位數:'))
a=n//100
b=(n%100)//10
c=n%10
total=a+b+c
print("每個數字的總和:",total)