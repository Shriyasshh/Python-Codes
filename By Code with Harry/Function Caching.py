import functools    #used for caching
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(14))
print("Done for14")
print(fx(6))
print("Done for 6")

print(fx(20))
print("Done for 20")
print(fx(14))
print("Done for14")
print(fx(6))
print("Done for 6")
print(fx(4))
print("Done for 4")