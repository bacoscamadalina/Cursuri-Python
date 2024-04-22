#                                GENERATOR
'''
GENERATOR = instrument pt crearea iteratiilor
'''


def genEven(n):
    generatednumbers = 0
    currentnumber = 0
    while generatednumbers < n:
        currentnumber += 1
        if currentnumber % 2 == 0:
            yield currentnumber
            generatednumbers += 1


gen = genEven(15)
for i in gen:
    print(i)


def my_gen():
    n = 1
    print('PRIMUL PRINT')
    yield n
    n += 1
    print('AL DOILEA PRINT')
    yield n
    n += 1
    print('AL TREILEA PRINT')
    yield n


mg = my_gen()
print(next(mg))
print(next(mg))
print(next(mg))
