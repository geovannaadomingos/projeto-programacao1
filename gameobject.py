from vector2 import Vector2

class GameObject():
    all_objects = []

    def __init__(self, v2_pos, v2_size, clickable=False):
        self.v2_pos = v2_pos
        self.v2_size = v2_size
        self.clickable = clickable
        self.v2_collideOffset = Vector2(0,0)
        self.v2_collideBox = self.v2_size

        GameObject.all_objects.append(self)
    
    def isPointInside(self, v2_point):
        if self.v2_pos.x <= v2_point.x < (self.v2_pos.x + self.v2_size.x):
                if self.v2_pos.y <= v2_point.y < (self.v2_pos.y + self.v2_size.y):
                    return True
        return False

    def getCenterPos(self):
        return self.v2_pos + (self.v2_size/2.0)

    def isCollide(self, gameObject):
        if (self.v2_pos.x + self.v2_collideOffset.x) <= (gameObject.v2_pos.x + gameObject.v2_collideOffset.x) <= (self.v2_pos.x + self.v2_collideOffset.x) + self.v2_collideBox.x or (gameObject.v2_pos.x + gameObject.v2_collideOffset.x) <= (self.v2_pos.x + self.v2_collideOffset.x) <= (gameObject.v2_pos.x + gameObject.v2_collideOffset.x) + gameObject.v2_collideBox.x:
            if (self.v2_pos.y + self.v2_collideOffset.y) <= (gameObject.v2_pos.y + gameObject.v2_collideOffset.y) <= (self.v2_pos.y + self.v2_collideOffset.y) + self.v2_collideBox.y or (gameObject.v2_pos.y + gameObject.v2_collideOffset.y) <= (self.v2_pos.y + self.v2_collideOffset.y) <= (gameObject.v2_pos.y + gameObject.v2_collideOffset.y) + gameObject.v2_collideBox.y:
                return True
        return False

    def draw(self, screen):
        pass

    def loop(self):
        pass