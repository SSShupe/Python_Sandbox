# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:41:33 2019

@author: Steve Shupe
"""
import numpy as np
import random

def simulate_prizedoor(number):
    prizedoors = []
    for i in range(number):
        prizedoors.append(random.choice([0,1,2]))
    return np.array(prizedoors)
    
def simulate_guess(number):
    guesses = []
    for i in range(number):
        guesses.append(random.choice([0,1,2]))
    return np.array(guesses)

def goat_door(simulate_prizedoor, simulate_guess):
    goat_list = []
    for i in range(len(simulate_guess)):
        if simulate_guess[i] == simulate_prizedoor[i]:
            choices = [0,1,2]
            choices.remove(simulate_guess[i])
            goat_list.append(random.choice(choices))
        else:
            choices_1 = [0,1,2]
            choices_1.remove(simulate_prizedoor[i])
            choices_1.remove(simulate_guess[i])
            goat_list.append(choices_1[0])
    return np.array(goat_list)

def switch_guess(simulate_guess, goat_door):
    new_guesses = []
    for i in range(len(simulate_guess)):
        switched_choices = [0,1,2]
        switched_choices.remove(simulate_guess[i])
        switched_choices.remove(goat_door[i])
        new_guesses.append(switched_choices[0])
    return np.array(new_guesses)
    
def win_percentage(guesses, simulate_prizedoors):
    wins = 0
    for i in range(len(simulate_prizedoors)):
        if guesses[i] == simulate_prizedoors[i]:
            wins += 1
    return wins/len(simulate_prizedoors)

#Stick with original guess
print("Win percentage sticking with original door:", win_percentage(simulate_guess(10000), simulate_prizedoor(10000)))

#Switch door after goatdoor opened
a = simulate_prizedoor(10000)
b = simulate_guess(10000)
g = goat_door(a,b)
s = switch_guess(b,g)
print("Win percentage changing doors after goat door opened:", win_percentage(s,a))

"""
Win percentage sticking with original door: 0.3299
Win percentage changing doors after goat door opened: 0.667
"""