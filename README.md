### README.md

```markdown
# Spotify Lofi Playlist Automation

This Python script automates the process of opening Spotify in a browser and playing a random lofi playlist at 7:30 AM every weekday. It supports multi-monitor setups and allows you to customize playlist URLs and screen coordinates.

---

## Features
- Randomly selects a playlist from your predefined list.
- Works with multiple monitors.
- Schedules playback for specific days and times (default: 7:30 AM on weekdays).

---

## Prerequisites

### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/downloads/).

### 2. Install Required Libraries
Install dependencies using `pip`:
```bash
pip install pyautogui schedule screeninfo
```

### 3. Spotify Account
Ensure you're logged in to Spotify in your default browser to avoid login interruptions.

---

## Configuration

### 1. Add Your Playlist URLs
Edit the `playlists` list in the script with the URLs of your favorite Spotify playlists:
```python
playlists = [
    "https://open.spotify.com/playlist/37i9dQZF1DX2qzUOsHszjJ",  # Example playlist 1
    "https://open.spotify.com/playlist/37i9dQZF1DWU1h2c7gbFUs",  # Example playlist 2
    "https://open.spotify.com/playlist/37i9dQZF1DX5eE1W1GFpZZ",  # Example playlist 3
]
```

### 2. Adjust Play Button Coordinates
Use the helper script to find the "Play" button coordinates for your monitor setup:
```python
import pyautogui
print("Move your mouse to the desired position and press Ctrl+C to stop.")
try:
    while True:
        print(pyautogui.position())
except KeyboardInterrupt:
    print("Position capture stopped.")
```

Update the coordinates in the `play_button_positions` dictionary for each monitor.

---

## Running the Script

Run the script using:
```bash
python spotify_lofi_automation.py
```

To ensure the script runs automatically on startup, follow the instructions for your operating system:

### Windows
1. Press `Win + R`, type `shell:startup`, and hit Enter.
2. Copy the script or a shortcut to the script into the startup folder.
3. (Optional) Create a `.bat` file to run the script:
    ```bat
    @echo off
    pythonw "C:\path\to\spotify_lofi_automation.py"
    ```
   Place the `.bat` file in the startup folder.

### macOS
1. Open the **Terminal** and create a `plist` file for the script:
    ```bash
    nano ~/Library/LaunchAgents/com.spotifylofi.plist
    ```
2. Add the following content:
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.spotifylofi</string>
        <key>ProgramArguments</key>
        <array>
            <string>/usr/bin/python3</string>
            <string>/path/to/spotify_lofi_automation.py</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
    </dict>
    </plist>
    ```
3. Save and enable the script:
    ```bash
    launchctl load ~/Library/LaunchAgents/com.spotifylofi.plist
    ```

### Linux
1. Create a systemd service file:
    ```bash
    sudo nano /etc/systemd/system/spotify_lofi.service
    ```
2. Add the following content:
    ```ini
    [Unit]
    Description=Spotify Lofi Automation Script
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /path/to/spotify_lofi_automation.py
    Restart=always

    [Install]
    WantedBy=default.target
    ```
3. Enable and start the service:
    ```bash
    sudo systemctl enable spotify_lofi.service
    sudo systemctl start spotify_lofi.service
    ```

---

## Troubleshooting
- **PyAutoGUI Coordinates Off**: Ensure your monitor setup matches the configured coordinates.
- **Script Doesn’t Run on Startup**: Double-check the file paths and startup configuration for your OS.
- **Browser Login Issues**: Log in to Spotify manually in your default browser to avoid interruptions.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it for personal or commercial use.
```

This README provides step-by-step instructions to set up the script and ensure it runs on startup for Windows, macOS, and Linux. Let me know if you'd like to adjust or expand on any section!