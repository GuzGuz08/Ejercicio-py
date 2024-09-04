from metodos import empleado

# crear un programa que pida al usuario 3 empleados, el programa debe ordenarme 
#de manera ascendente cual es el empleado con mayor sueldo 
#nombre edad sueldo, si el empleado es >18age aumenta 5% else
# <18 age se disminuye 5%, mostrar todos los empleados aumentados o no 
#nombre que se les puso 

empleados=empleado()


for i in range(3):
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    sueldo = int(input("ingrese su sueldo: "))
    empleados.llenar_lista(nombre,edad,sueldo)
empleados.aumentomayores()
empleados.edadigual()
empleados.dismimenores()
empleados.sueldomayor()
empleados.sueldomenor()
empleados.ordenarlista()
empleados.imprimir()



#4 sueldos, 4 edades,
# si el sueldo es mayor de 300mil y la edad mayor de 18
#se le sube un 40% sacar promedio de sueldos,edad min y max

