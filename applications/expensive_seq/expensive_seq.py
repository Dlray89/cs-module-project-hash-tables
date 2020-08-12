# Your code here
import time

cache = dict()
def expensive_seq(x, y, z):
    # if args are not in cache dict
    if (x , y, z) not in cache:
        #if x less or equal to 0
        if x <= 0:
            # add args to the cache as a singular number
            cache[(x , y, z)] = y + z
        else:
            # if x is a positive non zero number

            cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z) + expensive_seq(x - 2, y + 2, z * 2) + expensive_seq(x - 3, y + 3, z * 3)
        
    return cache[(x, y, z)]
       



if __name__ == "__main__":
    start = time.time()
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")
        end = time.time()

    print(expensive_seq(150, 400, 800))
    print(f"time elapsed: {end - start}")
