import xlrd #pip install xlrd
from arrays import Array3D

def main():
    a3 = Array3D(34,33,14)
    for anio in range(1985,2019,1):
        ruta = './Precipitacion/'+str(anio)+'Precip.xls'

        archivo = xlrd.open_workbook(filename = ruta)
        hoja = archivo.sheet_by_index(0)
    

        for r in range(1,33,1):
            for c in range(0,14,1):
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))

    a = int(input("Año(1985-2019):"))
    e = int(input("Estado(1-32):"))
    m = int(input("Mes(1-12):"))
    print(f"{a3.get_item(a-1985,e,m)}")

    print("\n")
    print("########## Punto 1 ##########")

    tempa = int(input("Año(1985-2019):"))
    tempe = int(input("Estado(1-32):"))
    tempm = int(input("Mes(1-12):"))
    estado = a3.get_item(tempa-1985,tempe,0)
    mes = a3.get_item(tempa-1985,0,tempm)
    red = round(a3.get_item(tempa-1985,tempe,tempm),1)
    print(f"En el estado de {estado} llovió un promedio de {red} centímetros cúbicos en el mes de {mes} de {tempa}")

    print("\n")
    print("########## Punto 2 ##########")

    tempe2 = int(input("Estado(1-32):"))
    tempm2 = int(input("Mes(1-12):"))
    prom = 0
    for x in range(1985,2019,1):
        x = a3.get_item(x-1985,tempe2,tempm2)
        prom += x
    print(prom/34)

    print("\n")
    print("########## Punto 3 ##########")

    tempe3 = int(input("Estado(1-32):"))
    for a in range(1985,2018,1):
        a+=1
        for y in range(0,12,1):
            y+=1
            w = a3.get_item(a-1985,tempe3,y)
            prom = w+prom
    print(prom/408)

    print("\n")
    print("########## Punto 4 ##########")

    for s in range(1,33,1):
        for a in range(1985,2018,1):
            a+=1
            for y in range(12,13,1):
                y+=1
                w = a3.get_item(a-1985,s,y)
                prom= prom+w
    print(prom/(s*(a-1984)))

main()
