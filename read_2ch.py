#!/usr/bin/env python
#coding=utf-8
# Read the analog sensor value via MCP3002.
#http://tekitoh-memdhoi.info/views/745

import spidev
import time
import subprocess

spi = spidev.SpiDev()
spi.open(0, 0)
# Settings (for example)
#spi.max_speed_hz = 10000

try:
    while True:
        # ch0
        resp = spi.xfer2([0x68, 0x00])
        value_ch1 = ((resp[0] << 8) + resp[1]) & 0x3ff
        time.sleep(1)
        # ch1
        resp = spi.xfer2([0x78, 0x00])
        value_ch2 = ((resp[0] << 8) + resp[1]) & 0x3ff
        print "Ch1 Voltage=" + str(value_ch1) + "/"+ str(round((value_ch1 / 38.75),3)),"Ch2 Voltage=" + str(value_ch2) + "/"+ str(round((value_ch2 / 38.75),3))

        time.sleep(5)
except KeyboardInterrupt:
    spi.close()