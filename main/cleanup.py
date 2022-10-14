def cleanem():
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)

    print(">>>>>Cleanin up")
    GPIO.cleanup()
