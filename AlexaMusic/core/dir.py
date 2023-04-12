#
# Cᴏᴘʏʀɪɢʜᴛ (C) 2021-2022 by Jᴏᴋᴇʀ @Github, < https://github.com/DEAR_HK >.

# RADHE MUSIC мαкєѕ уσυ нαρρу αи∂ ιтѕ α ραят σf THE_JOKER_ZONE .

# Kanged By © @DEAR_HK
# Group © @THE_JOKER_ZONE

# lankadhipatilankesh
# All rights reserved. ©Yukki


import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
