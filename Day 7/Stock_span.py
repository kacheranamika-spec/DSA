#Stock Span Problem

n = 7
price = [100,80,60,70,6,75,85]
ans =[1]
for i in range(1,n):
    if price[i]<price[i-1]:
        ans