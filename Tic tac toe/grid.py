import pygame
from pygame import color
import os

letter_x = pygame.image.load(os.path.join('res', 'letter_x.png'))
letter_0 = pygame.image.load(os.path.join('res', 'letter_o.png'))

class Grip:
    
    def __init__(self) :
        
        self.grip_line = [((0, 200), (600, 200)),   #1st horizontal line
                          ((0, 400), (600, 400)),   #2ns horizontal line
                          ((200, 0), (200, 600)),   #1st vertical line
                          ((400, 0), (400, 600))]   #2nd vertical line
        
        self.grid = [[0 for x in range (3)] for y in range (3)]
        
        self.switch_player = True
        
        #search direction around the current input 
        #direction                  NE       E       SE      S        SW       W         NW       N
        self.search_direction = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
        
        self. game_over = False

            
    def print_grid(self):
        for row in self.grid :
            print(row)
            
            
    def get_cell_value(self, x, y):
        return self.grid[y][x]
    
    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value
        
    #set 'x' pr 'o' to position in grid 
    def get_mouse(self, x, y, player):
        if self.get_cell_value(x, y) == 0:
            self.switch_player = True
            if player == 'x' :
                self.set_cell_value(x, y, 'x')
            elif player == 'o':
                self.set_cell_value(x, y, 'o')
        else:
            self.switch_player = False        
    
            
    def draw(self, surface):
        
        #draw the line for game
        for lines in self.grip_line:
            pygame.draw.line(surface, (200,200,200), lines[0], lines[1], 2)
            
        #draw the 'x' and 'o' everytime player press
        for y in range( len(self.grid)):
            for x in range (len(self.grid[y])):
                #check if the cell is empty before input 
                if self.get_cell_value(x, y) == 'x':
                    surface.blit(letter_x, (x*200, y*200))
                elif self.get_cell_value(x, y) == 'o':
                    surface.blit(letter_0, (x*200, y*200))
        
    #check when check around cell is in playing area             
    def is_in_bound(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y <3
   
    def is_grip_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False 
        return True               
   
    #check for winner 
    #check around the current cell x, y coord
    def check_grip(self, x, y, player) :
        
        #for loop go to each of the direction to check 
        #reset count to 1 when move to the new direction 
        for (dir_x, dir_y) in (self.search_direction):
            count = 1
            #move to the next cell in current direction
            xx = x + dir_x
            yy = y + dir_y
            
            #while loop to continute to check on that direction 
            while self.is_in_bound(xx, yy) and player == self.get_cell_value(xx, yy):
                count += 1
                xx += dir_x
                yy += dir_y
            
            #after checking everthing in current direction then if count = 3, current player win 
            if count == 3:
                print(f'Player : {player} win' )
                self.game_over = True
                break
            
            elif self.is_grip_full() == True:
                self.game_over = True
    
    def clear_grip(self):
        self.grid = [[0 for x in range (3)] for y in range (3)]
        self.game_over = False