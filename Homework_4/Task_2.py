def dict_key(**kwargs):
    return {v: k for k, v in kwargs.items()}


print(dict_key(x=5, y=8, c=10))
