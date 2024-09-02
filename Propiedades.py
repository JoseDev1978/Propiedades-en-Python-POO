'''
Variables de Instancias
'''

class ExampleClass:
    def __init__(self, val = 1): #parametro con argumento = 1
        self.first = val #Variable de instancia (First)

    def set_second(self, val):
        self.second = val #Variable de instancia (Second)

example_object_1 = ExampleClass() #Prop. first
example_object_2 = ExampleClass(2)#Prop. second

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5   #El Objeto_3 se ha creado una variable de instancia (Third)
# fuera del bloque de codigo de la clase (ExampleClass)

print(example_object_1.__dict__) # __dict__ conjunto de propiedades y metodos predefinidos (Diccionario)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

'''Salida del programa es
{'first': 1}
{'first': 2, 'second': 3}
{'first': 4, 'third': 5}
'''
# Instancia de Clase

class ExampleClass:
    counter = 0 # se inicializa la variable en 0 (Variable de Clase)
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1 # la variable de clase se incrementa en 1 dentro del constructor


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

''' La salilda del programa
 {'first': 1} 1
 {'first': 2, 'counter': 2} 2
 {'first': 4, 'counter': 3} 3

'''
#comprobando la existencias de Atributos

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)

''' al ejecutar el programa obtenemos:
1
Traceback (most recent call last)
File ".main.py", line 11, in
print(example_object.b)
AttributeError: 'ExampleClass' object has no attribute 'b'
'''   

#como solucionar ese AttibuteError
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass
