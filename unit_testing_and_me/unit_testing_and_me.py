#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
sys.path.extend(('.', '..'))

from presentation import Presentation, typewriter

def multiline(*args):
    return '\n'.join(args)
_ = multiline
mu = multiline

def subtitle(*args):
    return ''.join((args[0].title(), '\n', '\n', multiline(*args[1:])))
st = subtitle

def trans(slide):
    type_speed = 0.02
    return (slide, typewriter(type_speed))

slides = [trans(mu('Unit Testing and Me', 'The Charles Nelson Story')),

        trans(st('Smoke Tests',
            "r = myfunc()",
            "assertTrue(r['success'])")),
            # Does the function even run from start to finish without erroring.
            # Call it with the simplest set of data that will exercise the common case.
            # Avoid branches in the code if it is natural
            # Do as little as possible to get the function running from start to finish.
            # FAST

        trans('Testing the Units'),
            # Don't worry what some function 100 calls deep is doing to your data.
            # Only test what the function claims to do.

        trans('Mocking'),
            # return_value, monkeypatching

        trans('Sandbox'),
            # All new tests should use an empty database by default.
            # It's called "legacy" for a reason.

        trans('Test Fixtures'),
            # Set up all the data a test will need
            # All of it.
            # Use no client-data. Clients are wierd.

        trans(mu('Tools','PolicyTool, PaymentsTool')),
            # Makes policies and payments for you
            # also cleans up after itself.

        trans(st('Shared Fixtures',
            'Fast, but bad for R/W',
            'Perfect for Read-Only')),
            # Fast but bad if doing R/W.
            # Perfect for Read-Only tests.

        trans('Fresh Fixtures'),
            # SLOWWWWWWWWWWW
            # In-ram databases make this more tolerable.
            # only option for R/W tests where rolling back
            # the fixture is difficult or impossible.

        trans('Minimal Fixtures'),
            # Don't use PolicyTool.create_policy_term_and_revision.
            # The name is long because the function is slow as a dog.
            # Does your test really need a policy with a named insured and agent?
            # How about bill-whom stuff set?
            # Or even a policy type?
            # Or a billing schedule?
            # Didn't think so.

        trans('Testable vs Untestable'),
            # Some things in BC are untestable. Old accounting for instance.
            # Other things are outside the purview of python unit-tests:
            # HTML/CSS/JS changes, wording changes to a Note, database changes.

        trans('Determinism'),
            # Known input, known output.
            # Known state after processing.

        trans(st('Short Tests',
                '<= 8 lines.',
                'cool story bro, tl;dr, etc.')),
            # Yes, including setup.
            # Unit Tests should not be longer than that.
            # 1 line to check result
            # 1 line to call function
            # 6 lines of setup. Plenty.
            # Is your setup getting long?
            # Generalize it. It should probably be a tool, or part of one.

        trans(st('TestCase for every method',
                'TestCommitRevision',
                'test_with_bad_revision()',
                'test_in_world_of_tomorrow()',
            )),
            # 

        trans(mu('Conditional Tests', 'vs.', 'Guard Assertions')),
        trans(st('Bad:', "if foo in bar:", "self.assertTrue(bar[foo])")),
        trans(st('Good:', 'self.assertTrue(foo in bar)', 'self.assertTrue(bar[foo])')),

        trans(mu('XUnit Patterns:', 'xunitpatterns.com')),
            # A gold-mine of things to do and things to avoid

        ]

Presentation(slides=slides).start()
