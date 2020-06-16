import cairo, os, random, math
from PIL import Image, ImageDraw


list_of_colors = [(0,0,0), (255,255,255), (95, 78, 105),
    (152, 32, 32), (81, 102, 141), (81, 138, 141), (164, 138, 141), (75, 198, 251), 
    (255, 176, 165), (155,50,200), (100,100,100), (89, 130, 129), (190, 79, 86)]


def draw_background(cr, r, g, b, width, height):
    cr.set_source_rgba(r, g, b)
    cr.rectangle(0,0, width, height)
    cr.fill()



def main(width, height, orbit, boardersize, sunsize, noise):

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    cr = cairo.Context(ims)
    draw_background(cr, 0.3, 0.3, 0.3, width, height)
    draw_background(cr, 0.2, 0.7 ,0.7, width, height/2)
    

    ims.write_to_png('Generative-Space-Example.png')


class Object(Physical):

    def __init__(self, name, typeobject = "box", width, height):
        self.name = name
        self.width = width
        self.height = height
        if not typeobject == "box" or typeobject == "circle":
            raise ValueError("Shape is not included in object")
        else:
            self.typeobject = typeobject
        

        ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        source = cairo.Context(ims)


    
    def drawobject(self, source, typeobject):
        source.set_source_rgba(0.5, 0.8, 0.1)
        if typeobject == "circle":
            source.cricle()
        

        for 





    






if __name__ ==  '__main__':
    orbit = 500 #input("Input orbit type: ")
    width = 500 #int(input("Input width: "))
    height = 500 #int(input("Height: "))
    sunsize = 100#int(input("Sunsize: "))
    boardersize = 100 #int(input("Boardersize: "))
    noise = 100 #int(input("Noise: "))
    
    main(width, height, orbit, boardersize, sunsize, noise)