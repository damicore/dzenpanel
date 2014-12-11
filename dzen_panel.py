#! /usr/bin/env python

import sys
import string
import os

status_cmd = 'herbstclient tag_status'
idle_cmd = 'herbstclient --idle'

def parse_tags(output):
    #Takes herbstclient tag_status and parses it
    #returns a nested list of tags.
    tags = output.split()
    taglist = ''
    for i in range(len(tags)):
        if tags[i][0] == '#':
            s = '^bg(' + colors[3] + ')' + tags[i][1:] + ' '
            taglist += s
        elif tags[i][0] == ':':
            taglist += '^bg(' + colors[4] + ')' + tags[i][1:] + ' '
    return taglist

def parse_xdef():
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

colors = parse_xdef()
single_line_out = ''
idlein = os.popen(idle_cmd)
#for line in idlein:
#while True:
line = idlein.readline()
    #if 'tag' in line:
proc = os.popen(status_cmd)
output = proc.readline()
taglist = parse_tags(output)
single_line_out = taglist + ' hola'
sys.stdout.write(single_line_out)

#while True:
    #idlein = os.popen(idle_cmd)
    #print(idlein.readline())
    #if 'tag' in event:
    #proc = os.popen(status_cmd)
    #output = proc.readline()
    #taglist = parse_tags(output)
    #print(taglist)
