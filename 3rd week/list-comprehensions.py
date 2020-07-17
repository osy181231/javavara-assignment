x = int(input())
y = int(input())
z = int(input())
n = int(input())
                
answer = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n]
print(answer)

#성공

#List Comprehension 없이도 해봤습니당
#answer = []
#for a in range(x+1):
#    for b in range(y+1):
#        for c in range(z+1):
#            if a + b + c != n:
#                answer.append([a,b,c])