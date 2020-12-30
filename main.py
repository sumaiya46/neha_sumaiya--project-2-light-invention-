while True:
    print("Light Level:" + input.light_level())
    if input.light_level()<= 5:
        light.set_all (light.rgb(0, 0, 255))
    elif input.light_level()> 15: 
        light.clear ()
    else:
        light.set_all (light.rgb(127, 0, 255))

#If light level is greater than 15 the LEDs will be clear
#If light level is less than or equal to 5 then LEDs will be blue
#If light level is neither (less than or equal to 5 and greater than 15) then LEDs will be purple 