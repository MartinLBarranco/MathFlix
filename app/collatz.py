import matplotlib.pyplot as plt

def collatz(n:int)->int:
    """
        Hace una iteración de Collatz.
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n //2
    else:
        return 3*n+1

def cuentaIteraciones(n:int):
    """
        Input: Un número entero mayor o igual a 1.
        Output: El número de iteraciones que hay que hacer hasta llegar a 1.
    """
    if not isinstance(n, int):
        raise Exception("Tienes que meter un número entero mayor o igual a 1.")
    if n < 1:
        raise Exception("Tienes que meter un número entero mayor o igual a 1.")
    contador = 1
    a = n
    while a != 1:
        contador += 1
        a = collatz(a)
    return contador

def listaCollatz(n:int):
    """
        Input: Un entero mayor o igual a 1.
        Output: La lista de las iteraciones de Collatz del input hasta 1 
    """
    if not isinstance(n, int):
        raise Exception("Tienes que meter un número entero mayor o igual a 1.")
    if n < 1:
        raise Exception("Tienes que meter un número entero mayor o igual a 1.")
    ys = []
    a = n
    while a != 1:
        ys.append(a)
        a = collatz(a)
    ys.append(1)
    return ys

def dibujaNumIteraciones(n:int):
    """
        Dibuja una gráfica con el número de iteraciones que hace falta para llegar hasta 1 empezando por el número que indica el eje de ordenadas.
    """
    lista = list(map(cuentaIteraciones, range(1,n+1)))
    plt.figure(figsize=(15,10))
    plt.plot(range(len(lista)), lista, '-o')
    #plt.title(f"# iteraciones hasta llegar hasta 1 empezando desde donde indica el eje X.")
    plt.xlabel("Semilla")
    plt.ylabel("Cantidad de iteraciones")
    plt.grid(True)
    plt.show()

def dibujaNHastaUno(n:int):
    lista = listaCollatz(n)
    plt.figure(figsize=(15,10))
    plt.plot(range(len(lista)), lista, '-o')
    plt.title(f"Iteraciones de la sucesión de Collatz para el número {n}")
    plt.xlabel("Iteración")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.show()
