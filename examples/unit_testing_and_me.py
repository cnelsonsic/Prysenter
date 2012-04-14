#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
sys.path.extend(('.', '..'))

from prysenter import Prysentation, pechakucha

from prysenter.formatters import multiline as mu
from prysenter.formatters import subtitle as st
from prysenter.formatters import code_subtitle as ct

slides = [
        mu('Unit Testing and Me',
            'The Charles Nelson Story'),

        'Where to Start',
        #   Huge project
        #   Deep dependencies
        #   commit_revision: touches a quarter of the codebase.

        'Pick a function',
        #   Preferably back-end to avoid having to construct JSON
        #   Preferably with as few dependent functions as possible

        st('Smoke Test',
            "set_up_myfunc()",
            "r = myfunc()",
            "assertTrue(r['success'])"),
            # FAST
            # Does the function even run from start to finish without erroring.
            # Call it with the simplest set of data that will exercise the common case.
            # Avoid branches in the code if it is natural
            # Path of Least Resistance
            # Do as little as possible to get the function running from start to finish.

        #Architecture
        ct('do_thing()',
            'TestDoThing(TestCase)',
            'test_do_thing()',
            'test_do_thing_with_foo()',
            'or test_with_foo()',
            ),
            # Testing do_thing()?
            # Make a test case: "TestDoThing".
            # And make a test method: "test_do_thing"
            #   Its silly, but it placates pythoscope
            #       Will be used to generate test stubs
            #       in trunk, should be in trunk Real Soon Now.
            # Then, if you have a condition you want to test:
            #   Make a test method like "test_do_thing_with_foo".
            #   Or even just "test_with_foo", if you're feeling lazy.

        mu('One Branch', 'One Test'),
            # For each branch in the function,
            # There should be a test where it goes down that branch.
        mu('test_do_foo_if_bar', 'test_do_foo_if_not_bar', 'etc.'),

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
            # tests/test_reports_views.py

#         st('Pythoscope',
#             'Test stubs'),
#             # Stubs out tests, puts in skips.
#             # Will be in Trunk shortly, will bump our total
#             #   test count to something like 1200 tests.
#             #   One for every function and method.

        'Testing the Units',
            # Don't worry what some function 100 calls deep is doing to your data.
            # Only test what the function claims to do.
            # Presume output from auxilliary functions is good (as long as input is.)
            # You can probably presume current output is good if input is.
            # Manual validation is encouraged.

        st('Mocking',
                'm = Mock(return_value=4)',
                'm() == 4'),
            # If an auxiliary function is hairy, mock it.
            # If it's outside our control (smtp, vendors), mock it.
            # Real, pure unit tests will mock everything outside of the
            #   code under tests's control.
            # You can have mock return a value when called like a function
            # You can have it raise an exception

        ct('do_foo calls do_bar',
                'do_bar = Mock()'),
            # Have do_bar return exactly what it takes to make do_foo happy.

        mu('Integration Test', 'vs', 'Unit Test'),
            # Most of our tests are integration tests due to reliance
            # on external resources (other code, databases, remote servers).
            # Integration: Useful, hard to debug, just shows us if the system is broken
            # Unit Tests: Easy to debug.
            #   In a perfect world, if you change a function, only its test should break,
            #   and even then, only the test for whatever branch you edited would break.

        'Sandbox',
            # All new tests should use an empty database by default.
            # It's called "legacy" for a reason.
            # Tools should be created (eventually) to create all the data you need.

        ### Maybe snip? ###
        st('Clean Fixtures',
                'initial.sql',
                'Create data with', 'BC functions',
                'newPolicy, etc'),
            # Set up all the data a test will need
            # All of it.
            # Use no client-data. Clients are wierd.
            # Test setup should presume that the data is completely blank.
            # initial.sql
            #

        st('Tools','PolicyTool, PaymentsTool'),
            # Makes policies and payments for you
            # also cleans up after itself.
            # Could have a LinesTool, a ClaimsTool, a ContactsTool, things like that.

        st('Shared Fixtures',
            'setUpClass()',
            'Perfect for Read-Only',
            'Fast, but bad for R/W',
            ),
            # Fixtures shared between multiple test functions,
            # and possibly multiple TestCases.
            # Perfect for Read-Only tests.
            # Great if you need to do a number of assertions
            # Fast but bad if doing R/W.
            # Tends to be hard to clean up consistently.

        st('Clean Up',
            'setUpClass(cls)',
            'del cls.thing'),
            # I had an class instance hanging around on the testcase class itself
            #   that I had set up in setUpClass.
            # It was preventing other tests from running correctly
            #   because it was still on the Class, and not on the class _instance_.
            # Things were staying around past the life of the instance,
            #   and generally causing havoc.
            # If a testcase runs fine on its own, but not in
            #   the same run as others, there's probably
            #   something that isn't getting cleared.

        st('Fresh Fixtures',
                'Slow',
                'Good for R/W',),
            # SLOWWWWWWWWWWW
            # In-ram databases make this more tolerable.
            # Only option for R/W tests where rolling back
            # the fixture is difficult, prone to error, or impossible.

        'Minimal Fixtures',
            # Don't use PolicyTool.create_policy_term_and_revision.
            # The name is long because the function is slow as a dog.
            # Does your test really need a policy with a named insured and agent?
            # How about bill-whom stuff set?
            # Or even a policy type?
            # Or a billing schedule?
        ### END Maybe snip? ###

        'Testable vs Untestable',
            # Some things in BC are untestable. Old accounting for instance.
            # Other things are outside the purview of python unit-tests:
            # HTML/CSS/JS changes, wording changes to a Note, data changes.
            # All code changes should be accompanied by tests that cover it.

        'Determinism',
            # Known input, known output.
            # Known state after processing.

        st('Short Unit Tests',
                '<= 8 lines.',
                'cool story bro, tl;dr, etc.'),
            # Yes, including setup.
            # Unit Tests should not be longer than that.
            # 1 line to check result
            # 1 line to call function
            # 6 lines of setup. Plenty.
            # Is your setup getting long?
            # Generalize it. It should probably be a tool, or part of one.
            # See also: tests/test_reports_views.py

        mu('Conditional Tests', 'vs.', 'Guard Assertions'),
        st('Bad:', "if bar in foo:", "self.assertTrue(foo[bar])"),
        st('Good:', 'self.assertTrue(bar in foo)', 'self.assertTrue(bar[foo])'),
            # If something is possible and you are already accounting for it,
            # it should probably be a guard assertion instead of a conditional.

        mu('XUnit Patterns:', 'xunitpatterns.com'),
            # A gold-mine of things to do and things to avoid

        ]

from prysenter.shtf import shtf
shtf(slides, __file__)

# import pprint
# slides_and_notes = pprint.pformat(slides)
# with open(__file__+".notes", "w") as f:
#     f.write(slides_and_notes)

Prysentation(slides=slides, timeout=pechakucha.timeout).start()
