#! /usr/bin/env python2

import os

status_cmd = 'herbstclient tag_status'

def parse_tags(status):
    #Takes herbstclient tag_status and parses it
    #returns a nested list of tags.
    tags = status.split()
    for i in range(len(tags)):
        tag = tags[i]
        t = list(tag)
        tags[i] = t
    return tags

while True:
    proc = os.popen(status_cmd)
    output = proc.readline()
    tag_list = parse_tags(output)
    print tag_list

