# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:55:48 2017

@author: Haijie Zuo
"""

#A bezier can do the job, ideally accompanied by an adiabacity criterion on the rate of change, rather than minimum bend radius only.
#Yes, you can implement it yourself as a "patch", i.e. create a polygon and make it into an element:

import nazca as nd
import numpy as np
import matplotlib.pyplot as plt
nd.strt(length=1000,width=20).put()
#nd.bend(angle=90,radius=500).put()

#xout=1;
#yout=2;
#aout=3;

#l = []



        
def bezier(a=0, b=0, c=0,p0_x=0,p0_y=0,length=2000,width=5000,orientation=-1):
    """Create a Bezier waveguide based on parameters a, b and c."""
    with nd.Cell(name='Bezier') as bez:
        t=np.arange(0,1,0.001);
        width=width*orientation;
        p1_x=p0_x+length;
        p1_y=p0_y;
        p2_x=p1_x;
        p2_y=p1_y-width;
        p3_x=p0_x;
        p3_y=p0_y-width;
        
        x=p0_x*(1-t)**3+3*p1_x*t*(1-t)**2+3*p2_x*t*t*(1-t)+p3_x*t**3;
        y=p0_y*(1-t)**3+3*p1_y*t*(1-t)**2+3*p2_y*t*t*(1-t)+p3_y*t**3;        

        #l = list(product(x, y))
        #mylist = [[0,1],  [0,2],  [0,2],  [0,5]];
        x1=np.array([x]) ;
        y1=np.array([y]) ;
        x2=x1.T;
        y2=y1.T;
        bezier_curve=np.hstack((x2,y2));
        #bezier_curve = [(0, 0), (3, 3), (500, 500),(500, 900)] # Bezier waveguide outline
        #nd.Polygon(layer=1,points=bezier_curve ).put(0)
        nd.Polyline(layer=0,points=bezier_curve,width=50).put(0)
            #add pins to the input and output, pointing outwards of the bezier guide         
        nd.Pin('a0').put(0, 0, 180) #if bezier starts in (0, 0, 0)
#        nd.Pin('b0').put(xout, yout, aout)
        nd.strt(length=100, width=100).put(p0_x, p0_y)
        nd.strt(length=100, width=100).put(p1_x, p1_y)
        nd.strt(length=100, width=100).put(p2_x, p2_y)
        nd.strt(length=100, width=100).put(p3_x, p3_y)
        
        width_x=(p1_x+p2_x)/2
        width_y=(p1_y+p2_y)/2
        nd.text('width', height=250, align='cc', layer=2).put(width_x, width_y)
        
        length_x=(p0_x+p1_x)/2
        length_y=(p0_y+p1_y)/2
        nd.text('length', height=250, align='cc', layer=2).put(length_x, length_y)


    return bez
  
bezier(a=0).put()


#nd.strt(length=10000,width=60).put()
#To create a Beizer curve between two pins say p1 and p2, you first want to get the distance:

#dx, dy, da = nd.diff(p1, p2)

#You can send p1 and p2 to your bezier function and define your bezier_curve (outline) with them.

#def bezier(pin1, pin2, a=0, b=0, c=0):
#     dx, dy, da = nd.diff(pin1, pin2)
#     #etc.
#
#Be sure to add enough polygon points to obtain the grid resolution of your intended mask.
nd.export_gds()