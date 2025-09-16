#!/bin/bash

# Correct Docker run command for ARM64 Android 13 with LiteGapps, Magisk, and Widevine
# This removes the x86_64 native bridge parameters that don't work with ARM64

docker run -itd --privileged --restart=always \
    -v ~/asaya13_2/data:/data \
    -p 5556:5555 \
    redroid/redroid:13.0.0_litegapps_magisk_widevine \
    ro.build.fingerprint=google/redfin/redfin:12/SQ1D.220205.003/8069835:user/release-keys \
    ro.product.model="Pixel 5" \
    ro.product.manufacturer=Google \
    ro.product.brand=google \
    ro.product.name=redfin \
    ro.product.device=redfin \
    ro.adb.secure=0 \
    ro.secure=0 \
    androidboot.adb=1 \
    androidboot.redroid_adb_enable=1

echo "Container started with correct ARM64 parameters"
echo "Connect with: adb connect 127.0.0.1:5556"
