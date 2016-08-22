#!/usr/bin/env python
# *-- coding: utf-8 --*

import random 
import math

# the dorms, each of which has two available spaces
dorms = ["Zeus", "Athena", "Hercules", "Bacchus", "Pluto"]

# people, along with their first and second choices
prefs = [("Toby", ("Bacchus", "Herclues")),
         ("Steve", ("Zeus", "Pluto")),
         ("Karen", ("Athena", "Zeus")),
         ("Sarah", ("Zeus", "Pluto")),
         ("Dave", ("Athena", "Bacchus")),
         ("Jeff", ("Herclues", "Pluto")),
         ("Fred", ("Pluto", "Athena")),
         ("Suzie", ("Bacchus", "Herclues")),
         ("Laura", ("Bacchus", "Herclues")),
         ("James", ("Herclues", "Athena"))]

# [(0, 9), (0, 8), (0, 7), (0, 7), (0, 6),..., (0, 0)]
domain = [(0, (len(dorms)*2)-i-1) for i in range(0, len(dorms)*2)]

def printsolution(vec):
    slots = []
    # create two slots for each dorm 
    for i in range(len(dorms)):
        slots += [i, i]

    # loop over each students assignment
    for i in range(len(vec)):
        x = int(vec[i])

        # choose the slot from the remaining ones
        dorm = dorms[slots[x]]
        # show the student and assigned dorm
        print prefs[i][0], dorm
        # remove this slot
        del slots[x]

def dormcost(vec):
    cost = 0
    # create a list of student
    slots = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

    # loop over each student
    for i in range(len(vec)):
        x = int(vec[i])
        dorm = dorms[slots[x]]
        pref = prefs[i][1]

        # first choice cost 0, second choice cost 1
        # not on the list cost3
        if pref[0] == dorm:
            cost += 0
        elif pref[1] == dorm:
            cost += 1
        else:
            cost += 3

        del slots[x]
    return cost

