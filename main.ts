while (true) {
    console.log("Light Level:" + input.lightLevel())
    if (input.lightLevel() <= 5) {
        light.setAll(light.rgb(0, 0, 255))
    } else if (input.lightLevel() > 15) {
        light.clear()
    } else {
        light.setAll(light.rgb(127, 0, 255))
    }
    
}
