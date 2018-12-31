#function decorator
def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
    
@upper
def two_times_string(string):
    new_string = [i*2 for i in string]
    return "".join(new_string)
    
#two_times_string("hallo")

#class decorator
class my_decorator(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        result = self.f(*args, **kwargs)
        result = result.upper()
        return result

@my_decorator
def string_multiplier(string, n):
    new_string = string * n
    return new_string
    
#string_multiplier("hallo", 2)


#decorator with argument
def decorator(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            switch = {"upper": result.upper(),
                      "lower": result.lower(),}
            result = switch.get(argument, result)
            return result
        return wrapper
    return real_decorator
    
    
@decorator("lower")
def string_multiplier(string, n):
    new_string = string * n
    return new_string
    
    
#string_multiplier("HALLO", 2)



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



