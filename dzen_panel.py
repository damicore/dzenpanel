#! /usr/bin/env python

import time
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
            s = '^bg(' + colors[11] + ') ' + tags[i][1:] + ' '
            taglist += s
        elif tags[i][0] == ':':
            taglist += '^bg(' + colors[17] + ') ' + tags[i][1:] + ' '
        elif tags[i][0] == '.' or '!':
            taglist += '^bg(' + colors[3] + ') ' + tags[i][1:] + ' '
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

def print_colors(colors):
    res = ''
    for i in range(len(colors)):
        res +='^bg(' + colors[i] + ')' + str(i)
    return res

def get_date():
    return time.strftime('%a %d %b %Y %R')

colors = parse_xdef()
single_line_out = ''
idlein = os.popen(idle_cmd)
#for line in idlein:
#next to function
proc = os.popen(status_cmd)
output = proc.readline()
taglist = parse_tags(output)
single_line_out = taglist
print(single_line_out)
sys.stdout.flush()
#till here
while True:
    line = idlein.readline()
    if 'tag' in line:
        #from
        proc = os.popen(status_cmd)
        output = proc.readline()
        taglist = parse_tags(output)
        single_line_out = taglist
        print(single_line_out)
        sys.stdout.flush()
        #to
