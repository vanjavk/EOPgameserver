import socket
import time
from _thread import *
import math
class object(object):
    def __init__(self,x=0,y=0,idd=0,metadata=0):
        self.x=x
        self.y=y
        self.idd=idd
        self.metadata=metadata
projs=list()
speed=9
class projectile(object):
    def __init__(self,name,x=0,y=0,xs=0,ys=0):
        self.name=name
        self.x=x
        self.y=y
        self.xs=xs
        self.ys=ys
def calcspeed(x1,y1,x2,y2):
    lenx=x2-(x1+20)
    leny=y2-(y1+20)
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
def calcdirx(rot):
    return (math.cos(math.radians(rot)))
def calcdiry(rot):
    return (math.sin(math.radians(rot)))
#print(calcdir(300))
#print(calcspeed(0,0,0,0))
class player(object):
    def __init__(self,name,x=0,y=0,xs=0,ys=0,timeout=time.time(),firing=0,lastfire=0,score=0):
        self.name=name
        self.x=x
        self.y=y
        self.firing=firing
        self.lastfire=lastfire
        self.xs=xs
        self.ys=ys
        self.timeout=timeout
        self.score=score
    def info(self):
        return self.name,self.x,self.y,self.xs,self.ys,self.timeout

            
p=dict()
pstr=""
# A UDP server

# Set up a UDP server
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Listen on port 21567
# (to all IP addresses on this system)
listen_addr = ('51.38.112.120',5555)
UDPSock.bind(listen_addr)

# Report on all data packets received and
# where they came from in each case (as this is
# UDP, each may be from a different source and it's
# up to the server to sort this out!)
def threaded_sender(UDPSock,pstr,addr):
    UDPSock.sendto(pstr.encode("utf-8"),addr)
    
def threaded_client(UDPSock):
    global pstr
    global p
    while True:
        #time2=time.time()
        
        data,addr = UDPSock.recvfrom(4096)
        if data:
            pd=data.decode("utf-8").split("|")
            #print(pd,"\n number of projectiles:{0}".format(len(projs)))
            if pd[0]=="EXIT":
                p.pop(pd[1])
                #break
            else:
                if pd[0] in p.keys():
                    p.update({pd[0]:player(name=pd[0],x=int(pd[1]),y=int(pd[2]),firing=int(pd[3]),xs=int(pd[4]),ys=int(pd[5]),timeout=int(time.time()),lastfire=p[pd[0]].lastfire,score=p[pd[0]].score)})
                else:
                    p.update({pd[0]:player(name=pd[0],x=int(pd[1]),y=int(pd[2]),firing=int(pd[3]),xs=int(pd[4]),ys=int(pd[5]),timeout=int(time.time()))})              
            start_new_thread(threaded_sender,(UDPSock,pstr,addr))
            #UDPSock.sendto(pstr,addr)
            
        #while time.time()-time2<1/60:
            #print("Looper too fast")

start_new_thread(threaded_client,(UDPSock,))
while True:
    #time1=time.time()
    #start_new_thread(threaded_client,(UDPSock,))
    #print("--------------------------------------")
    #print (addr,data.decode("utf-8").split("|"))
    #print(p)
    #print("Clients connected:",len(p))
    time.sleep(1/70)

    #for i in projs:
    
    pstrtemp=""
    
    try:
        if len(p)>0:
            for i in p.keys():
                if int(p[i].firing)==1:
                    if time.time()-p[i].lastfire>0.8:
                        projs.append(projectile(name=i,x=p[i].x+20,y=p[i].y+20,xs=calcdirx(calcspeed(p[i].x,p[i].y,p[i].xs,p[i].ys)),ys=calcdiry(calcspeed(p[i].x,p[i].y,p[i].xs,p[i].ys))))
                        print(i,"fired a bullet from",p[i].x,p[i].y,"to",p[i].xs,p[i].ys)
                        p[i].lastfire=time.time()
    except RuntimeError:
        print("A U PM")
    removelist=list()
    for i in projs:
        i.x+=i.xs*speed
        i.y+=i.ys*speed
        if i.x>800 or i.x<0 or i.y>600 or i.y<0:
            removelist.append(projs.index(i))
        for kl in p.keys():
            if i.name!=kl:
                if float(i.x)>float(p[kl].x) and float(i.x)<float(p[kl].x)+40:
                    if i.y>p[kl].y and i.y<p[kl].y+40:
                        p[i.name].score+=1
                        
                        p[kl].score-=1
                        
                        print(i.name,"killed",kl+". Score:", p[kl].score)
                        removelist.append(projs.index(i))
                        
    for j in removelist[::-1]:
        try:
            
            projs.pop(j)
        except:
            pass
    #print(projs)
    try:
        if len(p)>0:
            for i in p.keys():
                if int(time.time())-p[i].timeout>10:
                    print(i,"TIMED OUT")
                    p.pop(i)
                else:
                    pstrtemp+=p[i].name+"|"+str(p[i].x)+"|"+str(p[i].y)+"|"+str(p[i].score)+"|"+str(p[i].ys)+"|"+str(p[i].timeout)+"|"
                    #print(p[i].info())
                #x=1
            #pstrtemp+=","
            for i in projs:
                pstrtemp+=str(round(i.x,5))+","+str(round(i.y,5))+","+str(round(i.xs,5))+","+str(round(i.ys,5))+","
            pstrtemp=pstrtemp[:-1]
                #x=1
        else:
            print('zzz')
    except RuntimeError:
        pstrtemp="ERROR"
        if len(p)==0:
            print("LAST PLAYER DISCONNECTED")
        else:
            print("PLAYER (DIS)CONNECTED")
    #except TypeError:
            #print("WRONG TIME??? OR AN EMPTY SERVER")
    if pstrtemp!="ERROR":
        pstr=pstrtemp
    #while time.time()-time1<1/60:
        #print("Loop too fast")
    #xoox=time.time()-time1
    #print(xoox)
    

    
