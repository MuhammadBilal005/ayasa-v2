import os
import re
import shutil
from stuff.general import General
from tools.helper import bcolors, get_download_dir, host, print_color, run


class Widevine(General):
    def __init__(self, android_version) -> None:
        super().__init__()
        self.android_version = android_version
        if android_version not in self.dl_links[self.machine[0]]:
            raise ValueError("Android version {} not supported for architecture {}".format(android_version, self.machine[0]))
        self.dl_link = self.dl_links[self.machine[0]][android_version][0]
        self.act_md5 = self.dl_links[self.machine[0]][android_version][1]

    download_loc = get_download_dir()
    machine = host()
    copy_dir = "./widevine"
    dl_links = {
        "arm64": {
            "13.0.0": ["https://github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/archive/a8524d608431573ef1c9313822d271f78728f9a6.zip",
                       "5c55df61da5c012b4e43746547ab730f"]
        }
    }
    dl_file_name = os.path.join(download_loc, "widevine.zip")
    extract_to = "/tmp/widevineunpack"

    def download(self):
        print_color("Downloading widevine now .....", bcolors.GREEN)
        super().download()

    def copy(self):
        if os.path.exists(self.copy_dir):
            shutil.rmtree(self.copy_dir)
        run(["chmod", "+x", self.extract_to, "-R"])
        print_color("Copying widevine library files ...", bcolors.GREEN)
        name = re.findall(r"([a-zA-Z0-9]+)\.zip", self.dl_link)[0]
        shutil.copytree(os.path.join(self.extract_to, "vendor_google_proprietary_widevine-prebuilt-"+name,
                        "prebuilts"), os.path.join(self.copy_dir, "vendor"), dirs_exist_ok=True)

        for file in os.listdir(os.path.join(self.copy_dir, "vendor", "etc", "init")):
            if file.endswith('.rc'):
                os.chmod(os.path.join(self.copy_dir, "vendor", "etc", "init", file), 0o644)
