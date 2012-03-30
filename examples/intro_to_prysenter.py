#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
sys.path.extend(('.', '..'))

from presentation import Presentation, typewriter

def trans(slide):
    type_speed = 0.02
    return (slide, typewriter(type_speed))

slides = ['{f_green}Intro to Prysenter',
          trans('Prysenter does presentations'),
          'Simple',
          'Minimal',
          '{f_yellow}{s_bright}Quick',
          'Thank You.',]
Presentation(slides=slides).start()
