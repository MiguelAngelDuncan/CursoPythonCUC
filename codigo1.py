# Comentario de linea
"""
Comentario de Parrafo
"""
# Hola Mundo
print("Hola Mundo")
# variables
x = 4 # int 
y = "texto"  # String
z = 4.5  # Float
a = True  # boolean
b = False # boolean
c = 4 + 5j # complejo 
print(x, y, z, a, b, c)
# Conocer el tipo de dato de una variable
print(type(b))

# Conversiones de tipos de datos

# enteros
x = int(2)
print(x)


x = int("2")
print(x)

# Float
x = float("2")
print(x)
x = float("2.5")
print(x)

# String
x = str("2")
print(x)
x = str("2.5")
print(x)

# manejo de cadenas de texto y alguno metodos

cad = "Hello World"
print(cad[0])
print(cad[2])
print(cad[0:4]) # No toma el ultimo valor

cad = "    Hello World     "
cad = cad.strip()
print(cad)
print(cad[0])

cad = "Hello World"
print(len(cad))
print(cad.lower()) # Minuscula

cad = "Hello World"
print(len(cad))
print(cad.upper()) # Mayuscula

print(cad.replace('l', 'Y'))
print(cad.split("l")

# Operaciones

# Operaciones Aritmetica
a = 2
b = 3
c = a + b
c = a - b 
c = a * b
c = a / b # Cociente
c = a % b # Residuo
c = a ** b # Exponente
c = math.sqrt(a) # Raiz
c = math.pi 

suma = a + b
print(r)

# Captura por consola
print ("Digite el nombre: ")
nombre = input()
print("Hola "+nombre+"!")
 
print("Digite el numero uno: ")
n1 = input()
n1 = float(n1)
print("Digite el numero dos: ")
n2 = input()
n2 = float(n2)
print(n1+n2)

# Condiciones

a = 2
b = 5
if a > b:
    print (a, "Es mayor que", b)
else:
    print (b, "Es mayor que", a)
    
if b > a:
    if b > 1:
        print (b, "Es mayor 1 y es mayor que",a )

if b > a:
    if b > 1:
    print (b, "Es mayor 1 y es mayor que",a )

if a == b:
    elif a > b:
    print (a, "Es mayor que", b)
else:
    print (b, "Es mayor que", a)
        
if a == b and a > 2:
    print (a, "Es igual a",b,"Mayor que 2") 
    
    if a == b or a > 2:
     print (a, "Es igual a",b,"Mayor que 2") 
     
     
     
print("Digite su edad: ")
edad=input()
edad=int(edad)
if edad>=18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")  
    

#Si de Linea con sino
print('Es mayor de edad') if edad>=18 else print ('Menor de edad')

#Si de Linea sin sino    
if edad >=18: print("Es mayor de edad")

# arrays
v = ["Hola", "Mundo", 4, 3.4, ["otro", "Arrays", "Dentro"]]
v2 = ["Hola", "Mundo"]
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v4 = range(1,10)
v5 = range(200)

for x in v5:
    print(x)

# Acceder al Elemento

print (v2[0])


#Modificar el elemento

v2[1] = "Roberto"

#Eliminar elemento

v2.remove("Hola")

#Eliminar el ultimo elemento
v.pop()
v.pop(4)

#Agregar elementos
v.append(5)
v.insert(1,"Roberto")

#Borrar el Vector
v.clear()

#Conocer la posición de un elemento
v.index('Mundo')

#Numero de elementos e un arrays
len(v)
# Cuantas veces aparece un elemento en el vector
v.append('Mundo')
v.count('Mundo')


#Ordenar un vector
a.sort()

# recorrer con saltos
# dos en dos
a= [5, 9, 6, 7, 11]
for x in a [0:3:2]:
    print(x)


#Preguntas si existe un elemento dentro de un arrays
a= [5, 9, 6, 7, 11]

20 in 4

res = 20 in a 
print(res)
# Acceder al ultimo elemento del vector
a[-3]
# Acceder a un elemento de un arrays interno
#Forma 1
aux = v[-1]
aux = aux[0]
print(aux)

#Forma2
aux = v[-1][0]
print (aux)

#matriz

m = [[2,4], [4,2]]

# Recorrer Vector
v = v [2:4]
for x in v:
    print(x)

print("Digite el valor final de la sumatoria")
a = int(input())
suma = 0
for x in range(a+1):
    suma = suma + x
print("La sumatoria es: ", suma) 
###################
print("Digite el valor final de la sumatoria")
a = int(input())
#suma = 0
sumatoria = sum(range(a+1))
print("La sumatoria es: ", sumatoria) 

#while
i = 1
while i<5:
    print(i)
    i = i + 1
  
#Funciones - Metodos
#Procedimiento no retorna valor
    def hola_mundo():
        print("Hola mundo")
#Invocar el procedimiento        
hola_mundo()

# Funcion que retorna valor
def elevar_cuadrado(numero):
    return numero ** 2

# Invocar función
elevar_cuadrado(3)
    