class Vector2:
    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y
        self.mod = (x**2 + y**2)**(1/2)

    
    def __add__(self, other):

        result = Vector2(self.x + other.x, self.y + other.y)
        return(result)
    
    
    def __sub__(self, other):

        result = Vector2(self.x - other.x, self.y - other.y)
        return(result)
    
    
    def __mul__(self, other):

        if type(other) is Vector2:
            result = self.x * other.x + self.y + other.y
        
        else:
            result = Vector2(self.x * other, self.y * other)

        return(result)
    

    def __truediv__(self, other):

        result = Vector2(self.x / other, self.y / other)
        return(result)
    

    def unit(self):

        if self.mod != 0:
            result = self / self.mod

        else:
            result = Vector2(0, 1)

        return(result)
    
    def normal(self):

        result = Vector2(-self.y, self.x)
        return(result)
    
    def PygameVectorToVector2(PygameVector):
        
        result = Vector2(PygameVector[0], PygameVector[1])
        return(result)