enwordlist.csv

import csv

datos = [
    ["Probe", "Sectag", "Relatedu", "Firstnum", "Dis1num", "Dis2num", "Bignum", "Oddeven"],
    ["HANDS", "FEET", f,"0:06","0","0:12",1111111,f]
    ["STORE", "SHOP", f,"0:06","0:02","0:10",2222222,j]
    ["CURTAIN", "DRAPE", f,"0:06","0:06","0:06",3333333,f]
    ["CAT", "KITTEN", f,"0:09","0","0:09",4444444,j]
    ["PONDER", "THINK", f,"0:09","0:02","0:07",5555555,f]
    ["BAG", "SACK", j,"0:09","0:06","0:03",6666666,j]
    ["STRAW", "HAY", j,"0:06","0","0:12",7777777,f]
    ["WEEDS", "ROOTS", j,"0:06","0:02","0:10",8888888,j]
    ["PROMISE", "PLEDGE", f,"0:06","0:06","0:06",9999999,f]
    ["PROFIT", "LOSS", j,"0:09","0","0:09",10101010101010,j]
]

# Nombre del archivo CSV
nombre_archivo = "datos_ejemplo.csv"

# Escribir los datos en el archivo CSV
with open(nombre_archivo, 'w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(datos)

print(f"Archivo CSV '{nombre_archivo}' generado correctamente.")