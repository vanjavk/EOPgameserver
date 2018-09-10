import pymysql.cursors
from tkinter import Button,Entry,Label,Tk,StringVar,Frame,IntVar,Checkbutton
import operator
import re
import pygame
import os
import os.path
import sys
import time
import ipgetter
from _thread import *
from tkinter.messagebox import showerror,showinfo
import socket
blocksize=40
psx=blocksize
import math
import bcrypt
import requests
from Cryptodome.Cipher import AES
opcije=""
aeskey = b'vanjavk6jepropro'
remuser=""
rempassword=""
speed=3
psy=blocksize*2
p=dict()
p1=dict()
p2=dict()
mouseclicked,mousex,mousey=0,0,0
ps=pygame.sprite.Group()
cmapdata=list()
class NullDevice():
    def write(self, s):
        pass
#image_resources = "C:/python34/imgs/"
t=Tk()
remember=IntVar()
feg=True
while feg==True:
    try:
        SERVER=socket.gethostbyname('eopgame.vanjavk.me')
        print("SERVER",SERVER)
        feg=False
    except Exception as e:
        showerror(title="Error!",message="ERROR WITH CONNECTION!\n"+str(e))
#print("MYIP",ipgetter.myip())
#print(SERVER)
if ipgetter.myip()==SERVER:
    IP="192.168.5.17"
    #print("LOKALNI")
else:
    IP=SERVER
    sys.stdout = NullDevice()

    """
feg=True

while feg==True:
    try:
        connection = pymysql.connect(host='eop.yugocraft.com',
                                     user='HqdpRxT6a',
                                     password='SvzjsjJb2',
                                     db='eopusersgame',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        feg=False 
    except Exception as e:
        showerror(title="Error!",message="Unable to connect to MYSQL server. Retrying...")
"""
        
#print(connection)
#print("test")
#
class NullDevice():
    def write(self, s):
        pass
original_stdout = sys.stdout
#sys.stdout = NullDevice()

class object(object):
    def __init__(self,x=0,y=0,idd=0,metadata=0):
        self.x=x
        self.y=y
        self.idd=idd
        self.metadata=metadata
projlist=list()
class projectile(pygame.sprite.Sprite):
    def __init__(self,image,name,x=0,y=0,direction=0):
        self.name=name
        self.direction=direction
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
class player(pygame.sprite.Sprite):
    def __init__(self,image,name,x=0,y=0,xs=0,ys=0):
        self.name=name
        self.xs=xs
        self.ys=ys
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

def loadlevel():
    global cmapdata
    filedata1 = open("level.txt", "r")
    filedata2=filedata1.read().split("\n")
    filedata3=list()
    for i in filedata2:
        filedata3.append(list(map(int,i.split(","))))
    return filedata3
    
def drawlevel(cmapdata,gameDisplay):
    global blocksize
    #print(cmapdata)
    for y in range(len(cmapdata)):
        for x in range(len(cmapdata[0])):
            #print(x,y)
            if cmapdata[y][x]==0:
                #pygame.draw.rect(gameDisplay,(255,0,0),[x*blocksize,y*blocksize,blocksize,blocksize])
                gameDisplay.fill((255,0,0),rect=[x*blocksize,y*blocksize,blocksize,blocksize])
            elif cmapdata[y][x]==1:
                gameDisplay.fill((5,5,5),rect=[x*blocksize,y*blocksize,blocksize,blocksize])
def calcspeed(lenx,leny):
    #print(lenx,leny)
    if lenx==0:
        if leny>0:
            return 90
        else:
            return 270
    if leny==0:
        if lenx>0:
            return 0
        else:
            return 180
    else: 
        omj=leny/lenx
        if lenx>0 and leny>0:
            return math.degrees(math.atan(leny/lenx))
        if lenx>0 and leny<0:
            return 360+math.degrees(math.atan(leny/lenx))
        if lenx<0 and leny<0:
            return 180+math.degrees(math.atan(leny/lenx))
        if lenx<0 and leny>0:
            return 180+math.degrees(math.atan(leny/lenx))
#def threaded_client1(UDPSock,username):
    #return
nekidict=dict()
myscore="0"
def threaded_client(UDPSock,username):
    #print("jaar")
    global projlist
    global nekidict
    global p1
    projlisttemp=list()
    #print("NEW THREAD STARTED")
    while True:
        
        time2=time.time()
        try:
            
            ptemp=dict()
            nekidicttemp=dict()
            #print("NEW THREAD STARTED")
            dr, server = UDPSock.recvfrom(4096)
            if dr:
                
                dr=dr.decode("utf-8").split("|")
                #print("FUCKING SUCCESS!!!!!!!!!!!!!!!!")
                #print("Connected clients:",str(len(dr)//6))
                #print(dr)
                
                if len(dr)>0:
                    for i in range(len(dr)//6):
                        if dr[i*6]!=username:
                            ptemp.update({dr[i*6]:player(name=dr[i*6],x=int(dr[i*6+1]),y=int(dr[i*6+2]),xs=int(dr[i*6+3]),ys=int(dr[i*6+4]),image="player1.png")})
                        else:
                            nekidicttemp.update({dr[i*6]:player(name=dr[i*6],x=int(dr[i*6+1]),y=int(dr[i*6+2]),xs=int(dr[i*6+3]),ys=int(dr[i*6+4]),image="player1.png")})
                            global myscore
                            myscore=dr[i*6+3]
                            #print(myscore)
                        #print(dr[i*6],dr[i*6+1],dr[i*6+2],dr[i*6+3],dr[i*6+4],dr[i*6+5])
                    dr1=dr[-1].split(",")
                    #print(dr1)
                    projlisttemp=list()
                    for j in range(len(dr1)//4):
                        #print("u")#,direction=int(calcspeed(float(dr1[j*4+2]),float(dr1[j*4]+3)))
                        projlisttemp.append(projectile(name="unknown",x=float(dr1[j*4]),y=float(dr1[j*4+1]),image="proj.png"))
                        #print("he")
                        
                
        except Exception as e:
            #time.sleep(0.05)
            #print("ERROR====",e)
            #print(e)
            ptemp="ERROR"
            projlisttemp="ERROR"
        if ptemp!="ERROR":
            p1=ptemp.copy()
            nekidict=nekidicttemp.copy()
        if projlisttemp!="ERROR":
            
            projlist=projlisttemp[:]
            #print(p1)
            #for i in p1.keys():
                #print (p1[i].x)
        #while time.time()-time2<1/70:
            #print("Looper too fast")



# render text


def startgame(username):
    global myscore
    global p
    global p1
    global p2
    global blocksize
    global psx
    global psy
    global p
    global mouseclicked
    global mousex
    global mousey
    global nekidict
    
    clock=pygame.time.Clock()
    
    EOP=pygame.init()
    
    #print("I'M ABOUT TO LOAD MYFONT")
    try:
        myfont= pygame.font.Font('freesansbold.ttf',30)
        
        #myfont = pygame.font.Font(None, 30)
    except:
        print("ERROR FONT")
        pass
    #print("I SUCCEED")
    gameDisplay=pygame.display.set_mode((800,600))
    
    right,left,up,down=False,False,False,False
    
    p.update({username:player(name=username,x=380,y=280,image="player.png")})
    #print(p)
    white=(255,255,255)
    red=(255,0,0)
    black=(0,0,0)
    pygame.display.set_caption("EOP")
    gameExit=False
    #pygame.display.flip(
    pygame.display.update()
    
   
    UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    global IP
    addr = (IP,5555)
    start_new_thread(threaded_client,(UDPSock,username))
    #poruka=str(random.randint(1,500))
    #print("randint je", poruka)
    #print(s.recv(2048).decode('utf-8'))
    #s.send(poruka.encode('utf-8'))
    #input()
    #print(s.recv(2048).decode('utf-8'))
    #####cmapdata=loadlevel()
    while not gameExit:
        
        ###drawlevel(cmapdata,gameDisplay)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouseclicked=1
                    mousex,mousey=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0]==False:
                    mouseclicked=0
            
            if event.type == pygame.QUIT:
                gameExit=True
##                if event.key==pygame.K_RIGHT:
##                    right=True
##                    p[username].xs  =speed
##                if event.key==pygame.K_UP:
##                    up=True
##                    p[username].xs =speed
##                if event.key==pygame.K_DOWN:
##                    down=True
##                    p[username].xs=-speed
            #if event.type== pygame.KEYDOWN:
        mousez= pygame.mouse.get_pressed()
        keyz = pygame.key.get_pressed()
        #print(keyz)
        if mousez[0]:
            mouseclicked=1
            mousex,mousey=pygame.mouse.get_pos()
        else:
            mouseclicked=0
            
        if keyz[pygame.K_LEFT] or keyz[pygame.K_a]:
            left=True
            p[username].xs =-speed
        else:
            left=False
        if keyz[pygame.K_RIGHT] or keyz[pygame.K_d]:
            right=True
            p[username].xs =speed
        else:
            right=False
        if keyz[pygame.K_UP] or keyz[pygame.K_w]:
            up=True
            p[username].xs =-speed
        else:
            up=False
        if keyz[pygame.K_DOWN] or keyz[pygame.K_s]:
            down=True
            p[username].xs =speed
        else:
            down=False
                
                    
##            if event.type== pygame.KEYUP:
##                if event.key==pygame.K_LEFT:
##                    left=False
##                    #print("left",left)
##                if event.key==pygame.K_RIGHT:
##                    right=False
##                    #print("right",right)
##                if event.key==pygame.K_UP:
##                    up=False
##                if event.key==pygame.K_DOWN:
##                    down=False



        if left==right:
            p[username].xs=0
        elif left==True:
            p[username].xs=-speed
        else:
            p[username].xs=speed
        #print(up,down,left,right)
        if up==down:
            
            p[username].ys=0
        elif up==True:
            p[username].ys=-speed
        else:
            p[username].ys=speed
        
##        p[username].rect.x +=p[username].xs
##        if cmapdata[math.floor((p[username].rect.y+blocksize*2)/blocksize)][math.floor((p[username].rect.x+blocksize/2)/blocksize)]==0:
##            p[username].ys=1
##        else:
##            p[username].ys=0
        #print(p[username].rect.x,p[username].rect.y)
        if p[username].rect.x+p[username].xs>0 and p[username].rect.x+p[username].xs<760:
            #print(p[username].rect.x+p[username].xs)
            p[username].rect.x +=p[username].xs 
        if p[username].rect.y+p[username].ys>0 and p[username].rect.y+p[username].ys<560:
            p[username].rect.y +=p[username].ys 
        gameDisplay.fill((200,200,200))
        p5=p1.copy()
        p5.update(nekidict)
        stringara=""
        xerox=0
        if len(p2)>0:
            for student in (sorted(p5.values(), key=operator.attrgetter('xs'))):
                stringara=str(student.name)+" | "+str(student.xs)+" "
                label = myfont.render(stringara, 2, (244,244,244),(5,5,5))
                gameDisplay.blit(label, (0, xerox))
                xerox+=14
        
        
        #pygame.draw.rect(gameDisplay,black,[p[username].rect.x+psx/2,p[username].rect.y+psy/2,2,2])
        #gameDisplay.fill(red,rect=[200,200,50,50])
        p2=p1.copy()
        #if len(p2)>0:
        #    for i in p2.keys():
                #print("i",i,"p2[i]",p2[i],"p2[i].x",p2[i].x)
        #        pygame.draw.rect(gameDisplay,black,[int(p2[i].x),int(p2[i].y),10,10])
        ps=pygame.sprite.Group()
        projsp=pygame.sprite.Group()
        projlist1=projlist[:]
        global myscore
        try:
            myscore1=myscore
        except:
            pass
        
        ps.add(p[username])
        ps.draw(gameDisplay)
        #print(myscore1)
        
        if len(projlist1)>0:
            #print(projlist1)
            #print("huraj")
            for i in projlist1:
                #print(i)
                projsp.add(i)
                projsp.draw(gameDisplay)
                projsp=pygame.sprite.Group()
        if len(p2)>0:
            #print("huraj")
            for i in p2.keys():
                
                ps.add(p2[i])
                
                label = myfont.render(str(p2[i].xs), 2, (244,244,244),(5,5,5))
            
                ps.draw(gameDisplay)
                ps=pygame.sprite.Group()
                
                gameDisplay.blit(label, (int(p2[i].rect.x)+20-label.get_rect().width/2, int(p2[i].rect.y)+20-label.get_rect().height/2))
        #print(len(p2))
        #label = myfont.render("Some text!", 1, (255,255,0))  
        #gameDisplay.blit(label, (300,300))
        label = myfont.render(str(myscore1), 2, (244,244,244),(5,5,5))
        gameDisplay.blit(label, (int(p[username].rect.x)+20-label.get_rect().width/2, int(p[username].rect.y)+20-label.get_rect().height/2))
        if len(p2)==0:
            gameDisplay.fill((200,200,200))
            label = myfont.render("Waiting for other players", 2, (244,244,244),(5,5,5))
            gameDisplay.blit(label, (400, 300))
        
        
        pygame.display.update()
        #print(p[username].rect.x,p[username].rect.y)
        #print(len(projlist1))
        datatosend=username+"|"+str(p[username].rect.x)+"|"+str(p[username].rect.y)+"|"+str(mouseclicked)+"|"+str(mousex)+"|"+str(mousey)
        UDPSock.sendto(datatosend.encode("utf-8"),addr)
        
        

                           
        
        clock.tick(60)
    UDPSock.sendto("EXIT|{0}".format(username).encode("utf-8"),addr)
    print("EXIT|{0}".format(username))
    pygame.quit()
    quit()


def checkvalidemail(email):
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return True
    else:
        return False
def checkvalidusername(username):
    if re.match(r"^[a-zA-Z0-9]*$", username):
        return True
    else:
        return False
def checkvalidpassword(password):
    if re.match(r"^[a-zA-Z0-9]*$", password):
        return True
    else:
        return False
    
def checkusernameindb(username):
    try:
        response=requests.post("https://eopgame.vanjavk.me/checkusernameindb.php", data={'username': username})
        print (response.text)
        if response.json()['result']==1:
            return True
        elif response.json()['result']==0:
            return False
        else:
            showerror(title="Error!",message="ERROR WITH RESPONSE!")
            return True
        """
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `email`, `password` FROM `eopusersgame` WHERE `username`=%s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            #print(result)
            if result!=None:
                return True
            else:
                return False
        """
    except:
        print("checkusernameindb")
        showerror(title="Error!",message="ERROR WITH CONNECTION!")
        return True
def checkemailindb(email):
    try:
        response=requests.post("https://eopgame.vanjavk.me/checkemailindb.php", data={'email': email})
        if response.json()['result']==1:
            return True
        elif response.json()['result']==0:
            return False
        else:
            showerror(title="Error!",message="ERROR WITH RESPONSE!")
            return True
        """
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `username`, `password` FROM `eopusersgame` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            #print(result)
            if result!=None:
                return True
            else:
                return False
        """
    except:
        print("checkemailindb")
        showerror(title="Error!",message="ERROR WITH CONNECTION!")
        return True
def getpassword(username):
    try:

        response=requests.post("https://eopgame.vanjavk.me/getpassword.php", data={'username': username})
        if response.text=='false':
            showerror(title="Error!",message="ERROR WITH RESPONSE!")
            return None
        else:
            return response.json()['password']
        """
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `password` FROM `eopusersgame` WHERE `username`=%s"
            cursor.execute(sql, (username))
            result = str(cursor.fetchone()).split("'")
            print(result,"getpassword")
            return result[3]
        """
    except Exception as e:
        return None
        print("getpassword",e)
        showerror(title="Error!",message="ERROR WITH CONNECTION!")
def checkpassword(username,password):
    try:
        response=requests.post("https://eopgame.vanjavk.me/checkpassword.php", data={'username': username,'password': password})
        if response.json()['result']==0:
            #showerror(title="Error!", message="WRONG PASSWORD!")
            return False
        elif response.json()['result']==1:
            return True
        else:
            #showerror(title="Error!", message="ERROR WITH RESPONSE!")
            return False
        """
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `password` FROM `eopusersgame` WHERE `username`=%s"
            cursor.execute(sql, (username))
            result = str(cursor.fetchone()).split("'")
            print(result,"getpassword")
            return result[3]
        """
    except Exception as e:
        return None
        print("getpassword",e)
        showerror(title="Error!",message="ERROR WITH CONNECTION!")
def adduserindb(username,email,password):
    try:

        response=requests.post("https://eopgame.vanjavk.me/adduserindb.php", data={'username': username, 'email': email,'password': password})
        if response.json()['result']==0:
            showerror(title="Error!",message="ERROR WITH RESPONSE!")
        elif response.json()['result']==1:
            showinfo(title="Information",message="SUCCESSFULLY REGISTERED!")
        else:
            showerror(title="Error!",message="ERROR WITH RESPONSE!")


            
        """
        with connection.cursor() as cursor:
            sql = "INSERT INTO `eopusersgame` (`username`, `email`, `password`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, email, password))
            connection.commit()
            showinfo(title="Information",message="SUCCESSFULLY REGISTERED!")
        """
    except Exception as e:
        print("adduserindb",e)
        showerror(title="Error!",message="ERROR WITH CONNECTION!")
def register():

    username=str(e1.get())
    email=str(e2.get())
    password=str(e3.get())
    if len(username)<6 or len(email)<5 or len(password)<6:
        showerror(title="Error!",message="TOO SHORT!")
    else:
        if checkvalidusername(username):
            if checkvalidemail(email):
                if checkvalidpassword(password):
                    if checkusernameindb(username)==True:
                        showerror(title="Error!",message="USERNAME IS TAKEN!")
                    else:
                        if checkemailindb(email):
                            showerror(title="Error!",message="EMAIL IS TAKEN!")
                        else:
                            adduserindb(username,email,password)
                else:
                    showerror(title="Error!",message="INVALID PASSWORD! (Use only a-z,A-Z,0-9)") 
            else:
                showerror(title="Error!",message="INVALID EMAIL!")
        else:
            showerror(title="Error!",message="INVALID USERNAME! (Use only a-z,A-Z,0-9)")

                
        
    
    #pygame.quit()
def login():
    username=str(e4.get())
    password=str(e5.get())
    if remember.get()==1:
        opcijes="1|"+username+"|"+password+"|"
        text=opcijes.encode("utf-8")
        elen = len(text) % 16
        if elen:
            text += bytes(16 - elen)
        global aeskey
        encryption_suite = AES.new(aeskey, AES.MODE_CBC, b'vj83SDUAIkw92KAd')
        cipher_text = encryption_suite.encrypt(text)
        open('settings.bin', 'wb').write(cipher_text)
    else:
        try:
            os.remove('settings.bin')
        except:
            pass
            
    if len(username)<6 or len(password)<6:
        showerror(title="Error!",message="TOO SHORT!")
    else:
        if checkvalidusername(username):
            if checkvalidpassword(password):
                if checkusernameindb(username):
                    if checkpassword(username,password)==True:
                        #showinfo(title="Information",message="SUCCESSFULLY LOGGED IN!")
                        t.destroy()
                        
                        startgame(username)
                        
                    else:
                        showerror(title="Error!",message="INVALID PASSWORD&USERNAME COMBINATION!")
                else:
                    showerror(title="Error!",message="USERNAME DOES NOT EXIST!")
            else:
                showerror(title="Error!",message="INVALID PASSWORD! (Use only a-z,A-Z,0-9)") 
        else:
            showerror(title="Error!",message="INVALID USERNAME! (Use only a-z,A-Z,0-9)")

#if os.path.exists("C:\\EOP"):
if os.path.isfile("settings.bin")==True:
    try:
        cipher_text=open('settings.bin', 'rb').read()
        decryption_suite = AES.new(aeskey, AES.MODE_CBC, b'vj83SDUAIkw92KAd')
        plain_text = decryption_suite.decrypt(cipher_text).decode('utf-8')
        opcije=plain_text.split("|")
    except Exception as e:
        print(e)
        opcije="0|||".split("|")
    
else:
    opcije="0|||".split("|")
#else:
#    os.makedirs("C:\\EOP")
#    opcije="0||".split("|")
    



t.title('EOP')
t.config(bg='green',width = 300,height = 600)

c1=Checkbutton(t,text="Remember me",variable=remember,bg='lightblue',activebackground="blue")
c1.place(x=105,y=450)
if opcije[0]=="1":
    c1.select()

l1=Label(t,text="REGISTER TO EOP",font=("Verdana",18),bg='pink')
l1.place(x=40,y=1)

l2=Label(t,text="USERNAME:",bg='pink')
l2.place(x=5,y=50)
l3=Label(t,text="E-MAIL:",bg='pink')
l3.place(x=5,y=100)
l4=Label(t,text="PASSWORD:",bg='pink')
l4.place(x=5,y=150)
e1=Entry(t,textvariable=StringVar(t, value=''))
e1.place(x=80,y=51)
e2=Entry(t,textvariable=StringVar(t, value=''))
e2.place(x=80,y=101)
e3=Entry(t,show="*",textvariable=StringVar(t, value=''))
e3.place(x=80,y=151)
b1=Button(text="REGISTER",font=("Verdana",15), command=register,bg='pink')
b1.place(x=100,y=200)
#----------------------------------------------------------
l5=Label(t,text="LOGIN TO EOP",font=("Verdana",18),bg='yellow')
l5.place(x=60,y=300)

l6=Label(t,text="USERNAME:",bg='yellow')
l6.place(x=5,y=350)
l7=Label(t,text="PASSWORD:",bg='yellow')
l7.place(x=5,y=400)
e4=Entry(t,textvariable=StringVar(t, value=opcije[1]))
e4.place(x=80,y=351)
e5=Entry(t,textvariable=StringVar(t, value=opcije[2]),show="*")
e5.place(x=80,y=401)
b2=Button(text="LOGIN",font=("Verdana",15), command=login,bg='yellow')
b2.place(x=115,y=500)



#login()
t.mainloop()



# Connect to the database

#print(connection)



