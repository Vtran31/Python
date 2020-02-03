import pygame
import os
from grid import Grip   #the other python file that I create
import socket   # for tcp protocol 
import threading


#set where windows will be when open 
os.environ['SDL_VIDEO_WINDOW_POS'] = '900, 100'


surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe-Client')

################################ SETUP THREADING ####################################################

#Threading in python is used to run multiple threads (tasks, function calls) at the same time. 
# Note that this does not mean that they are executed on different CPUs. 
# Python threads will NOT make your program faster if it already uses 100 % CPU time. 
# In that case, you probably want to look into parallel programming
# Python threads are used in cases where the execution of a task involves some waiting. 
# One example would be interaction with a service hosted on another computer, such as a webserver. 
# Threading allows python to execute other code while waiting; this is easily simulated with the sleep function.
def create_thread(target):
    thread = threading.Thread(target= target)
    thread.daemon = True
    thread.start()
    
################################ END THREADING SETUP ################################################


################################ USING SOCKET TO CREATE CONNECTION TO SERVER - START ##########################

#set host, port number 
#visit https://realpython.com/python-sockets/ for more information 
HOST = '127.0.0.1'    #standar loopback interface host 
PORT = 65432          #port to listen on (non-privileged ports are > 1023)
connected = False     #check the status is connected
conn, addr = None, None

#The arguments passed to socket() specify the address family and socket type.
#  AF_INET is the Internet address family for IPv4. 
# SOCK_STREAM is the socket type for TCP, 
# the protocol that will be used to transport our messages in the network.
soc_ket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server 
soc_ket.connect((HOST, PORT))

def receive_data():
    while True:
        data = soc_ket.recv(1024).decode()
        print(data)
        

################################ USING SOCKET TO CREATE CONNECTION TO SERVER - STOP ##########################

#define grip viraible ( same as CDDrawr grip = new CDDrawer)
grip = Grip()
running = True
player = 'x'

create_thread(target= receive_data)

while running :
    

    #detect keyboard press
    for event in pygame.event.get():
        
        #detect x quit icon is click 
        if event.type == pygame.QUIT:
            running = False
            
         #detect mouse click    
        if event.type == pygame.MOUSEBUTTONDOWN and not grip.game_over:
            print('Mouse click!')
            
            if pygame.mouse.get_pressed()[0]:      #detect left mouse was click 
                print(pygame.mouse.get_pressed())  #print what button was press on mouse
                    
                #get position where mouse click 
                pos = pygame.mouse.get_pos()
                print(f'Mouse click at: {pos}')
                print(f'Cell coor at : ({pos[0] // 200}, {pos[1]//200})') #devident of 2 int -> get cell position 
                
                 #set x or o to grid 
                grip.get_mouse(pos[0] // 200, pos[1] // 200, player)
                
                ########################### SEND DATA TO CLIENT - START ##########################
                x, y = pos[0]//200, pos[1] // 200
                
                #create data, and encode it 
                send_data = f'{x}-{y}'.encode()
                
                #use conn to send data
                #conn.send(send_data)
                
                
                ########################### SEND DATA TO CLIENT - STOP ##########################
                
                #print the grid 
                grip.print_grid()
                
                #check for winner 
                grip.check_grip(pos[0] // 200, pos[1] // 200, player)
                
                #change the player 
                if grip.switch_player == True:
                    if player == 'x' :
                        player = 'o'
                    elif player == 'o':
                        player = 'x'
                       
                #print if the player is press inside the player area
                print(grip.is_in_bound(pos[0] // 200, pos[1] // 200))
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grip.game_over:
                grip.clear_grip()
            if event.key == pygame.K_ESCAPE:
                running = False
               
    #fill background         
    surface.fill((0,0,0))
    
    #draw the grip line from grid.py file 
    grip.draw(surface)
    
    pygame.display.flip()
    
    