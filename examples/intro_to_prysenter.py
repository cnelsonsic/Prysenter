#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
sys.path.extend(('.', '..'))

from prysenter import Prysentation, typewriter, pechakucha

def trans(slide):
    type_speed = 0.02
    return (slide, typewriter(type_speed))

slides = ['{f_green}Intro to Prysenter',
          # Transistion is erroring out after latest upstream merge
          # trans('Prysenter does presentations'),
          'Simple',
          'Minimal',
          '{f_yellow}{s_bright}Quick',
          'Thank You.',]
Prysentation(slides=slides, timeout=pechakucha.timeout).start()
