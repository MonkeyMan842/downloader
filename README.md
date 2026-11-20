# Media Downloader & Merger GUI

A lightweight Python Tkinter desktop app for downloading video and separate audio streams using `yt-dlp`, automatically remuxing and merging them into clean `.mkv` files with `mkvmerge` (MKVToolNix), and organizing shows or movies into properly named files.

## Features
- **Simple GUI:** Built with Python's built-in `tkinter`—no heavy Python dependencies required.
- **Separate Audio & Video Merging:** Automatically downloads separate visual and audio streams and combines them into a single `.mkv` file.
- **Auto-Cleanup:** Optional checkbox to automatically delete temporary `- visual.mkv` and `- audio.mkv` files after merging.
- **TV Show & Movie Formatting:** Automatically formats filenames for movies (`Movie Name.mkv`) or episodes (`Show Name - S01E01 - Episode Name.mkv`).
- **Cross-Platform:** Works on both **Windows** and **Linux**.

---

## Prerequisites

Make sure you have **Python 3** and the following three command-line tools installed:
1. **[yt-dlp](https://github.com)** — For downloading the streams.
2. **[FFmpeg](https://ffmpeg.org)** — Required by `yt-dlp` for remuxing video to `.mkv`.
3. **[MKVToolNix (`mkvmerge`)](https://mkvtoolnix.download)** — For merging separate video and audio tracks into one `.mkv` file.

---

## Setup Instructions

### Windows Setup
You can install the tools either **locally inside the project folder** (easiest) or **system-wide**:

#### Option A: Portable Folder Setup (Recommended)
1. Download or clone this repository to a folder on your PC.
2. Download the Windows executables and place them **in the exact same folder as the `.py` files**:
   - `yt-dlp.exe` (from [yt-dlp Releases](https://github.com/releases))
   - `ffmpeg.exe` (from [FFmpeg Windows builds](https://gyan.dev))
   - `mkvmerge.exe` **and all accompanying `.dll` files** (from the portable `.7z` archive on the [MKVToolNix Downloads](https://mkvtoolnix.downloaddownloads.html#windows) page)
3. Open Command Prompt or PowerShell inside that folder (tip: click the File Explorer address bar, type `cmd`, and press **Enter**) and run:
   ```cmd
   python your_main_script.py
   ```

#### Option B: System-Wide Setup via `winget`
Open PowerShell and run:
```powershell
winget install yt-dlp.yt-dlp Gyan.FFmpeg MoritzBunkus.MKVToolNix
```
*(Note: If `mkvmerge` is not automatically added to your PATH, add `C:\Program Files\MKVToolNix` to your Windows Environment Variables.)*

---

### Linux Setup
1. Install Python Tkinter and the required tools using your distribution's package manager. For example, on Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install python3-tk yt-dlp ffmpeg mkvtoolnix
   ```
2. Navigate to the project folder and launch the GUI:
   ```bash
   cd /path/to/repo
   python3 your_main_script.py
   ```

---

## How to Use
1. Launch the app (`python your_main_script.py`).
2. **Uncheck `DanTheMan?`** to reveal the **File Path** box, and paste the full folder path where you want your files saved (e.g., `C:\Users\Name\Videos` on Windows or `/home/name/Videos` on Linux).
3. Paste the **URL** (and **Audio URL** if `needs Audio?` is checked).
4. Enter the **Ep/Movie Name** (and **Show Name**, **Season num**, and **Episode Num** if `Show?` is checked).
5. Check **Delete separate files?** if you want the temporary visual/audio files removed after merging.
6. Click **run** and check your terminal window for download progress.
