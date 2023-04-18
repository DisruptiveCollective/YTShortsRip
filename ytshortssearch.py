import sys
import subprocess

def download_shorts(search_term, max_results=100):
    cmd = [
        "yt-dlp",
        f"ytsearch{max_results}:\"{search_term}\"",
        "--match-filter",
        "duration<60",
        "--format",
        "best[ext=mp4]",
        "-o",
        "downloads/%(title)s.%(ext)s",
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Downloaded top {max_results} YouTube Shorts for '{search_term}'")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading YouTube Shorts: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_shorts_ytdlp.py \"search_term\"")
        sys.exit(1)

    search_term = sys.argv[1]
    download_shorts(search_term)

if __name__ == "__main__":
    main()
