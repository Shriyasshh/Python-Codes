def my_gen():
    for i in range(5):
        yield i
    
g=my_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for j in g:
    print(j)