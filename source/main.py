# main.py
import time
from mpd_client import MpdWrapper
from oled_display import OledDisplay
from config import UPDATE_INTERVAL

def main():
    mpd = MpdWrapper()
    mpd.connect()

    oled = OledDisplay()

    while True:
        status, song = mpd.get_status()
        if status and song:
            artist = song.get("artist", "Unbekannt")
            title = song.get("title", "Ohne Titel")
            row_one = artist + "-" + title
            state = status.get("state", "-")
            oled.show_text([f"{row_one}", f"[{state}]"])
        else:
            oled.show_text(["MPD nicht erreichbar"])

        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Beendet.")

