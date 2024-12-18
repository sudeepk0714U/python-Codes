import time
def usingWhile():
    while i<5000:
        i = i+1
        print(i)
    pass
def usingFor():
    for i in range(5000):
        print(i)
    pass
init = time.time()
usingWhile()
print(time.time()-init)
usingFor()