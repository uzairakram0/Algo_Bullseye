import math

def throw(n):
    if n > 846357:
        return 1
    else:
        return 0
        
# s = start line, k = final line, d = number of darts
def bullseye(s, k, d):
    miss = 0
    i = s
    
    if d < 2:
        while i < k:
            miss = throw(i)
            if miss == 1:
                print(i-1)
                break
            i = i+1
    else:
        x = s + int(math.sqrt(k))
        miss = throw(x)
            
            
        if miss == 1:
            bullseye(s, x-1, d-1)
        else:
            bullseye(x, k, d)
    

k = 1000000
d = 2

print('The maximum line number from which the player hits bullseye:')
bullseye(0, k, d)

