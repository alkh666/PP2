# *args for multiple positional arguments
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sum_all(1,2,3,4))  # 10

# **kwargs for multiple named arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alikhan", age=20, country="Kazakhstan")

# combine *args and **kwargs
def combined(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

combined(1,2, name="Samet", city="Astana")