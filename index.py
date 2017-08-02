# -*- coding: utf-8 -*-

"""
posix:
export FLASK_APP=index.py
windows:
set FLASK_APP=index.py
flask run
"""
from character_generator import Character
from flask import Flask, render_template
import sys, random

app = Flask(__name__)

@app.route("/")
def create_char():
    character = Character()
    ancestry_list = ["human", "changeling", "clockwork", "dwarf", "orc", "goblin"]
    ancestry = ancestry_list[random.randint(0, len(ancestry_list) - 1)]
    attributes = character.generate_ancestry(ancestry)
    names = attributes["names"]
    name = names[random.randint(0, len(names) - 1)]
    strength = attributes["strength"]
    agility = attributes["agility"]
    intelect = attributes["intelect"]
    will = attributes["will"]
    perception = intelect
    defense = agility
    health = strength
    healing_rate = str(int(round(int(health)/4, 0)))
    size = attributes["size"]
    speed = attributes["speed"]
    power = attributes["power"]
    damage = attributes["damage"]
    insanity = attributes["insanity"]
    corruption = attributes["corruption"]
    language = attributes["languages"]
    background = character.generate_random(ancestry, "_background" , "1d20")
    personality = character.generate_random(ancestry, "_personality", "3d6")
    religion = character.generate_random(ancestry, "_religion", "3d6")
    age = character.generate_random(ancestry, "_age", "3d6")
    build = character.generate_random(ancestry, "_build", "3d6")
    appearence = character.generate_random(ancestry, "_appearence", "3d6")
    true_age = character.generate_random(ancestry, "_true_age", "3d6")
    apparent_gender = character.generate_random(ancestry, "_apparent_gender", "1d6")
    apparent_ancestry = character.generate_random(ancestry, "_apparent_ancestry", "3d6")
    quirk = character.generate_random(ancestry, "_quirk", "1d20")
    form = character.generate_random(ancestry, "_form", "3d6")
    purpose = character.generate_random(ancestry, "_purpose", "1d20")
    hatred = character.generate_random(ancestry, "_hatred", "1d20")
    diistinctive_appearence = character.generate_random(ancestry, "_distinctive_appearence", "1d20")
    odd_habit = character.generate_random(ancestry, "_odd_habit", "1d20")
    profession_type, profession = character.generate_profession()
    wealth = character.generate_wealth()
    interesting_thing = character.generate_interesting_things()
    positive_trait_a, positive_trait_b, negative_trait = character.generate_personality_traits()
    return render_template('index.html', **locals())
