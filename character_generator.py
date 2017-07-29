# -*- coding: utf-8 -*-

from load_json import Import
import dice, os

import_file = Import()
extension = ".json"


class Character():

    def generate_ancestry(self, ancestry):
        if os.name == "posix":
            attribute_list = import_file.json_file("./ancestries" + "/" +
            ancestry + "/" + ancestry + extension)
        else:
            attribute_list = import_file.json_file(".\\ancestries" + "\\" +
            ancestry + "\\" + ancestry + extension)
        return attribute_list

    def generate_random(self, ancestry, list_type, rolling):
        number = str(int(dice.roll(rolling)))
        try:
            if os.name == "posix":
                background = import_file.json_file("./ancestries" + "/" +
                ancestry + "/" + ancestry + list_type + extension)[number]
            else:
                background = import_file.json_file(".\\ancestries" + "\\" +
                ancestry + "\\" + ancestry + list_type + extension)[number]
        except (SyntaxError, IOError, UnicodeEncodeError):
            return ""
        else:
            return background
