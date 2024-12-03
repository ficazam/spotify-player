import webbrowser
import time
import random
import pyautogui
import schedule

# this is just some placeholder playlists. You can add any playlist you like!
playlists = [
    "https://open.spotify.com/playlist/28BE3XWhDJdnAGKybZIJPK",
    "https://open.spotify.com/playlist/5S85xmkjdaMBp91V5ACjPv",
    "https://open.spotify.com/playlist/3OhVs5fNbkLe27XEvE6s7y",
    "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM",
    "https://open.spotify.com/album/63Fj4g3QB8tP1T46fTWKbI",
]

def openSpotifyAndPlay():
    url = random.choice(playlists)
    webbrowser.open(url)
    
    time.sleep(5)
    # use the calculateMousePosition func to find where the play button is on your screen, then adjust.
    pyautogui.moveTo(2320, 1025)
    pyautogui.click()
    
def calculateMousePosition():
    print("Move your mouse to the desired position and press Ctrl+C to stop.")
    try:
        while True:
            print(pyautogui.position())
    except KeyboardInterrupt:
        print("Position capture stopped.")

def main():
    # calculateMousePosition()
    openSpotifyAndPlay()
    
schedule.every().monday.at("08:07").do(main)
schedule.every().tuesday.at("08:07").do(main)
schedule.every().wednesday.at("08:07").do(main)
schedule.every().thursday.at("08:07").do(main)
schedule.every().friday.at("08:07").do(main)
    
while True:
    schedule.run_pending()
    time.sleep(60)