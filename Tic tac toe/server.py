import pygame
import os
from grid import Grip   #the other python file that I create
import socket   # for tcp protocol 
import threading


#set where windows will be when open 
os.environ['SDL_VIDEO_WINDOW_POS'] = '900, 100'


surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe')

#define grip viraible ( same as CDDrawr grip = new CDDrawer)
grip = Grip()
running = True
player = 'x'

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

################################ USING SOCKET TO CREATE CONNECTION - START ##########################

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

#2nd step is blind socket
soc_ket.bind((HOST, PORT))

#3th step is begin to listen
#if we have more than 2 client -> change in number 1 -> number of client  
soc_ket.listen(1)

def receive_data():
    while True:
        data = conn.recv(1024).decode()
        print(data)

def waiting_for_connection():
    global conn, addr, connected
    #accept() blocks and waits for an incoming connection. 
    # When a client connects, it returns a new socket object 
    # representing the connection and a tuple holding the address of the client. 
    # The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6. 
    # See Socket Address Families in the reference section for details on the tuple values.
    conn, addr = soc_ket.accept()
    
    #after confirm connection from client print connected
    print("Client is connect")
    connected = True
    
    #call receive_data after client is connected
    
    
#4th step is waiting for connection from client 
#also create threat to waiting for connection 

######## IMPORTANCE TO KNOW ##################
#Without create threading funtion, the game will stop to wating for connect
# by create this the game now have 2 thread : 1 is wating for connection , and 1 is continute to displat the game 
create_thread(waiting_for_connection)
    

################################USING SOCKET TO CREATE CONNECTION -END ##########################

while running :
    #detect keyboard press
    for event in pygame.event.get():
        
        #detect x quit icon is click 
        if event.type == pygame.QUIT:
            running = False
            
         #detect mouse click    
        if event.type == pygame.MOUSEBUTTONDOWN and connected:
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
                conn.send(send_data)
                receive_data()
                
                
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
    
    