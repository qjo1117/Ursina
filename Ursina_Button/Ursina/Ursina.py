from ursina import *

def update():
    
    return

def ButtonCommand(type):
    cube.texture = 'Sample' + str(type) + '.png'

app = Ursina()

button1 = Button(icon = 'A.png', scale = 0.2, x = -0.5)
button2 = Button(icon = 'B.png', scale = 0.2, x = 0.0)
button3 = Button(icon = 'C.png', scale = 0.2, x = 0.5)

cube = Entity(model = 'cube', texture = 'Sample1.png', y = 1.5)

button1.on_click = Func(ButtonCommand, 1)
button2.on_click = Func(ButtonCommand, 2)
button3.on_click = Func(ButtonCommand, 3)

app.run()