# -*- coding: utf-8 -*-

from load_json import Import
import dice

import_file = Import()
extension = ".json"

class Character():

    def generate_race(self, race):
        attribute_list = import_file.json_file(race + extension)
        return attribute_list

    def generate_random(self, race, list_type, rolling):
        number = str(int(dice.roll(rolling)))
        print number
        background = import_file.json_file(race + list_type + extension)[number]
        return background
