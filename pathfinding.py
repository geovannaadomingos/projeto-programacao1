import pygame
from pygame.locals import *

BLACK = (0,0,0) #barreiras
WHITE = (255,255,255) #grade originalmente
GRAY = (128, 128, 128) #linhas da grade
TURQUOISE = (64, 224, 208) #ponto inicial
YELLOW = (255, 255, 0) #ponto final
BLUE = (0, 0, 255) #caminho

class Grid():
    
    def __init__(self, length, height, cube_size):
        self.length = length #comprimento
        self.height = height #altura
        self.cube_size = cube_size #tamanho do cubo
        self.qtd_cube_height = height // cube_size #quantidade do cubo na altura
        self.qtd_cube_length = length // cube_size #quantidade do cubo no comprimento
        self.matrix = [] # cada linha vai ser uma lista que vai conter as colunas

        for row in range(self.qtd_cube_height):
            row_list = []
            for column in range(self.qtd_cube_length):
                row_list.append(Cube(column, row, WHITE))
            self.matrix.append(row_list)
    
    def draw(self, screen):
        img = pygame.Surface((self.cube_size, self.cube_size))
        
        for row in range(self.qtd_cube_height):
            for column in range(self.qtd_cube_length):
                cube = self.matrix[row][column]
                img.fill(cube.state)
                screen.blit(img, (cube.x * self.cube_size, cube.y * self.cube_size))
        
        self.draw_grid(screen, 2)
    
    def draw_grid(self, screen, espessura_row):
        for row in range(self.qtd_cube_height):
            pygame.draw.line(screen, GRAY, (0, row * self.cube_size), (self.length, row*self.cube_size), espessura_row) #linhas horizontais
        
        for column in range(self.qtd_cube_length):
            pygame.draw.line(screen, GRAY, (column * self.cube_size, 0), (column*self.cube_size, self.height), espessura_row) #linhas verticais

    def get_screen_cube_pos(self, mouse_pos): #pegando posição do mouse na tela; mouse_pos = (100, 100) x: 100, y: 100
        grid_pos_x = mouse_pos[0] // self.cube_size
        grid_pos_y = mouse_pos[1] // self.cube_size

        return self.matrix[grid_pos_y][grid_pos_x]

    def neighbors(self, cube):
        neighbors_list = []

        if cube.x + 1 < self.qtd_cube_length:
            neighbors_list.append(self.matrix[cube.y][cube.x+1]) #vizinho da direita
        if cube.x - 1 >= 0:
            neighbors_list.append(self.matrix[cube.y][cube.x-1]) #vizinho da esquerda
        if cube.y + 1 < self.qtd_cube_height:
            neighbors_list.append(self.matrix[cube.y+1][cube.x]) #vizinho de cima
        if cube.y - 1 >= 0:
            neighbors_list.append(self.matrix[cube.y-1][cube.x]) #vizinho de baixo
        
        return neighbors_list
    
    def find_cube_color(self, color):
        for row in self.matrix:
            for cube in row:
                if cube.state == color:
                    return cube
        return None

class Cube():
    
    def __init__(self, x, y, state):
        self.state = state
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.parent = None
    
    #g = distancia do cubo até o cubo_inicial(partida)
    #h = distancia do cubo até o cubo_final(destino)
    #f = g + h
    
    def valor_f(self):
        return self.g + self.h

class Pathfinding():

    def find_distance(cube1, cube2):
        distanceX = abs(cube1.x - cube2.x)
        distanceY = abs(cube1.y - cube2.y)

        return 10*(distanceX+distanceY)
    
    def retrace_path(cube_start, cube_end): #Refazendo o caminho
        path = []
        current_cube = cube_end
        
        while current_cube != None: #current_cube = None seria o cube_start (já que não tem pai/parente)
            path.append(current_cube)
            current_cube = current_cube.parent
        
        return path[::-1] #inverte o caminho; cubo_final, ...., cubo_inicial


    def get_path(cube_start, cube_end, grid): #encontrar o caminho
        list_open_cubes = [] #cubos que vamos analisar
        list_closed_cubes = [] #cubos que já foram analisados

        list_open_cubes.append(cube_start)
        
        #Zerar os valores de g, h da grid
        for row in grid.matrix:
            for cube in row:
                cube.h = 0
                cube.g = 0
                cube.parent = None
        
        while len(list_open_cubes) > 0:
            current_cube = list_open_cubes[0]

            for cube in list_open_cubes:
                if cube.valor_f() < current_cube.valor_f() or (cube.valor_f() == current_cube.valor_f() and cube.h < current_cube.h):
                    current_cube = cube
            
            list_open_cubes.remove(current_cube)
            list_closed_cubes.append(current_cube)

            if current_cube == cube_end:
                return Pathfinding.retrace_path(cube_start, cube_end)
            
            for neighborCube in grid.neighbors(current_cube):
                if neighborCube.state == BLACK or neighborCube in list_closed_cubes:
                    continue
                
                movement_cost = current_cube.g + Pathfinding.find_distance(current_cube, neighborCube) #se for diagonal, mas quando n for sempre vai ser 10
                if movement_cost < neighborCube.g or neighborCube not in list_open_cubes:
                    neighborCube.g = movement_cost
                    neighborCube.h = Pathfinding.find_distance(neighborCube, cube_end)
                    neighborCube.parent = current_cube
                    
                    if neighborCube not in list_open_cubes:
                        list_open_cubes.append(neighborCube)
        return []

if __name__ == "__main__":
    grade = Grid(600, 600, 60)

    SCREEN_LENGTH = 600
    SCREEN_HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pathfinding')

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(10) # FPS
        screen.fill(BLACK)
        events = pygame.event.get() # pegar os eventos 
        
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[2]: #click direito = obstaculos
            mouse_cube =  grade.get_screen_cube_pos(mouse_pos) #cubo sob o mouse
            mouse_cube.state = BLACK
        elif pygame.mouse.get_pressed()[0]: #click esquerdo = ponto inicial; dois clicks esquerdo = ponto final
            mouse_cube = grade.get_screen_cube_pos(mouse_pos)
            if mouse_cube.state == TURQUOISE:
                mouse_cube.state = YELLOW
            else:
                mouse_cube.state = TURQUOISE

        for event in events:
            if event.type == KEYDOWN:
                if(event.key == K_SPACE):
                    cube_start = grade.find_cube_color(TURQUOISE)
                    cube_end = grade.find_cube_color(YELLOW)
                    path = Pathfinding.get_path(cube_start, cube_end, grade) #lista de cubinhos

                    for cube in path:
                        cube.state = BLUE

        grade.draw(screen)
        pygame.display.update()