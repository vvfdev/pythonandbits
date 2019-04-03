import time as ti, random as ra, ctypes as ct
nMax = 4
#Esta variable es para saber cuantos items va a poder almacenar, sí esto lo cambian y ponen 100 les van a salir 100
# datos diferentes en vez de 4, les recomiendo que lo prueben para que vean que es verdad

#Aquí creamos una clase que se llama eData y le damos un parametro dentro de los parentesis (ct.Structure) esto debe ser
#parte de la libreria que se importa más arriba (ctypes as ct)
class eData(ct.Structure):
 _fields_ = [ ('nBits', ct.c_ushort) ] #Esto representa el ushort que es el tipo de dato que estamos usando
 
#definimos una función con el nombre Make_Trama
def Make_Trama():
 #Aquí los 16 bits los dividen para asignar en cada parte de la memoria un dato diferente
 
 nID_Clave  = ra.randint(0x01, 0x0f) #1..015 = Clave producto -> 4Bits
 nID_Cantidad_Producto  = ra.randint(0x01, 0xff) #1..255 = Cantidad producto -> 8Bits
 nID_Precio_Producto  = ra.randint(0x01, 0x0f) #1..015 Precio Productos -> 4 Bits
 #los << son para los corrimientos decimales si mal no recuerdo.
 nTrama = nID_Clave << 12 | nID_Cantidad_Producto << 4 | nID_Precio_Producto #2 Bytes c/Información 16Bits
 return nTrama

#aMov es una array, matriz, lista, como sea que lo conozcan, es de una dimensión solo
aMov = [] ; ePaq = eData() #Invocamos la clase y la asignamos en una variable

for i in range(nMax):
 ePaq.nBits = Make_Trama()
 aMov.append(ePaq.nBits)
	
for nPos in range(nMax):
 print('\nWord     :' + str( aMov[nPos]))
 print('Código   :' + str( aMov[nPos] >> 12 & 0x0f))
 print('Cantidad :' + str( aMov[nPos] >> 4 & 0xff))
 print('Precio   :' + str( aMov[nPos] & 0x0f))
