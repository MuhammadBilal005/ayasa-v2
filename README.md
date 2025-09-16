# Remote-Android Script - ARM64 Android 13 Edition

This script adds Gapps, Magisk and other components to redroid **without recompiling the entire image**
Optimized for ARM64 architecture and Android 13.

If redroid-script doesn't work, please create an issue

## Dependencies
- lzip

## Specify container type

Specify container type. Default is docker

option:
```
 -c {docker,podman}, --container {docker,podman}
```

## Specify an Android version

Use `-a` or `--android-version` to specify the Android version of the image being pulled. The value can be `13.0.0`. The default is 13.0.0.

```bash
# pull the latest image
python redroid.py -a 13.0.0
```

## Add LiteGapps to ReDroid image

```bash
python redroid.py -lg
```

## Add MindTheGapps to ReDroid image

```bash
python redroid.py -mtg
```

## Add Magisk to ReDroid image

Zygisk and modules like LSPosed should work. 

```bash
python redroid.py -m
```

## Add widevine DRM(L3) to ReDroid image

```
python redroid.py -w
```

## Example

This command will add LiteGapps, Magisk, and Widevine to the ReDroid image at the same time.

```bash
python redroid.py -a 13.0.0 -lgmw
```

Then start the docker container.

```bash
docker run -itd --rm --privileged \
    -v ~/data:/data \
    -p 5555:5555 \
    redroid/redroid:13.0.0-litegapps-magisk-widevine
```

## Troubleshooting

- Magisk installed: N/A

  According to some feedback from WayDroid users, changing the kernel may solve this issue. https://t.me/WayDroid/126202

- The device isn't Play Protect certified
    1. Run below command on host
    ```
    adb root
    adb shell 'sqlite3 /data/data/com.google.android.gsf/databases/gservices.db \
    "select * from main where name = \"android_id\";"'
    ```

    2. Grab device id and register on this website: https://www.google.com/android/uncertified/

## Credits
1. [remote-android](https://github.com/remote-android)
2. [waydroid_script](https://github.com/casualsnek/waydroid_script)
3. [Magisk Delta](https://huskydg.github.io/magisk-files/)
4. [LiteGapps](https://sourceforge.net/projects/litegapps/)
5. [MindTheGapps](https://github.com/s1204IT/MindTheGappsBuilder)
