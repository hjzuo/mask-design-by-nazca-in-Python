# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:58:43 2018

@author: Haijie Zuo
"""
# dose test

import nazca as nd

l=45000;
r=2000;
ua=180; "$upperward angle"
da=-180; "$downward angle"
pitch=50;
wafer=25.4*4*1000
w=2.3;  "wg width"
pos_y = 0;

nd.bend(angle=360,radius=25.4*1000*2,width=w).put(25.4*1000*2,-25.4*1000*2)






# dose 600mj/cm2
n = 0
while n<10:
    nd.strt(length=25.4*2*1000,width=w).put(25.4*1000,25.4*1000+n*50)
    n = n + 1
nd.text('600',height=2000).put()    

# dose 800mj/cm2
    
n = 0
while n<10:
    nd.strt(length=25.4*2*1000,width=w).put(25.4*1000,n*50-10*1000)
    n = n + 1
nd.text('XL',height=5000).put(48000, 20000)    


# dose 1000mj/cm2


n = 0
while n<10:
    nd.strt(length=25.4*2*1000,width=w).put(25.4*1000,n*50-20*1000)
    n = n + 1
nd.text('XL',height=5000).put(48000, 20000)

# dose 1200mj/cm2


n = 0
while n<10:
    nd.strt(length=25.4*2*1000,width=w).put(25.4*1000,n*50-30*1000)
    n = n + 1
nd.text('XL',height=5000).put(48000, 20000)
# dose 1400mj/cm2


n = 0
while n<10:
    nd.strt(length=25.4*2*1000,width=w).put(25.4*1000,n*50-40*1000)
    n = n + 1
nd.text('XL',height=5000).put(48000, 20000)    
# dose 1400mj/cm2


n = 0
while n<10:
    nd.strt(length=25.4*2*1000,width=w).put(25.4*1000,n*50-30*1000)
    n = n + 1
nd.text('XL',height=5000).put(48000, 20000)










nd.export_gds(filename='dose_test.gds')