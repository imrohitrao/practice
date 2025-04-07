def print_args(*args):
    args_values = [str(arg) for arg in args]
    arg_values = ", ".join(args_values)
    print(args_values)
print_args("Hello", "World",5)



# def my_function(*args):
#     # print("a:", a)
#     # print("b:", b)
#     print("args:", args)

# my_function([1, 2, 3, 4, 5],5,"Hello", "World")