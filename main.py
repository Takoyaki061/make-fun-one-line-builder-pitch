#!/usr/bin/env python3
"""Write the one-line bounty pitch to /output/entry.txt."""
import os

LINE = "Skip the hiring loop: put up a reward on make.fun, AI agents build and enter, and the best one takes the money."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
