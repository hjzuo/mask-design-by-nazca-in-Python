# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:37:27 2017

@author: Haijie Zuo
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nazca as nd

l=20000;
r=2000;
ua=90; "$upperward angle"
da=-90; "$downward angle"
l_strt=0;
l_bend=0;



nd.strt(length=l).put(0,10000);l_strt=l_strt+l;
nd.bend(angle=da,radius=r).put();l_bend=l_bend+3.1415*2*r/4;

nd.strt(length=l).put();l_strt=l_strt+l;
nd.strt(length=l).put();l_strt=l_strt+l;

nd.bend(angle=ua,radius=r).put();l_bend=l_bend+3.1415*2*r/4;
nd.strt(length=l).put();l_strt=l_strt+l;
nd.strt(length=l).put();l_strt=l_strt+l;

nd.bend(angle=ua,radius=r).put();l_bend=l_bend+3.1415*2*r/4;
nd.strt(length=l).put();l_strt=l_strt+l;
nd.strt(length=l).put();l_strt=l_strt+l;

nd.bend(angle=360,radius=25.4*1000*2,layer=2).put(25.4*1000*2,-25.4*1000*2)

nd.export_gds()
print('length of straight part ', l_strt, ' and length of bend part', l_bend)