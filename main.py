# -*- coding: utf-8 -*-

from character_generator import Character
import sys, random

character = Character()

ancestry_list = ["Human", "Changeling", "Clockwork", "Dwarf", "Orc", "Goblin"]
ancestry = ancestry_list[random.randint(0, 5)]

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

print "Name: " + name
print "Ancestry: " + ancestry
print "Strength: " + strength
print "Agility: " + agility
print "Intelect: " + intelect
print "Will: " + will
print "Perception: " + intelect
print "Defense: " + agility
print "Health: " + health
print "Healing Rate: " + healing_rate
print "Size: " + size
print "Speed: " + speed
print "Power: " + power
print "Damage: " + damage
print "Insanity: " + insanity
print "Corruption: " + corruption
print "Languages: " + language
print "Background: " + background
print "Personality: " + personality
print "Profession Type: " + profession_type
print "Profession: " + profession
print "Wealth: " + wealth
print "Interesting Thing: " + interesting_thing
print "Positive Traits: " + positive_trait_a + ", " + positive_trait_b
print "Negative Trait: " + negative_trait

if ancestry == "human":
    print "Religion: " + religion
    print "Age: " + age
    print "Build: " + build
    print "Appearence: " + appearence
elif ancestry == "changeling":
    print "True Age: " + true_age
    print "Apparent Gender: " + apparent_gender
    print "Apparent Ancestry: " + apparent_ancestry
    print "Quirk" + ": " + quirk
elif ancestry == "clockwork":
    print "Form: " + form
    print "Purpose: " + purpose
elif ancestry == "dwarf":
    print "Age: " + age
    print "Appearence: " + appearence
    print "Build: " + build
    print "Hatred: " + hatred
elif ancestry == "goblin":
    print "Age: " + age
    print "Build: " + build
    print "Distinctive Appearance: " + diistinctive_appearence
    print "Odd Habit: " + odd_habit
elif ancestry == "orc":
    print "Build: " + build
    print "Age: " + age
    print "Appearence: " + appearence
