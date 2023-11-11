# Lab 5 -> Antonio Ruiz Benito

def add (a, b):
    """Metodo para sumar 2 numeros pasados por parametro"""
    return a + b

def subtract (a, b ):
    """Metodo para restar 2 numeros pasados por parametro"""
    return a - b

def multiply (a, b):
    """Metodo para multiplicar 2 numeros pasados por parametro"""
    return a * b

def divide (a, b):
    """
    Metodo para dividir 2 numeros pasados por parametro,
    controlando la excepcion que pudiese ocurrir al dividir por 0
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero!!!")
        result = None
    return result


if __name__ == "__main__":
    print(sum(3, 9))
    print(subtract(27, 2))
    print(multiply(1987, 29))
    print(divide(100, 9))