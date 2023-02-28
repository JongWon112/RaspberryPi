from RPi_I2C_LCD_driver import RPi_I2C_driver
import time

lcd = RPi_I2C_driver.lcd(0x27)
lcd.clear()

lcd.setCursor(0, 0)
lcd.print("Lcd Test")
lcd.setCursor(0, 1)
lcd.print("Hello")
