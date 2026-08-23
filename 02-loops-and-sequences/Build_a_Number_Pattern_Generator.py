def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        lista = []
        for num in range(n):
            lista.append(str(num+1))

    return " ".join(lista)
