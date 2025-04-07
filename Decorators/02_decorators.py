def debug(func):
    def wrapper(*args, **kwargs):
        args_list = ',  '.join(str(arg) for arg in args)
        kwargs_list = ',  '.join(f"{key}: {value}" for key, value in kwargs.items())
        print(f"Calling {func.__name__} with arguments: {args_list}, {kwargs_list}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    pass

greet("chai", greeting="hi")
