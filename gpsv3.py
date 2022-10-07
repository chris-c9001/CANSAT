import board
import busio
import adafruit_gps

# initialise communication, create gps object, and enable whole gps chip
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=30)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b"PMTK220,1000")

def getLocation():
    gps.update()
    if gps.latitude == None:
        return("no gps fix")
    return(gps.latitude, gps.longitude)

def getTime():
    gps.update()
    if gps.timestamp_utc == None:
        return("no gps time data")
    return("{:02}:{:02}:{:02}".format(gps.timestamp_utc.tm_hour, gps.timestamp_utc.tm_min, gps.timestamp_utc.tm_sec))

def getAltitude():
    gps.update()
    if gps.altitude_m == None:
        return("no gps altitude data")
    return(gps.altitude_m)

def getGroundSpeed():
    gps.update()
    if gps.speed_knots == None:
        return("no gps ground speed data")
    return(gps.speed_knots)
