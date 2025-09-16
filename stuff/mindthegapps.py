import os
import shutil
from stuff.general import General
from tools.helper import get_download_dir, host, print_color, run, bcolors


class MindTheGapps(General):
    dl_links = {
        "13.0.0": {
            "arm64": [
                "https://github.com/MindTheGapps/13.0.0-arm64/releases/download/MindTheGapps-13.0.0-arm64-20231025_200931/MindTheGapps-13.0.0-arm64-20231025_200931.zip",
                "dd3d04376f8326a6442c3072b7c2311d",
            ],
        },
    }

    arch = host()
    download_loc = get_download_dir()
    dl_file_name = os.path.join(download_loc, "mindthegapps.zip")
    dl_link = ...
    act_md5 = ...
    copy_dir = "./mindthegapps"
    extract_to = "/tmp/mindthegapps/extract"

    def __init__(self, version):
        self.version = version
        if version not in self.dl_links:
            raise ValueError("Android version {} not supported".format(version))
        if self.arch[0] not in self.dl_links[version]:
            raise ValueError("Architecture {} not supported for Android {}".format(self.arch[0], version))
        self.dl_link = self.dl_links[self.version][self.arch[0]][0]
        self.act_md5 = self.dl_links[self.version][self.arch[0]][1]

    def download(self):
        print_color("Downloading MindTheGapps now .....", bcolors.GREEN)
        super().download()

    def copy(self):
        if os.path.exists(self.copy_dir):
            shutil.rmtree(self.copy_dir)
        if not os.path.exists(self.extract_to):
            os.makedirs(self.extract_to)

        shutil.copytree(
            os.path.join(self.extract_to, "system", ),
            os.path.join(self.copy_dir, "system"), dirs_exist_ok=True, )
