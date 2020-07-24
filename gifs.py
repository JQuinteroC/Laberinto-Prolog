from PIL import Image, ImageDraw, ImageFont
import imageio

class gif():
    def __init__(self, mapa):
        self.a = mapa
        self.reco = []
        self.nombres = []
        self.images = []

        self.crearImagen(self.a, 2, -1, -1)



    def mover(self, recorrido):
        self.reco = recorrido
        num = 3
        for i in self.reco:
            pos = buscar_en_matriz(self.a,0,i)
            self.crearImagen(self.a,num,pos[0],pos[1])
            num = num + 1
        self.crearGif()
    '''
    def crearImagen(self,a,paso, posi, posj):
        x = 0
        y = 0
    
        image = Image.open("resources/Imagen1.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf",20)

        for i in range(len(a)):
            for j in range(len(a[i])):
                if i == posi and j == posj:
                    draw.text((50 + x,50 + y),str(a[i][j]),font=font, fill="red")
                else:
                    if (j == 0 or j == len(a[i])) and a[i][j] == "+":
                        draw.text((50 + x,50 + y),"|",font=font, fill="black")
                    elif str(a[i][j]) == "-":
                        draw.text((50 + x,50 + y)," ",font=font, fill="black")
                    elif str(a[i][j]) == "+":
                        draw.text((50 + x,50 + y),"─",font=font, fill="black")
                    else:
                        draw.text((50 + x,50 + y),str(a[i][j]),font=font, fill="black")
                x += 50
            y += 50
            x = 0

        image.save("resources/Imagen"+ str(paso) +".png")
        self.nombres.append("resources/Imagen"+str(paso)+".png")
    '''

    def crearImagen(self,a,paso, posi, posj):
        x = 0
        y = 0
    
        image = Image.open("resources/Imagen1.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf",20)

        for i in range(len(a)):
            for j in range(len(a[i])):
                if i == posi and j == posj:
                    draw.text((50 + x,50 + y),str(char(169)),font=font, fill="red")
                else:
                    if (j == 0 or j == len(a[i])) and a[i][j] == "+":
                        draw.text((50 + x,50 + y),str(char(186)),font=font, fill="black")
                    elif str(a[i][j]) == "-":
                        draw.text((50 + x,50 + y),str(char(205)),font=font, fill="black")
                    elif str(a[i][j]) == "+":
                        draw.text((50 + x,50 + y),str(char(186)),font=font, fill="black")
                    else:
                        draw.text((50 + x,50 + y)," ",font=font, fill="black")
                x += 50
            y += 50
            x = 0

        image.save("resources/Imagen"+ str(paso) +".png")
        self.nombres.append("resources/Imagen"+str(paso)+".png")

    def crearGif(self):
        for i in range(len(self.nombres)):
            self.images.append(imageio.imread(self.nombres[i]))

        imageio.mimsave('resources/movie.gif',self.images, duration=0.5, subrectangles=True)

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
