#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''Generate a text file suitable for doing a presentation with less.
Specifically for when things go very, very wrong and you have to quickly
recover where you were with minimal effort.'''

def shtf(slides, filename="presentation"):
    with open(filename+".shtf", 'w') as f:
        for slide in slides:
            f.write("\n"*10)
            f.write('\n'.join((line.center(30) for line in slide.split("\n"))))
