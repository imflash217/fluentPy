def greeting():
    return "Hello World"

###################################################
import time
def after(seconds, func):
    time.sleep(seconds)
    return func()

def new_greeting(name):
    return f"Hello {name}"

def helper():
    return new_greeting("Prithviraj")





if __name__ == "__main__":
    # print(greeting())
    # print(after(10, greeting))
    # print(after(3, new_greeting("Prithvi")))
    # print(after(3, helper))
    # print(after(3, lambda: new_greeting("Prithvi")))

    ## greetings = [lambda: new_greeting(name) for name in ["Prithvi", "Sanyogita"]]
    ## for g in greetings:
    ##     print(after(3, g))
    ##

    ## greetings = [lambda name=name: new_greeting(name) for name in ["Prithvi", "Sanyogita"]]
    ## for g in greetings:
    ##    print(after(3, g))

    #############################################################
    from functools import partial
    ## print(after(3, partial(new_greeting, "Prithvi")))

    ## greetings = [partial(new_greeting, name) for name in ["Prithvi", "Sanyogita"]]
    ## for g in greetings:
    ##     print(after(3, g))

    ## def new_after(seconds, func, args=()):
    ##     time.sleep(seconds)
    ##     return func(*args)
    ## print(new_after(3, new_greeting, "Prithvi"))
    ## print(new_after(3, new_greeting, ("Prithvi",)))

    def new2_after(seconds, func, *args):
        time.sleep(seconds)
        return func(*args)
    ## print(new2_after(3, new_greeting, "Prithvi"))

    def duration(*, hours, minutes, seconds):
        return 3600*hours + 60*minutes + seconds

    ## print(new2_after(3, duration, 1, 2, 3))
    ## print(new2_after(3, duration, hours=1, minuutes=2, seconds=3))

    def new3_after(seconds, func, *args, **kwargs):
        time.sleep(seconds)
        return func(*args, **kwargs)

    ## print(new3_after(3, duration, hours=1, minuutes=2, seconds=3))

    def new4_after(seconds, func, /, *args, **kwargs):
        time.sleep(seconds)
        return func(*args, **kwargs)

    print(new4_after(3, duration, hours=1, minutes=2, seconds=3))










