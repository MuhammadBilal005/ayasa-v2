import os
import shutil
from stuff.general import General
from tools.helper import get_download_dir, host, print_color, run, bcolors


class LiteGapps(General):
    dl_links = {
        "13.0.0": {
            "arm64": [
                "https://sourceforge.net/projects/litegapps/files/litegapps/arm64/33/lite/2024-10-22/LiteGapps-arm64-13.0-20241022-official.zip",
                "a8b1181291fe70d1e838a8579218a47c",
            ],
        },
    }
    api_level_map = {
        "13.0.0": "33",
    }
    arch = host()
    download_loc = get_download_dir()
    dl_file_name = os.path.join(download_loc, "litegapps.zip")
    dl_link = ...
    act_md5 = ...
    copy_dir = "./litegapps"
    extract_to = "/tmp/litegapps/extract"

    def __init__(self, version):
        self.version = version
        if version not in self.dl_links:
            raise ValueError("Android version {} not supported".format(version))
        if self.arch[0] not in self.dl_links[version]:
            raise ValueError("Architecture {} not supported for Android {}".format(self.arch[0], version))
        self.dl_link = self.dl_links[self.version][self.arch[0]][0]
        self.act_md5 = self.dl_links[self.version][self.arch[0]][1]

    def download(self):
        print_color("Downloading LiteGapps now .....", bcolors.GREEN)
        super().download()

    def copy(self):
        if os.path.exists(self.copy_dir):
            shutil.rmtree(self.copy_dir)
        if not os.path.exists(self.extract_to):
            os.makedirs(self.extract_to)
        if not os.path.exists(os.path.join(self.extract_to, "appunpack")):
            os.makedirs(os.path.join(self.extract_to, "appunpack"))

        # extract extract_to/files/files.tar.xz file to extract_to/appunpack
        run( [ "tar", "-xvf", os.path.join(self.extract_to, "files", "files.tar.xz"), "-C", os.path.join(self.extract_to, "appunpack"), ])
        shutil.copytree( os.path.join( self.extract_to, "appunpack", self.arch[0], self.api_level_map[self.version], "system",), os.path.join(self.copy_dir, "system"), dirs_exist_ok=True,)
