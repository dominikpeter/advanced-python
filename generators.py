# chain decorators

def square(x):
    for i in x:
      yield i**2
     
def negative(x):
    for i in x:
        yield abs(i)*-1
        
def to_percent(x):
    for i in x:
        string = str(i) + " %"
        yield string
     
#chain = to_percent(negative(square(range(1, 10))))
#list(chain)

#timeit
def timeit(func):
    def wrapper(*args, **kwargs):
        import datetime
        enter = datetime.datetime.now()
        result = func(*args, **kwargs)
        exit = datetime.datetime.now()
        time = (exit - enter).total_seconds()
        print(f"Total time = {time}")
        return result
    return wrapper

@timeit
def random_loop(n):
    import numpy as np
    x = np.zeros(n)
    for i in range(n):
        x[i] = np.random.randint(0, 100, n).mean()
    return x.mean()

#random_loop(100)
#random_loop(10000)







