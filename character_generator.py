# -*- coding: utf-8 -*-

from load_json import Import
import dice, os

import_file = Import()
extension = ".json"


class Character():

    def generate_ancestry(self, ancestry):
        if os.name == "posix":
            attribute_list = import_file.json_file("ancestries" + "/" +
            ancestry + "/" + ancestry + extension)
        else:
            attribute_list = import_file.json_file(".\\ancestries" + "\\" +
            ancestry + "\\" + ancestry + extension)
        return attribute_list

    def generate_random(self, ancestry, list_type, rolling):
        number = str(int(dice.roll(rolling)))
        try:
            if os.name == "posix":
                background = import_file.json_file("ancestries" + "/" +
                ancestry + "/" + ancestry + list_type + extension)[number]
            else:
                background = import_file.json_file(".\\ancestries" + "\\" +
                ancestry + "\\" + ancestry + list_type + extension)[number]
        except (SyntaxError, IOError):
            return ""
        else:
            return background#.encode("utf-8")

    def generate_profession(self):
        type_number = str(int(dice.roll("1d6")))
        profession_number = str(int(dice.roll("1d20")))
        professions_dict = {"1": "academic", "2": "common", "3": "criminal", "4": "martial", "5": "religious", "6": "wilderness"}
        try:
            if os.name == "posix":
                profession_type = import_file.json_file("professions/profession_type.json")[type_number]
                profession = import_file.json_file("professions/" + professions_dict[type_number] + ".json")[profession_number]
            else:
                profession_type = import_file.json_file(".\\professions\\profession_type.json")[type_number]
                profession = import_file.json_file(".\\professions\\" + professions_dict[type_number] + ".json")[profession_number]
        except ():
            return ""
        else:
            return profession_type, profession

    def generate_wealth(self):
        number = str(int(dice.roll("3d6")))
        try:
            if os.name == "posix":
                wealth = import_file.json_file("wealth/wealth.json")[number]
            else:
                wealth = import_file.json_file(".\\wealth\\wealth.json")[number]
        except ():
            return ""
        else:
            return wealth#.encode("utf-8")

    def generate_interesting_things(self):
        table_number = str(int(dice.roll("1d6")))
        json_file = "table_" + table_number + ".json"
        interesting_things_number = str(int(dice.roll("1d20")))
        try:
            if os.name == "posix":
                interesting_thing = import_file.json_file("interesting_things/table_" + table_number + ".json")[interesting_things_number]
            else:
                interesting_thing = import_file.json_file(".\\interesting_things\\table_" + table_number + ".json")[interesting_things_number]
        except ():
            return ""
        else:
            return interesting_thing#.encode("utf-8")

    def generate_personality_traits(self):
        positive_number_a = str(int(dice.roll("1d20")))
        positive_number_b = positive_number_a
        while positive_number_a == positive_number_b: positive_number_b = str(int(dice.roll("1d20")))
        negative_number = str(int(dice.roll("1d20")))
        if os.name == "posix":
            positive_trait_a = import_file.json_file("personality_traits/positive_personality_traits.json")[positive_number_a]
            positive_trait_b = import_file.json_file("personality_traits/positive_personality_traits.json")[positive_number_b]
            negative_trait = import_file.json_file("personality_traits/negative_personality_traits.json")[negative_number]
        else:
            positive_trait_a = import_file.json_file(".\\personality_traits\\positive_personality_traits.json")[positive_number_a]
            positive_trait_b = import_file.json_file(".\\personality_traits\\positive_personality_traits.json")[positive_number_b]
            negative_trait = import_file.json_file(".\\personality_traits\\negative_personality_traits.json")[negative_number]
        return positive_trait_a, positive_trait_b, negative_trait
