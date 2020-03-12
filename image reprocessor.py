import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import numpy
from math import sqrt
#import csv
mc = minecraft.Minecraft.create()
#mc.setBlock(x,y,z,id,meta)
file = open('colors.csv', 'r') 
im = Image.open('tomc.png').convert('RGB')
pix = im.load()
#pix[x,y]
width, height = im.size
class ess :
    r=0
    g=0
    b=0
col=file.readlines()
dis=99999999999999
chs=0
#print(col)
print(pix[10,10])
afct=0
print(len(col))
for x in range(0,width):
    for y in range(0,height) :
        dis=99999999999999
        for i in range(0,len(col)) :
            ess.r=float(col[i].split(',')[1])
            ess.g=float(col[i].split(',')[2])
            ess.b=float(col[i].split(',')[3])
            #print(pix[x,y])
            #print(sqrt((pix[x,y][0]-ess.r)**2+(pix[x,y][1]-ess.g)**2+(pix[x,y][2]-ess.b)**2))
            
            if sqrt((pix[x,y][0]-ess.r)**2+(pix[x,y][1]-ess.g)**2+(pix[x,y][2]-ess.b)**2) < dis :
                dis = sqrt((pix[x,y][0]-ess.r)**2+(pix[x,y][1]-ess.g)**2+(pix[x,y][2]-ess.b)**2)
                chs=i
        #print("-----",str(col[chs].split(',')[5]))
        mc.setBlock(x,10,y,int(str(col[chs].split(',')[4])),int(str(col[chs].split(',')[5])))
        afct+=1
        print(afct/(width*height)*100)
#sqrt[(Xa-Xb)²+(Ya-Yb)²+(Za-Zb)²]