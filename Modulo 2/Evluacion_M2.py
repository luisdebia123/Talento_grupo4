import decimal

number_keys = {
    "unidad_cien_mil" : 0,
    "unidad_diez_mil" : 0,
    "unidad_mil" : 0, 
    "centena" : 0,
    "decena" : 0,
    "unidad" : 0   
    }

def numero_a_diccionario(numero):
    largo = len(str(numero))
    for i in str(numero):
        if largo == 6:
            number_keys['unidad_cien_mil'] = int(i)
        elif largo == 5:
            number_keys['unidad_diez_mil'] = int(i)
        elif largo == 4:
            number_keys['unidad_mil'] = int(i)
        elif largo == 3:
            number_keys['centena'] = int(i)
        elif largo == 2:
            number_keys['decena'] = int(i)
        elif largo == 1:
            number_keys['unidad'] = int(i)
        largo = (largo-1)


def graficar():
    contador = 11
    for i in range(0,12):
        #for j in range(0,6):
        for j in number_keys:
            if(i==0)or(i==11):
                print("   +-+   ", end="")
            elif(((number_keys[j])-contador)==0):
                print("  XXXXX  ", end="")
                number_keys[j]=number_keys[j]-1
            else:
                print("   | |   ", end="")
        contador = contador -1
        print("")
    print(" 100.000   10.000   1.000     100      10        1")


print("bienvenidos")
num = int(input("Ingrese un numero de hasta 6 digitos: "))
numero_a_diccionario(num)
graficar()
print("fin")

# Convierte el número a string
s_numero = str(num)
c_numero = len (s_numero)
agregar_punto = []
archiva_numero =[]
contar = 0
# el número en string es leido uno a uno y se inserta un punto
for i in s_numero :
    if contar==3 or contar==6 :
        agregar_punto.append(i)
        agregar_punto.insert(c_numero-3,".")
        contar = contar+1
    else : 
        agregar_punto.append(i)
        contar = contar+1
# se imprime el número en miles
print ()
print ("Número Ingresado")
print ("----------------")
for i in range(len(agregar_punto)):
    agregar_punto[i] = str(agregar_punto[i])
    b= agregar_punto[i]
    archiva_numero=b + b
    print (b, end="") 