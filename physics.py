import math
from vector2 import *  


class MassPoint:

    def __init__(self, R = Vector2(0, 0), m = 1, g = 0):

        self.p = 0.1
        self.m = m
        self.r = ((self.m * 3) / (self.p * 4 * math.pi))**(1/3)
        if self.r >= 25:
            
            self.r = 25

        self.R = R
        self.V = Vector2(0, 0)
        self.A = Vector2(0, 0)
        self.F = Vector2(0, 0)
        self.nextF = Vector2(0, 0)
        self.g = g

    
    def SimulateStep(self, dt):

        self.AddForce(Vector2(0, -1) * self.g * self.m)
        
        self.F = self.nextF
        self.A = self.F / self.m
        self.V = self.V + self.A * dt
        self.R = self.R + self.V * dt

        self.nextF = Vector2(0, 0)


    def AddForce(self, F):

        self.nextF = self.nextF + F



class SpringJoint:

    def __init__(self, point1, point2, xn, k = 1, damp = 0):

        self.point1 = point1
        self.point2 = point2
        self.xn = xn
        self.k = k
        self.damp = damp


    def CalculateForce(self):
        
        #Spring force using Hooke's law
        self.x = (self.point1.R - self.point2.R).mod
        self.Fmod = (self.x - self.xn) * self.k

        self.p1F = (self.point2.R - self.point1.R).unit() * self.Fmod
        self.p2F = (self.point1.R - self.point2.R).unit() * self.Fmod
        self.point1.AddForce(self.p1F)
        self.point2.AddForce(self.p2F)


        #Damp force
        Vrel = self.point1.V - self.point2.V
        D = self.point2.R - self.point1.R
        DampMod = (Vrel * D) * self.damp / D.mod

        p1Damp = D.unit() * (-DampMod)
        p2Damp = D.unit() * DampMod
        self.point1.AddForce(p1Damp)
        self.point2.AddForce(p2Damp)



class System:
    def __init__(self):

        self.MassPointDic = {}
        self.SpringJointDic = {}

    
    def AddMassPoint(self, name, R = Vector2(0, 0), m = 1, g = 0):

        self.MassPointDic[name] = MassPoint(R, m, g)
        

    def AddSpringJoint(self, name, point1, point2, xn, k = 1, damp = 0):

        self.SpringJointDic[name] = SpringJoint(self.MassPointDic[point1], self.MassPointDic[point2], xn, k, damp)


    def AddString(self, name, PointN, R1, R2, m, k, damp, g):

        step = (R2 - R1) / PointN

        for i in range(PointN + 1):

            self.MassPointDic[name + "point" + str(i + 1)] = MassPoint(R1 + step * i, m, g)

        for i in range(1, PointN + 1):

            point1 = self.MassPointDic[name + "point" + str(i)]
            point2 = self.MassPointDic[name + "point" + str(i + 1)]
            self.SpringJointDic[name + "spring" + str(i)] = SpringJoint(point1, point2, step.mod, k, damp)


    def SimulateStep(self, dt):

        for SJ in self.SpringJointDic.values():

            SJ.CalculateForce()


        for MP in self.MassPointDic.values():

            MP.SimulateStep(dt)


    def GetEnergy(self):

        Ek = 0
        Epe = 0

        for MP in self.MassPointDic.values():

            Ek = Ek + ((MP.V.mod)**2 * MP.m) / 2

        for SJ in self.SpringJointDic.values():

            x = (SJ.point1.R - SJ.point2.R).mod
            Epe = Epe + x**2 * 2
            
        




