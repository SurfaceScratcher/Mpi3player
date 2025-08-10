# oled_display.py
import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from config import I2C_ADDRESS, OLED_WIDTH, OLED_HEIGHT

class OledDisplay:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=I2C_ADDRESS)
        self.display.fill(0)
        self.display.show()
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

    def show_text(self, lines):
        image = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))
        draw = ImageDraw.Draw(image)

        for i, text in enumerate(lines):
            draw.text((0, i * 15), text, font=self.font, fill=255)

        self.display.image(image)
        self.display.show()

