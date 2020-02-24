
queries = int(input())
 
numbers = []
n = 0
while n < queries:
    a = int(input())
    numbers.append(a)
    n += 1
 
caso1 = []
caso2 = []
caso3 = []
caso4 = []
caso5 = []
caso6 = []
 
def casos(base,limite,h):
    l = base
    while l <= limite:
        h.append(l)
        l += 12
casos(7,103,caso1)
casos(8,104,caso2)
casos(9,105,caso3)
casos(10,106,caso4)
casos(11,107,caso5)
casos(12,108,caso6)
 
 
 
 
for i in numbers:
    if i in caso1:
        g = i-1
        g = str(g)
        print(g + " WS")
        continue
 
    elif i in caso2:
        g = i-3
        g = str(g)
        print(g + " MS")
        continue
    
    elif i in caso3:
        g = i-5
        g = str(g)
        print(g + " AS")
        continue
    
    elif i in caso4:
        g = i-7
        g = str(g)
        print(g + " AS")
        continue
    
    elif i in caso5:
        g = i-9
        g = str(g)
        print(g + " MS")
        continue
 
    
    elif i in caso6:
        g = i-11
        g = str(g)
        print(g + " WS")
        continue
 
 
 
 
    if i % 6 == 0:
        g = i+1
        g = str(g)
        print(g + " WS")
        continue
 
 
    elif i % 6 == 5:
        g = i+3
        g = str(g)
        print(g + " MS")
        continue
 
 
    elif i % 6 == 4:
        g = i+5
        g = str(g)
        print(g + " AS")
        continue
 
 
    elif i % 6 == 3:
        g = i+7
        g = str(g)
        print(g + " AS")
        continue
 
 
    elif i % 6 == 2:
        g = i+9
        g = str(g)
        print(g + " MS")
        continue
 
    
    elif i % 6 == 1:
        g = i+11
        g = str(g)
        print(g + " WS")
        continue