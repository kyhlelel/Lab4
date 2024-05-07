import hal.hal_input_switch as switch
import hal.hal_led as led
import time
from time import sleep

switch.init()
led.init()
count = 0 

while True:
    if switch.read_slide_switch()==1:
        led.set_output(24,1)
        time.sleep(0.1)
        led.set_output(24,0)
        time.sleep(0.1)
    else:
        count +=1
        led.set_output(24,1)
        time.sleep(0,2)
        led.set_output(24,0)
        time.sleep(0.2)
        if count > 50:
            led.set_output(24,0)
            quit()
            

        
            
            
        
        



        
        
        
    
    
