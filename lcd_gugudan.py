from RPi_I2C_LCD_driver import RPi_I2C_driver
import time

lcd = RPi_I2C_driver.lcd(0x27)
lcd.clear()

lcd.setCursor(0,0)
lcd.print("gugudan")

for i in range(2,10):
	for j in range(1,10):
		inputStr = "%s x %s = %d" %(i, j, i*j)
		lcd.setCursor(0,1)
		lcd.print("%16s" %inputStr)
		time.sleep(0.5)
lcd.clear()
