import module

servo2 = module.get(module.SERVO2)

servo2.release(0)
servo2.position(0, 0)
servo2.position(0, 180)


servo2.release(1)
servo2.position(1, 0)
servo2.position(1, 180)