#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)

# GPIO connected to the power switch
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# GPIO connected to the power LED
GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)

GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
