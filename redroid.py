#!/usr/bin/env python3

import argparse
from stuff.litegapps import LiteGapps
from stuff.magisk import Magisk
from stuff.mindthegapps import MindTheGapps
from stuff.widevine import Widevine
import tools.helper as helper
import subprocess


def main():
    dockerfile = ""
    tags = []
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-a', '--android-version',
                        dest='android',
                        help='Specify the Android version to build',
                        default='13.0.0',
                        choices=['13.0.0'])
    parser.add_argument('-lg', '--install-litegapps',
                        dest='litegapps',
                        help='Install LiteGapps to ReDroid',
                        action='store_true')
    parser.add_argument('-mtg', '--install-mindthegapps',
                        dest='mindthegapps',
                        help='Install MindTheGapps to ReDroid',
                        action='store_true')
    parser.add_argument('-m', '--install-magisk', dest='magisk',
                        help='Install Magisk ( Bootless )',
                        action='store_true')
    parser.add_argument('-w', '--install-widevine', dest='widevine',
                        help='Integrate Widevine DRM (L3)',
                        action='store_true')
    parser.add_argument('-c', '--container', 
                        dest='container',
                        default='docker',
                        help='Specify container type', 
                        choices=['docker', 'podman'])

    args = parser.parse_args()
    
    # Check if running on ARM64 architecture
    arch = helper.host()[0]
    if arch != "arm64":
        helper.print_color("WARNING: This script is optimized for ARM64 architecture. Current architecture: {}".format(arch), helper.bcolors.YELLOW)
        helper.print_color("Continuing anyway, but some features may not work as expected.", helper.bcolors.YELLOW)
    
    dockerfile = dockerfile + \
        "FROM redroid/redroid:{}-latest\n".format(
            args.android)
    tags.append(args.android)
    
    if args.litegapps:
        LiteGapps(args.android).install()
        dockerfile = dockerfile + "COPY litegapps /\n"
        tags.append("litegapps")
        
    if args.mindthegapps:
        MindTheGapps(args.android).install()
        dockerfile = dockerfile + "COPY mindthegapps /\n"
        tags.append("mindthegapps")
        
    if args.magisk:
        Magisk().install()
        dockerfile = dockerfile+"COPY magisk /\n"
        tags.append("magisk")
        
    if args.widevine:
        Widevine(args.android).install()
        dockerfile = dockerfile+"COPY widevine /\n"
        tags.append("widevine")
        
    print("\nDockerfile\n"+dockerfile)
    with open("./Dockerfile", "w") as f:
        f.write(dockerfile)
    new_image_name = "redroid/redroid:"+"_".join(tags)
    subprocess.run([args.container, "build", "-t", new_image_name, "."])
    helper.print_color("Successfully built {}".format(
        new_image_name), helper.bcolors.GREEN)


if __name__ == "__main__":
    main()
