from PIL import Image, ImageDraw, ImageFont
import imageio

class gif():
    def __init__(self, mapa):
        self.a = mapa
        self.reco = []
        self.nombres = []
        self.images = []

        self.crearImagen(self.a, 2, -1, -1, [])

    def mover(self, recorrido):
        self.reco = recorrido
        num = 3
        for i in self.reco:
            pos = buscar_en_matriz(self.a,0,i)
            index = self.reco.index(i)
            self.crearImagen(self.a,num,pos[0],pos[1], self.reco[0:index])
            num = num + 1
        self.crearGif()

    def crearImagen(self,a,paso, posi, posj, pos):
        x = 0
        y = 0
    
        image = Image.open("resources/Imagen1.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf",20)

        for i in range(len(a)):
            for j in range(len(a[i])):
                # Recorrido
                if str(a[i][j]).replace("|","") in pos: # Migas de pan
                    for recorridos in pos:
                        k = buscar_en_matriz(a,0,recorridos)
                        xtem = 50 * k[1]
                        ytem = 50 * k[0]
                        if "|" in a[k[0]][k[1]]:
                            draw.text((50 + xtem,50 + ytem), chr(9608),font=font, fill="red")
                        else:
                            draw.text((50 + xtem,50 + ytem), chr(9608),font=font, fill="red")
                if i == posi and j == posj: # Posición actual
                    if "|" in a[i][j]:
                        draw.text((50 + x,50 + y), chr(9632) + chr(9553),font=font, fill="red")
                        draw.text((50 + x,50 + y), "  " + chr(9553),font=font, fill="black")
                    else:
                        draw.text((50 + x,50 + y), chr(9632),font=font, fill="red")
                else:
                    # Barreras verticales
                    if "|" in a[i][j]:
                        k = str(a[i][j]).replace("|","") 
                        if k != "":
                            tt = str(a[i][j]).replace(k, "  ")
                            tt = tt.replace("|", chr(9553))
                        else:
                            tt = str(a[i][j]).replace("|", chr(9553))
                        draw.text((50 + x,50 + y), tt,font=font, fill="black")
                    elif (j == 0 or j == len(a[i])-1) and a[i][j] == "+":
                        draw.text((50 + x,50 + y),str(chr(9553)),font=font, fill="black")
                    elif str(a[i][j]) == "-":
                        draw.text((50 + x,50 + y)," ",font=font, fill="black")
                    elif str(a[i][j]) == "+": # Horizontal
                        draw.text((50 + x,50 + y),str(chr(9552)),font=font, fill="black")
                    elif j == len(a[i])-1:
                        draw.text((50 + x,50 + y), chr(9553),font=font, fill="black")
                    else: # numeros
                        draw.text((50 + x,50 + y)," ",font=font, fill="black")
                x += 50
            y += 50
            x = 0

        image.save("resources/Imagen"+ str(paso) +".png")
        self.nombres.append("resources/Imagen"+str(paso)+".png")

    def crearGif(self):
        for i in range(len(self.nombres)):
            self.images.append(imageio.imread(self.nombres[i]))

        imageio.mimsave('resources/movie.gif',self.images, duration=0.5)

def main():
    gif()
    return 0

def buscar_en_matriz(matriz, cont, para):
    if matriz == []:
        return (-1, -1)
    paraX = str(para) + "|"
    if str(para) in matriz[0]:
        return [cont, matriz[0].index(str(para))]
    elif paraX in matriz[0]:
        return [cont, matriz[0].index(str(paraX))]
    return buscar_en_matriz(matriz[1:], cont + 1, para)

if __name__ == '__main__':
    main()
