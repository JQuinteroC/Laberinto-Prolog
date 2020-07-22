from pyswip import Prolog
prolog = Prolog()
# Lectura del archivo
mapa = open("laberinto.txt")
map = []
for i in mapa:
    map += [i.split(" ")]

# LLenar las horizontales
#  ESTO YA FUNCIONA Y LO MANDA A PROLOG, PERO PRIMERO PRUEBAS :3
'''for i in range(1,len(map),2):
    for j in range(1, len(map[i])-2):
        if "|" in map[i][j]:
            print("tiene la cosa")
        else:
            prolog.assertz("conectado(" + map[i][j].replace('|', '') + "," + map[i][j+1].replace('|', '') + ")")
            '''

# LLenar las verticales
for i in range(1,len(map)-2):
    for j in range(0,len(map[i])-1):
        if "-" in map[i+1][j] and map[i][j]!="":
            print("conectado(" + map[i][j].replace('|', '') + "," + map[i+2][j].replace('|', '') + ")")

# ESTO ES PARA BUSCAR DONDE ESTA EL COMIENZO Y EL FIN, AUN FALTARIA BUSCAR DONDE ESTA LA POSICION ANTERIOR POR LA QUE PODRIA LLEGAR
def buscar_en_matriz(matriz, cont, para):
    if matriz == []:
        return (-1, -1)
    if para in matriz[0]:
        return [cont, matriz[0].index(para)]
    return buscar_en_matriz(matriz[1:], cont + 1, para)


print(buscar_en_matriz(map, 0, "inicio"))  # Inicio
print(buscar_en_matriz(map, 0, "fin"))  # Fin

""" prolog.assertz("conecta(inicio, 2)")
prolog.assertz("conecta(1, 7)")
-prolog.assertz("conecta(2, 3)")
prolog.assertz("conecta(2, 8)")
-prolog.assertz("conecta(3, 4)")
prolog.assertz("conecta(3, 9)")
prolog.assertz("conecta(4, 10)")
-prolog.assertz("conecta(5, 6)")
prolog.assertz("conecta(5, 11)")
prolog.assertz("conecta(7, 13)")
-prolog.assertz("conecta(8, 9)")
prolog.assertz("conecta(10, 16)")
prolog.assertz("conecta(11, 17)")
prolog.assertz("conecta(12, 18)")
-prolog.assertz("conecta(13, 14)")
-prolog.assertz("conecta(14, 15)")
prolog.assertz("conecta(14, fin)")
prolog.assertz("conecta(16, 22)")
prolog.assertz("conecta(22, 21)")
prolog.assertz("conecta(21, 15)")

prolog.assertz('conectado(Pos1,Pos2) :- conecta(Pos1,Pos2)')
prolog.assertz('conectado(Pos1,Pos2) :- conecta(Pos2,Pos1)')
prolog.assertz('miembro(X,[X|_])')
prolog.assertz('miembro(X,[_|Y]) :- miembro(X,Y)')
prolog.assertz('sol :- camino([inicio],Sol),write(Sol)')
prolog.assertz('camino([fin|RestoDelCamino],[fin|RestoDelCamino])')
prolog.assertz('camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+ miembro(PosSiguiente,RestoDelCamino), camino([PosSiguiente,PosActual|RestoDelCamino],Sol)')

print(str(prolog.query("sol"))) """
