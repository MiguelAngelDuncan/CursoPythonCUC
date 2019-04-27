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
     
     