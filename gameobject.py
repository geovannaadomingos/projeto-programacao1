import gamemanager


class GameObject():
    all_objects = []

    def __init__(self, v2_spawnPos, v2_size, clickable=False):
        self.v2_pos = v2_spawnPos
        self.v2_size = v2_size * gamemanager.GameManager.scale
        self.clickable = clickable

        GameObject.all_objects.append(self)
    
    def isPointInside(self, v2_point):
        if self.v2_pos.x <= v2_point.x <= self.v2_pos.x + self.v2_size.x:
                if self.v2_pos.y <= v2_point.y <= self.v2_pos.y + self.v2_size.y:
                    return True
        return False

    def getCenterPos(self):
        return self.v2_pos + (self.v2_size/2.0)

    def draw(self, screen):
        pass

    def loop(self):
        pass