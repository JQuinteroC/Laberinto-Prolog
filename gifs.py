from PIL import Image, ImageDraw, ImageFont
import imageio

class gif():
    def __init__(self):
        self.a = [[0,2,3],[4,5,6],[7,8,9]]
        self.nombres = []
        self.images = []
        
        self.crearImagen(self.a,2)
        self.a = [[1,0,3],[4,5,6],[7,8,9]]
        self.crearImagen(self.a,3)
        self.a = [[1,2,0],[4,5,6],[7,8,9]]
        self.crearImagen(self.a,4)
        self.a = [[1,2,3],[0,5,6],[7,8,9]]
        self.crearImagen(self.a,5)
        self.a = [[1,2,3],[4,0,6],[7,8,9]]
        self.crearImagen(self.a,6)
        self.a = [[1,2,3],[4,5,0],[7,8,9]]
        self.crearImagen(self.a,7)
        self.a = [[1,2,3],[4,5,6],[0,8,9]]
        self.crearImagen(self.a,8)
        self.a = [[1,2,3],[4,5,8],[7,0,9]]

        self.crearGif()
    
    def crearImagen(self,a,paso):
        x = 0
        y = 0
    
        image = Image.open("resources/Imagen1.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf",20)

        for i in range(len(a)):
            for j in range(len(a[i])):
                draw.text((50 + x,50 + y),str(a[i][j]),font=font, fill="black")
                x += 100
            y += 100
            x = 0

        image.save("resources/Imagen"+ str(paso) +".png")
        self.nombres.append("resources/Imagen"+str(paso)+".png")

    def crearGif(self):
        for i in range(len(self.nombres)):
            self.images.append(imageio.imread(self.nombres[i]))

        imageio.mimsave('resources/movie.gif',self.images)

def main():
    gif()
    return 0

if __name__ == '__main__':
    main()
