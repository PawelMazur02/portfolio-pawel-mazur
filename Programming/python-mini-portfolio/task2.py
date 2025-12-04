def hello(name, fun):
    fun()
    print(f"{name}")

def good_morning():
    print("Good morning", end =" ")

def good_afternoon():
    print("Good afternoon", end =" ")

def good_evening():
    print("Good evening", end =" ")

def good_night():
    print("Good night", end =" ")

def code_wrapper(fun):
    def wrapper(name, time):
        if 5 <= time < 12:
            fun(name, good_morning)
        elif 12 <= time < 18:
            fun(name, good_afternoon)
        elif 18 <= time < 22:
            fun(name, good_evening)
        else:
            fun(name, good_night)
    return wrapper

@code_wrapper
def hello_time(name,time):
    hello(name,time)
    
hello_time("Paweł", 7)

