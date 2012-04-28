#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
sys.path.extend(('.', '..'))

from prysenter import Prysentation
from prysenter import ODPExtractor
from prysenter.formatters import multiline

slides = [multiline('The following slides',
                    'Are imported from',
                    'A LibreOffice presentation.')]

slides.extend(ODPExtractor('tests/Untitled 1.odp').all_slides)

from prysenter.shtf import shtf
shtf(slides, __file__)

Prysentation(slides=slides).start()
