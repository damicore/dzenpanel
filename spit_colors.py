#! /usr/bin/env python

import os

def parse_xres():
    os.chdir('/home/damian/')
    fin = open('.Xresources')
    colors = []
    for line in fin:
        color = line.strip()
        if 'color' in color:
            rgb = color[color.find('#'):]
            colors.append(rgb)
        elif 'background' in color:
            colors.append(color[color.find('#'):])
        elif 'foreground' in color:
            colors.append(color[color.find('#'):])
    return(colors)


print(parse_xres())
