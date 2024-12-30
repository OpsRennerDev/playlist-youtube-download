import os
import yt_dlp

def download_playlist(playlist_url, cookies_file, output_dir):
    """
    Download a YouTube playlist as MP3 files using yt-dlp.

    :param playlist_url: URL of the YouTube playlist
    :param cookies_file: Path to the cookies.txt file
    :param output_dir: Directory where MP3 files will be saved
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'cookiefile': cookies_file,
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Starting download of playlist: {playlist_url}")
        ydl.download([playlist_url])
        print(f"Download completed. Files saved to: {output_dir}")

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the YouTube playlist: ").strip()
    cookies_file = input("Enter the path to your cookies.txt file: ").strip()
    output_dir = input("Enter the directory where MP3 files should be saved: ").strip()

    try:
        download_playlist(playlist_url, cookies_file, output_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
