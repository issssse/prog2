
#(i:=[int(s) for s in input().split()])and print(sum(sum(x*x for x in p)<1 for p in ((__import__("random").uniform(-1,1) for _ in [0]*i[1]) for _ in [0]*i[0]))*2**i[1]/i[0])

#print((lambda n,d:sum(sum(x*x for x in p)<1 for p in ((__import__("random").uniform(-1,1) for _ in [0]*d) for _ in [0]*n))*2**d/n)(*map(int,input().split())))

#print((lambda n,d:sum(sum(__import__("random").uniform(-1,1)**2 for _ in[0]*d)<1 for _ in[0]*n)*2**d/n)(*map(int,input().split())))

print((lambda n,d:sum(sum(__import__("random").random()**2 for _ in[0]*d)<1 for _ in[0]*n)*4/n)(*map(int,input().split())))

# Function version:
# return sum(sum(uniform(-1,1)**2 for _ in[0]*d)<1 for _ in[0]*n)*2**d/n

# With semicolons allowed:
# from random import*;n,d=map(int,input().split());print(sum(sum(uniform(-1,1)**2 for _ in[0]*d)<1 for _ in[0]*n)*2**d/n)

