def greet(fx):
    def mfx(n, m):
        print("1a\"good morning ")
        fx()
        print("2a\"code executed successfully")
        print("3a\"",n + m)
    print("4a\"outer block code")
    return mfx

def hello():
    print("5a\"Hello world ")
    
greet(hello)(1, 2)