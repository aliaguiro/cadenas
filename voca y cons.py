def contar_vocales(c):
    contador=0
    total=0
    
    for i in range (len(c)):
        if c[i]=='a' or c[i]=='e' or c[i]=='i' or c[i]=='o' or c[i]=='u':
            contador=contador+1
    total=contador
    return total

def palabra():
    opc=int(input("""
Preisone
    1 para ingrear palabra
    2 para salir \n"""))
    while (opc >0 and opc <2):
        cadena=str(input('Ingrese una Palabra '))
        c=cadena.lower()
        print ('Hay ', contar_vocales(c), 'vocales y ', (len(c)-contar_vocales(c)), ' consonantes')
        opc=int(input("""
Preisone
    1 para ingrear palabra
    2 para salir \n"""))

palabra()
