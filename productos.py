#Se pide el nombre al usuario
nombre = input("Ingrese el nombre del producto: ")

#Se pide el precio unitario al usuario
precio_unitario = input("Ingrese el precio unitario: ")

#Verifiacion de tipo de dato de precio unitario
while True:
    
    #Se tratar de converir el precio unitario a float
    try:
        precio_unitario = float(precio_unitario)

    #Excepcion en caso de que la variable precio unitario no sea numerica
    except ValueError:
        print("Error, ingresaste un numero no valido")
        precio_unitario = input("Ingrese de nuevo el precio unitario: ")

    #Entra en el else si ninguna excepcion se dispara
    else:
        
        #Se verifica que el precio unitario sea un numero valido
        if precio_unitario >= 0:
            break

        #De no se un numero valido, le pedira al usuario ingresar el precio unitario de nuevo
        else:
            print("Error, ingresaste un numero no valido")
            precio_unitario = input("Ingrese de nuevo el precio unitario: ")


#Se pide el numero de productos adquiridos al usuario
num_product_adquiridos = input("Ingrese la cantidad de productos adquiridos: ")

#Verificacion de tipo de dato de numero de productos adquiridos
while True:
    
    #Se trata de convertir a entero a la variable num_product_adquiridos
    try:
        num_product_adquiridos = int(num_product_adquiridos)

    #Excepcion en caso de que la variable num_product_adquiridos no sea numerica
    except ValueError:
        print("Error, ingresaste un numero no valido")
        num_product_adquiridos = input("Ingrese de nuevo la cantidad de productos adquiridos: ")

    #Entra en el else si ninguna excepcion se dispara
    else:

        #Aqui se verifica que el tipo de dato no sea float y que sea mayor que 0
        if isinstance(num_product_adquiridos,float) or num_product_adquiridos < 0:
            print("Error, ingresaste un numero no valido")
            num_product_adquiridos = input("Ingrese de nuevo la cantidad de productos adquiridos: ")

        else:
            break


#Se pide el porcentaje de decuento al usuario
porcen_descuento = input("Ingrese el porcentaje de descuento en un rango de 0 a 100: ")

#Verificacion de tipo de dato de porcentaje de descuento
while True:
    
    #Se trata de convertir a entero a la variable porcen_descuento
    try:
        porcen_descuento = int(porcen_descuento)

    #Excepcion en caso de que la variable porcen_descuento no sea numerica
    except ValueError:
        print("Error, ingresaste un numero no valido")
        porcen_descuento = input("Ingrese de nuevo el porcentaje de descuento en un rango de 0 a 100: ")

    else:

        """Aqui se verifica que el tipo de dato no sea float 
        y que el porcentaje de descuento este en el rango de 0 a 100"""
        if isinstance(porcen_descuento,float):
            print("Error, ingresaste un numero no valido")
            porcen_descuento = input("Ingrese de nuevo el porcentaje de descuento en un rango de 0 a 100: ")

        #Aqui se verifica que porcen_descuento este en el rango correcto
        elif porcen_descuento < 0 or porcen_descuento > 100:
            print("El porcentaje de descuento tiene que estar entre 0 y 100")
            porcen_descuento = input("Ingrese de nuevo el porcentaje de descuento en un rango de 0 a 100: ")

        else:
            break


costo_sin_descuento = num_product_adquiridos * precio_unitario

costo_con_descuento = 0

#Costo_total en caso de que no haya descuento
costo_total = num_product_adquiridos * precio_unitario


#En caso de que si haya descuento, remplazaremos el valor de la variable costo_total
if porcen_descuento >= 1:
    costo_total = costo_sin_descuento - (costo_sin_descuento*porcen_descuento)/100


print(f"Nombre del producto: {nombre} \nMonto total: {costo_total:.2f}$")
