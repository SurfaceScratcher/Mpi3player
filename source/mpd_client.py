# mpd_client.py
from mpd import MPDClient, CommandError, ConnectionError
import time
from config import MPD_HOST, MPD_PORT, MPD_PASSWORD

class MpdWrapper:
    def __init__(self):
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.idletimeout = None

    def connect(self):
        try:
            self.client.connect(MPD_HOST, MPD_PORT)
            if MPD_PASSWORD:
                self.client.password(MPD_PASSWORD)
        except Exception as e:
            print(f"[MPD] Verbindung fehlgeschlagen: {e}")

    def disconnect(self):
        try:
            self.client.close()
            self.client.disconnect()
        except:
            pass

    def get_status(self):
        try:
            status = self.client.status()
            song = self.client.currentsong()
            return status, song
        except (ConnectionError, CommandError):
            self.disconnect()
            self.connect()
            return None, None

