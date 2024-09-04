class empleado:
# crear un programa que pida al usuario 3 empleados, el programa debe ordenarme 
#de manera ascendente cual es el empleado con mayor sueldo 
#nombre edad sueldo, si el empleado es >18age aumenta 5% else
# <18 age se disminuye 5%, mostrar todos los empleados aumentados o no 
#nombre que se les puso 


    def __init__(self):
        self.listaempleados=[]
        self.sueldos=[]
        self.sueldosmayores=[]
        self.sueldosmenores=[]

    
    
    def llenar_lista(self,nombre,edad,sueldo):
        nuevoempleado={"nombre":nombre,"edad":edad,"sueldo":sueldo}
        self.listaempleados.append(nuevoempleado)
        print ("Agregado exitosamente")


    def aumentomayores(self):
        self.mensajem=""
        iterador=0
        for objeto in self.listaempleados:
            nombre = objeto.get("nombre")
            edadd = objeto.get("edad")
            sueldo = objeto.get("sueldo")
            if edadd >18:
                aumento= sueldo + (sueldo * 0.05)
                self.sueldos.append(aumento)
                self.sueldosmayores.append(aumento)
                self.listaempleados[iterador]["sueldo"] = aumento
                self.mensajem += (f"{nombre} su sueldo se aumento 5% \n")
            iterador += 1

    
    def edadigual(self):
        self.mensajemen=""
        for objeto in self.listaempleados:
            edadd = objeto.get("edad")
            nombre = objeto.get("nombre")
            if edadd ==18:
                self.sueldos.append(objeto.get("sueldo"))
                self.mensajemen += (f"{nombre} su sueldo queda intacto\n")

    def dismimenores(self):
        self.mensaje=""
        iterador=0
        for objeto in self.listaempleados:
            nombre = objeto.get("nombre")
            edadd  = objeto.get("edad")
            sueldo = objeto.get("sueldo")
            
            if edadd <18:
                dismi= sueldo - (sueldo * 0.05)
                self.sueldos.append(dismi)
                self.sueldosmenores.append(dismi)
                self.listaempleados[iterador]["sueldo"] = dismi
                self.mensaje += (f"{nombre} su sueldo se disminuyo 5% \n")
            iterador +=1
    
    def sueldomayor(self):
        self.mayorsueldo= max(self.sueldos)


    def sueldomenor(self):
        self.menorsueldo= min(self.sueldos)
    
    def ordenarlista(self):
        self.sueldos.sort()


    def imprimir(self):
        print(f"aumentados: {self.mensajem}")
        print(f"disminuidos: {self.mensaje}")
        print(f"iguales:  {self.mensajemen}")
        print(f"sueldo mayor: {self.mayorsueldo}")
        print(f"sueldo menor {self.menorsueldo}")
        print(f"sueldos ascendentes: {self.sueldos}")
        print(f"estructura: {self.listaempleados}")
        