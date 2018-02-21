# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nazca as nd

l=45000;
r=2000;
ua=180; "$upperward angle"
da=-180; "$downward angle"
pitch=200;
wafer=25.4*4*1000
w=2.3;  "wg width"

nd.strt(length=l,width=w).put(0,16000)
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l*1.2,width=w).put()

nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l*1.5,width=w).put()


l2=35000
nd.strt(length=l*0.9,width=w).put(0,15000-16000-500+1000)
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l2/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l2/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l2/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l2*1.2,width=w).put()
#nd.bend(angle=ua,radius=r).put()

nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l2/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l2/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l2/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l*1.5,width=w).put()



l3=25000
nd.strt(length=l*0.75,width=w).put(0,15000-16000-pitch*14)
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l3/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l3/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l3/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l3*1.2,width=w).put()

nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l3/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l3/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l3/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l*1.5,width=w).put()


l4=15000
nd.strt(length=l*1.4,width=w).put(0,15000-16000-pitch*15-8*r)
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4*1.4,width=w).put()

nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l*1.5,width=w).put()

l4=5000
nd.strt(length=l*1.6,width=w).put(0,16000-200)
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4*1.9,width=w).put()

nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=ua,radius=r,width=w).put()
nd.strt(length=l4/2,width=w).put()
nd.bend(angle=da,radius=r,width=w).put()
nd.strt(length=l*1.5,width=w).put()



pitch2=15
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*1)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*2)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*3)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*4)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*5)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*6)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*7)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*8)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*9)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*10)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*11)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*12)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*13)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*14)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*15)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*16)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*17)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*18)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*19)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*20)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*21)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*22)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*23)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*24)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch2*25)

#alignment mark
nd.geometries.circle(radius=5000)

nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*5)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*6)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*7)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*8)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*9)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*10)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*11)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*12)
nd.strt(length=l*2.5,width=w).put(0,15000-16000-pitch*13)



nd.strt(length=l*1.1,width=w).put(0,15000-16000-pitch*16-8*r)
nd.bend(angle=da,radius=10000,width=w).put()
nd.bend(angle=da,radius=10000-2*pitch,width=w).put()
nd.bend(angle=da,radius=10000-4*pitch,width=w).put()
nd.bend(angle=da,radius=10000-6*pitch,width=w).put()
nd.bend(angle=da,radius=10000-8*pitch,width=w).put()
nd.bend(angle=da,radius=10000-10*pitch,width=w).put()
nd.bend(angle=da,radius=10000-12*pitch,width=w).put()

nd.bend(angle=da,radius=5000-6.5*pitch,width=w).put()#(10000-12*pitch-pitch）/2
nd.bend(angle=ua,radius=5000-6.5*pitch,width=w).put()

nd.bend(angle=ua,radius=10000-12*pitch,width=w).put()
nd.bend(angle=ua,radius=10000-10*pitch,width=w).put()
nd.bend(angle=ua,radius=10000-8*pitch,width=w).put()
nd.bend(angle=ua,radius=10000-6*pitch,width=w).put()
nd.bend(angle=ua,radius=10000-4*pitch,width=w).put()
nd.bend(angle=ua,radius=10000-2*pitch,width=w).put()
nd.bend(angle=ua,radius=10000,width=w).put()
nd.bend(angle=ua*0.5,radius=10000+2*pitch,width=w).put()
nd.bend(angle=da*0.5,radius=10000,width=w).put()
nd.strt(length=l,width=w).put()
#nd.bend(angle=da,radius=((10000-12*pitch)/2).put()
#nd.bend(angle=da,radius=((10000-12*pitch-pitch)/2).put()
#nd.bend(angle=ua,radius=((10000-12*pitch-pitch)/2).put()


#cleave mark
nd.strt(length=300,width=8000).put(0,0)
nd.strt(length=300,width=8000).put(25.4*4*1000-5000,0)

nd.strt(length=300,width=15000).put(15000,15000/2)
nd.strt(length=300,width=15000).put(wafer-15000,15000/2)
#nd.text('15000',height=500).put(wafer-15000, 0)
#nd.text('wafer-15000',height=500).put(15000, 0)
nd.strt(length=300,width=15000).put(15000,-15000/2-4500)
nd.strt(length=300,width=15000).put(wafer-15000,-15000/2-4500)

#nd.text('XL',height=5000).put(48000, 20000)
#nd.text('L',height=5000).put(43000, 3000)
#nd.text('M',height=4000).put(35000, -12500)
#nd.text('S',height=4000).put(65500, -9000)
#nd.text('XS',height=4000).put(73000, 7400)
#


nd.bend(angle=360,radius=25.4*1000*2,layer=2,width=w).put(25.4*1000*2,-25.4*1000*2)


nd.export_gds()
