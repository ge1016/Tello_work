#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tellopy
from time import sleep


drone=tellopy.Tello()
drone.connect()
drone.wait_for_connection(20)
drone.takeoff()
sleep(5)
#move:
#  drone.up(val)
#  drone.down(val)
#  drone.set_throttle(thr_val): -1~1(neg: down, pos: up )

#  drone.forward(val)
#  drone.backward(val)
#  drone.set_pitch(pit_val): -1~1(neg: back, pos: for )

#  drone.right(val)
#  drone.left(val)
#  drone.set_roll(rol_val): -1~1(neg: left, pos: right )
#rotate:
#  drone.clockwise(val)#順時針
#  drone.counter_clockwise(val)#逆時針
#  drone.set_yaw(yaw_val): -1~1(neg: left, pos: right )

#drone.forward(20)
#sleep(7)
#drone.backward(10)
#sleep(7)
#drone.right(10)
#sleep(7)
#drone.left(10)
#sleep(7)
#drone.flip_right()
#drone.flip_backleft()
#sleep(7)


drone.flip_forward()#翻轉
sleep(7)

drone.forward(20)#前進20
sleep(7)

drone.right(20)#向右20
sleep(7)

drone.up(20)#向上20
sleep(7)

drone.down(20)#向下20
sleep(7)



drone.clockwise(90)#順時針旋轉但是不會停
sleep(5)
drone.clockwise(0)
sleep(5)
drone.down(20)
sleep(5)
drone.forward(20)
sleep(5)

drone.clockwise(90)
sleep(5)
drone.clockwise(0)
sleep(5)
drone.up(20)
sleep(5)
drone.forward(20)
sleep(5)

drone.clockwise(90)
sleep(5)
drone.clockwise(0)
sleep(5)
drone.down(20)
sleep(5)
drone.forward(20)
sleep(5)

drone.clockwise(90)
sleep(5)
drone.clockwise(0)
sleep(5)
drone.up(20)
sleep(5)
drone.forward(20)
sleep(5)

#sleep(5)
#drone.clockwise(90)
#sleep(5)
#drone.forward(20)
#sleep(5)
#drone.clockwise(90)
#sleep(5)
#drone.forward(20)
#sleep(5)


#drone.up(20)
#sleep(7)
#drone.down(20)
#sleep(7)
drone.flip_forward()#翻轉
sleep(7)

drone.land()
sleep(3)

drone.quit()






