contador = 0

def dev_count(func):
    def wrapper(*args, **kwargs):
        global contador
        contador += 1

        print(f"{str(contador).rjust(3)} -- {args[0]}")
        res = func(*args, **kwargs)
        print(f"{str(contador).rjust(3)} -- {res}")
        
        return res

    return wrapper
