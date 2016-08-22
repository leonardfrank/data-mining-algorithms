#!/usr/bin/env python
# *-- coding : utf-8 --*

import math

people = ["Charlie", "Augustus", "Veruca", "Violet", "Mike", "Joe", "Willy", "Miranda"]

links = [("Augustus", "Willy"),
         ("Mike", "Joe"),
         ("Miranda", "Mike"),
         ("Violet", "Augustus"),
         ("Miranda", "Willy"),
         ("Charlie", "Mike"),
         ("Veruca", "Joe"),
         ("Miranda", "Augustus"),
         ("Willy", "Augustus"),
         ("Joe", "Charlie"),
         ("Veruca", "Augustus"),
         ("Miranda", "Joe")]


def crosscount(v):
    # convert the number list into a dictionary of person:(x, y)
    loc = dict([(people[i], (v[i*2], v[i*2+1])) for i in range(0, len(people))])
    total = 0
    # loop through every pair of links
    for i in range(len(links)):
        for j in range(i+1, len(links)):
            
            # get the locations
            (x1, y1), (x2, y2) = loc[links[i][0]], loc[links[i][1]]
            (x3, y3), (x4, y4) = loc[links[j][0]], loc[links[j][1]]

            den = (y4-y3) * (x2-x1) - (x4-x3) * (y2-y1)

            # den == 0 if the lines are parallel
            if den == 0:
                continue

            # otherwise ua and ub are the fraction of the line where they cross
            ua = ((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3)) / den
            ub = ((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3)) / den

            # if the fraction is between 0 and 1 for both lines then they cross each other
            if 0 < ua < 1 and 0 < ub < 1:
                total += 1
    return total  

from PIL import Image, ImageDraw
def drawnetwork(sol):
    # create the image
    img = Image.new('RGB', (400, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # create the position dict
    pos = dict([(people[i], (sol[i*2], sol[i*2+1])) for i in range(0, len(people))])

    for (a, b) in links:
        draw.line((pos[a], pos[b]), fill=(255, 0, 0))

    for n, p in pos.items():
        draw.text(p, n, (0, 0, 0))

    img.show()

domain = [(10, 370)] * (len(people)*2)
