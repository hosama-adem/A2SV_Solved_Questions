#HosamaAdem
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bl=[]
n=int(input())
h=input().lower()
for I in h:
    if I not  in bl:
        bl.append(I)
f=len(al)
b=len(bl)      
if f==b:
    print("YES")
else:
    print("NO")    
    
        
            
