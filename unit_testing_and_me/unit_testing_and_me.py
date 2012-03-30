#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
sys.path.extend(('.', '..'))

from presentation import Presentation

from formatters import multiline as mu
from formatters import subtitle as st
from formatters import code_subtitle as ct

slides = [mu('Unit Testing and Me', 'The Charles Nelson Story'),

        'Where to Start',
        #   Huge project
        #   Deep dependencies
        #   commit_revision: touches a quarter of the codebase.

        'Pick a function',
        #   Preferably back-end to avoid having to construct JSON
        #   Preferably with as few dependent functions as possible

        'setUp()',
        # Set up all the data you need to call your function
        #   Consider turning your setup into a generalized tool.
        # Make sure it returns what it claims to.
        #   result['success']

        st('Smoke Tests',
            "r = myfunc()",
            "assertTrue(r['success'])"),
            # Does the function even run from start to finish without erroring.
            # Call it with the simplest set of data that will exercise the common case.
            # Avoid branches in the code if it is natural
            # Do as little as possible to get the function running from start to finish.
            # FAST

        'Architecture',
        ct('do_thing()',
            'TestDoThing(TestCase)',
            'test_do_thing()',
            'test_do_thing_with_foo()',
            ),

        mu('foo_set_up()',
            'expected = "Bar"',
            'result = do_foo()',
            'assertEqual(expected, ','result)',
            ),
            # setUp() may or may not be literally setUp or setUpClass.
            # You should know the output ahead of time
            #   You should not have to ask the code what the answer is,
            #   if your fixtures are set up deterministically.
            # Call your function, and either check its output or the state of
            #   the universe.

        st('Pythoscope',
            'Test stubs'),
            # Stubs out tests, puts in skips.
            # Will be in Trunk shortly, will bump our total
            #   test count to something like 1200 tests.
            #   One for every function and method.

        'Testing the Units',
            # Don't worry what some function 100 calls deep is doing to your data.
            # Only test what the function claims to do.
            # Presume output from auxilliary functions is good (as long as input is.)
            # You can probably presume current output is good if input is.
            # Manual validation is encouraged.

        mu('One Branch', 'One Test'),
            # For each branch in the function,
            # There should be a test where it goes down that branch.
        mu('test_do_foo_if_bar', 'test_do_foo_if_not_bar', 'etc.'),

        st('Mocking',
                'm = Mock(return_value=4)',
                'm() == 4'),
            # If an auxiliary function is hairy, mock it.
            # If it's outside our control (smtp, vendors), mock it.
            # Pure unit tests will mock everything outside of the
            #   code under tests's control.
            # You can have mock return a value when called like a function
            # You can have it raise an exception

        st('do_foo calls do_bar',
                'do_bar = Mock()'),
            # Have do_bar return exactly what it takes to make do_foo happy.

        mu('Integration Test', 'vs', 'Unit Test'),
            # Most of our tests are integration tests due to reliance
            # on external resources (other code).

        'Sandbox',
            # All new tests should use an empty database by default.
            # It's called "legacy" for a reason.
            # Tools should be created (eventually) to create all the data you need.

        'Test Fixtures',
            # Set up all the data a test will need
            # All of it.
            # Use no client-data. Clients are wierd.
            # Test setup should presume that the data is completely blank.
            # initial.sql

        st('Tools','PolicyTool, PaymentsTool'),
            # Makes policies and payments for you
            # also cleans up after itself.
            # Could have a LinesTool, or a ClaimsTool, things like that.

        st('Shared Fixtures',
            'Fast, but bad for R/W',
            'Perfect for Read-Only'),
            # Fast but bad if doing R/W.
            # Great if you need to do a number of assertions
            #
            # Perfect for Read-Only tests.

        st('Clean Up',
            'setUpClass(cls)',
            'del cls.thing'),
            # I had an SQLA model hanging around on the class
            # That I had set up in setUpClass.
            # It was preventing other tests from running correctly
            # Because it was still on the Class, and not on the class _instance_.

        'Fresh Fixtures',
            # SLOWWWWWWWWWWW
            # In-ram databases make this more tolerable.
            # only option for R/W tests where rolling back
            # the fixture is difficult or impossible.

        'Minimal Fixtures',
            # Don't use PolicyTool.create_policy_term_and_revision.
            # The name is long because the function is slow as a dog.
            # Does your test really need a policy with a named insured and agent?
            # How about bill-whom stuff set?
            # Or even a policy type?
            # Or a billing schedule?
            # Didn't think so.

        'Testable vs Untestable',
            # Some things in BC are untestable. Old accounting for instance.
            # Other things are outside the purview of python unit-tests:
            # HTML/CSS/JS changes, wording changes to a Note, database changes.

        'Determinism',
            # Known input, known output.
            # Known state after processing.

        st('Short Tests',
                '<= 8 lines.',
                'cool story bro, tl;dr, etc.'),
            # Yes, including setup.
            # Unit Tests should not be longer than that.
            # 1 line to check result
            # 1 line to call function
            # 6 lines of setup. Plenty.
            # Is your setup getting long?
            # Generalize it. It should probably be a tool, or part of one.


        mu('Conditional Tests', 'vs.', 'Guard Assertions'),
        st('Bad:', "if foo in bar:", "self.assertTrue(bar[foo])"),
        st('Good:', 'self.assertTrue(foo in bar)', 'self.assertTrue(bar[foo])'),

        mu('XUnit Patterns:', 'xunitpatterns.com'),
            # A gold-mine of things to do and things to avoid

        ]

from shtf import shtf
shtf(slides, __file__)

# import pprint
# slides_and_notes = pprint.pformat(slides)
# with open(__file__+".notes", "w") as f:
#     f.write(slides_and_notes)

Presentation(slides=slides).start()
