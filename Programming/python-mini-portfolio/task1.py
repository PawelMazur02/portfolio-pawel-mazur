def suma(iter, step, start, direction=None):
    suma = start

    for i in range(iter):
        if direction is None:
            suma += step
        elif direction is True:
            suma += step
        else:
            suma -= step

    if direction is None:
        print("Wartość sumy:", suma)
    elif direction is True:
        return suma
    else:
        return suma - start


suma(5, 2, 1)

#%% 
roznica = suma(5, 2, 1, False)
print("Różnica:", roznica)
