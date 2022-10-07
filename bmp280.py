import board
import busio
import adafruit_bmp280
import time

# initialise communication and create sensor object
i2c = busio.I2C(scl=board.GP15, sda=board.GP14)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)


def getQfe():
    # calculate average starting pressure
    qfetemp = []
    for i in range(0, 10):
        qfetemp.append(bmp280.pressure)
        time.sleep(1)
    qfe = sum(qfetemp) / len(qfetemp)
    return(qfe)

def getTemperature():
    return bmp280.temperature

def getPressure():
    return bmp280.pressure

def getHeight(qfeb):
    # use rough 30ft per 100Pa calculation for pressure altitude
    changePress = (qfeb - bmp280.pressure) * 100
    heightb = changePress * 0.3
    heightbm = heightb / 3.281
    return heightbm
