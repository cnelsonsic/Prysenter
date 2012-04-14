#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def multiline(*args):
    return '\n'.join(args)

def subtitle(*args):
    return ''.join((args[0].title(), '\n', '\n', multiline(*args[1:])))

def code_subtitle(*args):
    return ''.join((args[0], '\n', '\n', multiline(*args[1:])))

speaker_notes = {}
def speaker_note(*args):
    notes = args[-1]
    global speaker_notes
    speaker_notes[args[:-1]] = notes

    return args[-1]
