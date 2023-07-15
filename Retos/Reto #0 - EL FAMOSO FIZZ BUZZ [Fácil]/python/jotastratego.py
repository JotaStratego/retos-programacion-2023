"""
/*
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/
"""

for i in range(1, 101):
    
    if i % 3 == 0 and i % 5 == 0:
        i = "fizzbuzz"
    elif i % 5 == 0:
        i = "buzz"
    elif i % 3 == 0:
        i = "fizz"
    else:
        i = i
    
    print(i)

"""
En este ejercicio he aprendido que el orden en el que se colocan los condicionales es importante para la ejecución de 
los mismos. Ya que se evalua de arriba a abajo. Si la primera ya se cumple, esa es la que se realiza. 
"""
