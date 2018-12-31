# chain generator

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






