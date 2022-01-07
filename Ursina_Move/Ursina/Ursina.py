from ursina import *
from random import randint

def update():
    
    for obj in objectList:
        obj.x += randint(-1, 1) * 3 * time.dt
        obj.y += randint(-1, 1) * 3 * time.dt
    return

app = Ursina()

objectList = []

for i in range(0,5):
    objectList.append(Entity(model = 'cube', position = (randint(-2, 2), randint(-2, 2), 0.0), scale = 0.2))

cube = Entity(model = 'cube', color = color.azure, position = (randint(-3, 3), randint(-3, 3), 0.0), scale = 0.2)

app.run()