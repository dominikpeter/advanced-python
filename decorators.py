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
