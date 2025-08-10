# config.py
# Konfigurationsparameter für MPD-OLED-Display

# MPD Einstellungen
MPD_HOST = "localhost"
MPD_PORT = 6600
MPD_PASSWORD = None  # z.B. "geheim" falls benötigt

# OLED Einstellungen
I2C_ADDRESS = 0x3C
OLED_WIDTH = 128
OLED_HEIGHT = 32

# Update-Intervalle
UPDATE_INTERVAL = 1.0  # Sekunden zwischen MPD-Abfragen
SCROLL_SPEED = 0.3     # Sekunden pro Scrollschritt

