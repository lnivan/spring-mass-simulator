from draw import *
from physics import *
from UI import *
import pygame
import time


WindowSize = (800, 800)
window = Window(WindowSize)


class FPSCounter:

    def __init__(self):

        self.start = time.time()
        self.end = 0
        self.FPS = 0


    def Update(self):

        self.end = time.time()
        self.FPS = 1 / (self.end - self.start + 0.00001)
        self.start = time.time()


fps = FPSCounter()
        




sistem = System()




'''sistem.AddMassPoint("point1", Vector2(300, 300), 100)
sistem.AddMassPoint("point2", Vector2(500, 300), 100)
sistem.AddMassPoint("point3", Vector2(500, 500), 100)
sistem.AddMassPoint("point4", Vector2(300, 500), 100)
sistem.AddSpringJoint("spring1", "point1", "point2", 300, 10000)
sistem.AddSpringJoint("spring2", "point2", "point3", 300, 1000)
sistem.AddSpringJoint("spring3", "point3", "point4", 300, 1000)
sistem.AddSpringJoint("spring4", "point4", "point1", 300, 1000)
'''

'''sistem.AddMassPoint("point1", Vector2(400, 700), 10000, -30)
sistem.AddMassPoint("point2", Vector2(350, 700), 50, 1000)
sistem.AddMassPoint("point3", Vector2(300, 700), 50, 1000)
sistem.AddMassPoint("point4", Vector2(250, 700), 50, 1000)
sistem.AddMassPoint("point5", Vector2(200, 700), 50, 1000)
sistem.AddMassPoint("point6", Vector2(150, 700), 50, 1000)
sistem.AddMassPoint("point7", Vector2(100, 700), 50, 1000)
sistem.AddSpringJoint("spring1", "point1", "point2", 50, 10000)
sistem.AddSpringJoint("spring2", "point2", "point3", 50, 10000)
sistem.AddSpringJoint("spring3", "point3", "point4", 50, 10000)
sistem.AddSpringJoint("spring4", "point4", "point5", 50, 10000)
sistem.AddSpringJoint("spring5", "point5", "point6", 50, 10000)
sistem.AddSpringJoint("spring6", "point6", "point7", 50, 10000)'''










sistem.AddMassPoint("point1", Vector2(80, 400), 10000000, 0)
sistem.AddMassPoint("point2", Vector2(720, 400), 10000000, 0)

string1 = sistem.AddString("string1", 50, Vector2(100, 400), Vector2(700, 400), 0.1, 2000, 20, 1000)

sistem.AddSpringJoint("spring1", "point1", "string1point1", 20, 3000)
sistem.AddSpringJoint("spring2", "string1point51", "point2", 20, 3000)



'''g = 1000

sistem.AddMassPoint("point1", Vector2(100, 700), 10000000, 0)
sistem.AddMassPoint("point2", Vector2(100, 550), 10000000, 0)
sistem.AddMassPoint("point3", Vector2(250, 700), 10, g)
sistem.AddMassPoint("point4", Vector2(250, 550), 10, g)
sistem.AddMassPoint("point5", Vector2(400, 700), 10, g)
sistem.AddMassPoint("point6", Vector2(400, 550), 10, g)
sistem.AddMassPoint("point7", Vector2(550, 700), 10, g)
sistem.AddMassPoint("point8", Vector2(550, 550), 10, g)
sistem.AddMassPoint("point9", Vector2(700, 700), 10, g)
sistem.AddMassPoint("point10", Vector2(700, 550), 10, g)

k = 1000
damp = 100

sistem.AddSpringJoint("spring1", "point1", "point3", 150, k, damp)
sistem.AddSpringJoint("spring2", "point3", "point5", 150, k, damp)
sistem.AddSpringJoint("spring3", "point5", "point7", 150, k, damp)
sistem.AddSpringJoint("spring4", "point7", "point9", 150, k, damp)

sistem.AddSpringJoint("spring5", "point2", "point4", 150, k, damp)
sistem.AddSpringJoint("spring6", "point4", "point6", 150, k, damp)
sistem.AddSpringJoint("spring7", "point6", "point8", 150, k, damp)
sistem.AddSpringJoint("spring8", "point8", "point10", 150, k, damp)

sistem.AddSpringJoint("spring9", "point3", "point4", 150, k, damp)
sistem.AddSpringJoint("spring10", "point5", "point6", 150, k, damp)
sistem.AddSpringJoint("spring11", "point7", "point8", 150, k, damp)
sistem.AddSpringJoint("spring12", "point9", "point10", 150, k, damp)

sistem.AddSpringJoint("spring13", "point1", "point4", 150 * 2**(1/2), k, damp)
sistem.AddSpringJoint("spring14", "point3", "point6", 150 * 2**(1/2), k, damp)
sistem.AddSpringJoint("spring15", "point5", "point8", 150 * 2**(1/2), k, damp)
sistem.AddSpringJoint("spring16", "point7", "point10", 150 * 2**(1/2), k, damp)

sistem.AddSpringJoint("spring17", "point2", "point3", 150 * 2**(1/2), k, damp)
sistem.AddSpringJoint("spring18", "point4", "point5", 150 * 2**(1/2), k, damp)
sistem.AddSpringJoint("spring19", "point6", "point7", 150 * 2**(1/2), k, damp)
sistem.AddSpringJoint("spring20", "point8", "point9", 150 * 2**(1/2), k, damp)
'''







button1 = Button("pause", Vector2(680, 750), Vector2(100, 30), print, WindowSize)
button2 = Button("point", Vector2(680, 710), Vector2(100, 30), print, WindowSize)
button3 = Button("spring", Vector2(680, 670), Vector2(100, 30), print, WindowSize)







'''point1 = sistem.AddMassPoint("point1", Vector2(400, 100), 10, 0)
point2 = sistem.AddMassPoint("point2", Vector2(400, 700), 10, 0)
sistem.AddSpringJoint("spring1", "point1", "point2", 200, 100, 1000)'''











'''sistem.AddMassPoint("point1", Vector2(400, 700), 10000000, 0)
sistem.AddString("string1", 30, Vector2(400, 40), Vector2(700, 400), 0.1, 3000, 20,1000)'''

#sistem.AddMassPoint("point5", Vector2(500, 700), 100, 1000)




running = True
while running == True:

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:

            running = False


    sistem.SimulateStep(0.0005)
    button1.Update(events)
    button2.Update(events)
    button3.Update(events)

    window.WindowRefresh()
    window.DrawSystem(sistem)
    window.DrawButton(button1)
    window.DrawButton(button2)
    window.DrawButton(button3)
    pygame.display.flip()


   # fps.Update()
    #print(fps.FPS)