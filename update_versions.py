#!/usr/bin/env python3
"""
Script to help update component versions
Run this to check for latest versions and get MD5 hashes
"""

import requests
import hashlib
import os
from tools.helper import download_file, get_download_dir, print_color, bcolors

def get_file_md5(url):
    """Download a file and return its MD5 hash"""
    download_loc = get_download_dir()
    filename = os.path.join(download_loc, "temp_check.md5")
    
    try:
        print_color(f"Downloading {url} to get MD5 hash...", bcolors.GREEN)
        md5_hash = download_file(url, filename)
        os.remove(filename)  # Clean up
        return md5_hash
    except Exception as e:
        print_color(f"Error downloading {url}: {e}", bcolors.RED)
        return None

def check_magisk_version():
    """Check latest Magisk version and get MD5"""
    print_color("=== Checking Magisk ===", bcolors.YELLOW)
    
    # Latest Magisk version v30.2
    magisk_url = "https://github.com/topjohnwu/Magisk/releases/download/v30.2/Magisk-v30.2.apk"
    
    md5_hash = get_file_md5(magisk_url)
    if md5_hash:
        print_color(f"Magisk URL: {magisk_url}", bcolors.GREEN)
        print_color(f"MD5 Hash: {md5_hash}", bcolors.GREEN)
        print_color("Update this in stuff/magisk.py:", bcolors.YELLOW)
        print_color(f'act_md5 = "{md5_hash}"', bcolors.GREEN)
    else:
        print_color("Failed to get Magisk MD5 hash", bcolors.RED)

def check_mindthegapps():
    """Check for newer MindTheGapps versions"""
    print_color("=== Checking MindTheGapps ===", bcolors.YELLOW)
    
    # Latest version URL (October 2023)
    current_url = "https://github.com/MindTheGapps/13.0.0-arm64/releases/download/MindTheGapps-13.0.0-arm64-20231025_200931/MindTheGapps-13.0.0-arm64-20231025_200931.zip"
    
    print_color("Latest MindTheGapps URL:", bcolors.GREEN)
    print_color(current_url, bcolors.GREEN)
    
    # Get MD5 hash for the new version
    md5_hash = get_file_md5(current_url)
    if md5_hash:
        print_color(f"MD5 Hash: {md5_hash}", bcolors.GREEN)
        print_color("Update this in stuff/mindthegapps.py:", bcolors.YELLOW)
        print_color(f'act_md5 = "{md5_hash}"', bcolors.GREEN)
    else:
        print_color("Failed to get MindTheGapps MD5 hash", bcolors.RED)
    
    print_color("Check for newer releases at:", bcolors.YELLOW)
    print_color("https://github.com/MindTheGapps/13.0.0-arm64/releases", bcolors.GREEN)

def check_litegapps():
    """Check LiteGapps version"""
    print_color("=== Checking LiteGapps ===", bcolors.YELLOW)
    
    current_url = "https://sourceforge.net/projects/litegapps/files/litegapps/arm64/33/lite/2024-10-22/LiteGapps-arm64-13.0-20241022-official.zip"
    
    print_color("Current LiteGapps URL:", bcolors.GREEN)
    print_color(current_url, bcolors.GREEN)
    print_color("Check for newer releases at:", bcolors.YELLOW)
    print_color("https://sourceforge.net/projects/litegapps/files/litegapps/arm64/33/lite/", bcolors.GREEN)

def main():
    print_color("=== Version Update Helper ===", bcolors.YELLOW)
    print_color("This script helps you get the latest versions and MD5 hashes", bcolors.GREEN)
    print()
    
    check_magisk_version()
    print()
    check_mindthegapps()
    print()
    check_litegapps()
    print()
    
    print_color("=== Summary ===", bcolors.YELLOW)
    print_color("1. Update the Magisk MD5 hash in stuff/magisk.py", bcolors.GREEN)
    print_color("2. Check for newer MindTheGapps releases", bcolors.GREEN)
    print_color("3. Monitor LiteGapps for updates", bcolors.GREEN)
    print_color("4. Test the build after updates", bcolors.GREEN)

if __name__ == "__main__":
    main()
