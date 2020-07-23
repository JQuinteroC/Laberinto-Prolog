from pyswip import Prolog
from gifs import gif
prolog = Prolog()
# Lectura del archivo
mapa = open("laberinto.txt")
map = []
for i in mapa:
    map += [i.split(" ")]

def buscar_en_matriz(matriz, cont, para):
    if matriz == []:
        return (-1, -1)
    if para in matriz[0]:
        return [cont, matriz[0].index(para)]
    return buscar_en_matriz(matriz[1:], cont + 1, para)

def caminoLlegada(pos, k, j):
    alf = ["+", "|", "-"]
    try:
        for i in alf:
            temStr = map[pos[0]+k][pos[1]+j].replace(i, "")
        temInt = int(temStr)
        prolog.assertz(
            "conecta(" + map[pos[0]][pos[1]] + "," + temStr + ")")
    except:
        pass

def inicializar():
    ini = buscar_en_matriz(map, 0, "inicio")  # Inicio
    caminoLlegada(ini, 1, 0)
    caminoLlegada(ini, 0, 1)
    caminoLlegada(ini, -1, 0)
    caminoLlegada(ini, 0, -1)

    # LLenar las horizontales
    for i in range(1, len(map), 2):
        for j in range(1, len(map[i])-2):
            if not("|" in map[i][j]):
                prolog.assertz(
                    "conecta(" + map[i][j].replace('|', '') + "," + map[i][j+1].replace('|', '') + ")")

    # LLenar las verticales
    for i in range(1, len(map)-2):
        for j in range(0, len(map[i])-1):
            if "-" in map[i+1][j]:
                if("conecta(" + map[i][j].replace('|', '') + "," + map[i+2][j].replace('|', '') + ")" != "conecta(,)"):
                    prolog.assertz(
                        "conecta(" + map[i][j].replace('|', '') + "," + map[i+2][j].replace('|', '') + ")")

    # Llenar la posicion de inicio y de final
    fin = buscar_en_matriz(map, 0, "fin")  # Fin
    caminoLlegada(fin, 1, 0)
    caminoLlegada(fin, 0, 1)
    caminoLlegada(fin, -1, 0)
    caminoLlegada(fin, 0, -1)

    # Funciones de busqueda
    prolog.assertz('conectado(Pos1,Pos2) :- conecta(Pos1,Pos2)')
    prolog.assertz('conectado(Pos1,Pos2) :- conecta(Pos2,Pos1)')
    prolog.assertz('miembro(X,[X|_])')
    prolog.assertz('miembro(X,[_|Y]) :- miembro(X,Y)')
    prolog.assertz('sol :- camino([inicio],Sol),write(Sol)')
    prolog.assertz('camino([fin|RestoDelCamino],[fin|RestoDelCamino])')
    prolog.assertz('camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+ miembro(PosSiguiente,RestoDelCamino), camino([PosSiguiente,PosActual|RestoDelCamino],Sol)')
    
    # Realizar busqueda
    camino = []
    for inf in prolog.query("camino([inicio],Sol)"):
        for j in inf["Sol"]:
            camino += [j]
        break
    camino.reverse()
    camino[0] = "inicio"
    camino[-1] = "fin"
    return camino

camino = inicializar()

gi = gif(map)
gi.mover(camino)
root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('resources/movie.gif')
root.mainloop()

