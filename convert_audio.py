#!/usr/bin/env python3
"""Convert local audio files between formats with ffmpeg.

Only converts files already on disk, downloads nothing.
Example: python convert_audio.py in.wav out.mp3 320k
"""
import subprocess
import sys


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: convert_audio.py in.wav out.mp3 320k")
        return 2
    src, dst, bitrate = sys.argv[1], sys.argv[2], sys.argv[3]
    r = subprocess.run(
        ["ffmpeg", "-y", "-i", src, "-b:a", bitrate, dst],
        capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-500:], file=sys.stderr)
        return r.returncode
    print(f"{src} -> {dst} ({bitrate})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
