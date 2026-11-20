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

Make sure you have **Python 3** and the following three command-line tools:
1. **[Python 3](https://python.org)** — Required to run the `.py` scripts and GUI.
2. **[yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/)** — For downloading the streams.
3. **[FFmpeg](https://ffmpeg.org)** — Required by `yt-dlp` for remuxing video to `.mkv`.
4. **[MKVToolNix (`mkvmerge`)](https://mkvtoolnix.download)** — For merging separate video and audio tracks into one `.mkv` file.

---

## Setup Instructions

### 1. Download the App
1. Go to the **Releases** section on the right side of this GitHub repository.
2. Download the latest **`.zip` file** containing the `.py` scripts and extract it into a folder on your computer.

---

### 2. Windows Setup

#### Step 1: Install Python (Skip if already installed)
1. Go to [python.org/downloads](https://python.org) and download the latest Python installer for Windows (or open PowerShell and run `winget install Python.Python.3.14`).
2. Run the installer.
3. **Important:** If using the standard `.exe` installer, make sure to check the box that says **"Add python.exe to PATH"** at the bottom of the first screen before clicking **Install Now**. *(If using the newer Python Install Manager, accept the default prompts to install Python and configure aliases.)*
4. To verify Python is installed, open Command Prompt and run `python --version`.

#### Step 2: Set Up `yt-dlp`, `FFmpeg`, and `MKVToolNix`
You can place the tools **locally inside the extracted folder** (recommended) or install them **system-wide**:

##### Option A: Portable Folder Setup (Recommended)
Download the Windows tools and place them **directly inside the exact same folder as the extracted `.py` files**:
- **yt-dlp:** Download `yt-dlp.exe` from [yt-dlp Releases](https://github.com/yt-dlp/yt-dlp/releases/) and place it directly in the project folder.
- **FFmpeg:** Go to [Gyan.dev FFmpeg Builds](https://gyan.dev), scroll to the **release builds** section, and download **`ffmpeg-release-essentials.zip`**. Extract the `.zip` file, open the extracted folder, go into the **`bin`** subfolder, and copy **`ffmpeg.exe` and `ffprobe.exe`** into your project folder alongside the `.py` files (you do not need `ffplay.exe`).
- **MKVToolNix:** Go to [MKVToolNix](https://mkvtoolnix.download), click **Downloads** in the top menu, and scroll down to the **Windows** section. Download the **64-bit portable `.7z` archive** (named `mkvtoolnix-64-bit-xx.x.x.7z`, **not** the installer `.exe`). Extract the `.7z` file, open the extracted `mkvtoolnix` folder, and copy **`mkvmerge.exe`** directly into your project folder alongside the `.py` files (you do not need any of the other files or folders). *(Windows 11 can extract `.7z` files natively; Windows 10 users can use [7-Zip](https://7-zip.org).)*

##### Option B: System-Wide Setup via `winget`
Open PowerShell and run:
```powershell
winget install yt-dlp.yt-dlp Gyan.FFmpeg MoritzBunkus.MKVToolNix
```
*(Note: If `mkvmerge` is not automatically added to your PATH, add `C:\Program Files\MKVToolNix` to your Windows Environment Variables.)*

#### Step 3: Run the App
Open Command Prompt or PowerShell inside your project folder (tip: click the File Explorer address bar, type `cmd`, and press **Enter**) and run:
```cmd
python your_main_script.py
```

---

### 3. Linux Setup
1. Most Linux distributions already include Python 3, though `tkinter` often needs to be installed separately. Install Python, Tkinter, and the required tools using your distribution's package manager. For example, on Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install python3 python3-tk yt-dlp ffmpeg mkvtoolnix
   ```
2. Navigate to the extracted folder and launch the GUI:
   ```bash
   cd /path/to/extracted/folder
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
