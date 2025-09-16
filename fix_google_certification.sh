#!/bin/bash

# Script to fix Google Play certification issues
# Run this after the container is running

echo "=== Fixing Google Play Certification ==="

# Get the Android ID
echo "Getting Android ID..."
ANDROID_ID=$(adb shell 'sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"' | grep -o '[0-9]*')

if [ -z "$ANDROID_ID" ]; then
    echo "ERROR: Could not get Android ID. Make sure the container is running and ADB is connected."
    echo "Run: adb connect 127.0.0.1:5556"
    exit 1
fi

echo "Android ID: $ANDROID_ID"
echo ""
echo "To fix Google Play certification:"
echo "1. Go to: https://www.google.com/android/uncertified/"
echo "2. Enter this Android ID: $ANDROID_ID"
echo "3. Complete the registration"
echo ""
echo "After registration, restart the container for changes to take effect."
