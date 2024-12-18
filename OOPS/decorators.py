def greet(fx):
    def mx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks")
    return mx
@greet 
def hello():
    print("hello world")
@greet
def add(a,b):
    print(a+b)
hello()
add(2,4)