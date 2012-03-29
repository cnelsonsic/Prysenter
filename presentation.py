#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os

class Presentation(object):
    '''Show a text-based presentation in your terminal.
    Make sure your font size is cranked to 72 or something
    equally ridiculous.
    Fair warning: Long, verbose slides are NOT SUPPORTED.
    Remember: smaller, quicker hunks of info to remind
    people what you are talking about.
    '''
    def __init__(self, slides):
        '''Initialize our presentation.
        Takes a list of slide strings like:
        >>> Presentation(['Why prysenter is cool.', 'It lets you do tiny slides.'])
        '''
        self.slides = list(slides)
        self.current_slide = self.slides[0]

    def __del__(self):
        # Turning the cursor on here so we get our cursor back
        # even on errors.
        self.cursor()

    def cursor(self, state='on'):
        '''State should be 'on' or 'off'.'''
        os.system('setterm -cursor %s' % state)

    @staticmethod
    def get_term_size():
        '''Gets the size of your terminal. May not work everywhere. YMMV.'''
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)

    @staticmethod
    def strip_ws(string):
        '''Strip leading whitespace around multiline strings.'''
        return '\n'.join((line.strip() for line in string.split("\n")))

    @staticmethod
    def clear():
        '''Clears the screen. Should work everywhere.'''
        os.system('cls' if os.name=='nt' else 'clear')

    @staticmethod
    def wait():
        '''Wait for the presenter to hit "Enter", then return.'''
        # TODO: Could be a fancy input loop and wait for any input at all?
        raw_input()

    def do_slide(self, slide=None):
        '''Print the given slide to the terminal.'''
        # We weren't passed a specific slide, just show the current one.
        if not slide:
            slide = self.current_slide

        rows, cols = self.get_term_size()

        # How many rows tall is the slide?
        slide_height = len(slide.split("\n"))

        # Determine our top margin,
        # subtracting the slide height if it's more than one line
        top_margin = (rows-(slide_height if slide_height > 1 else 0))/2

        # Print newlines to bump the slide text downward enough
        # Remember that print adds a new line, hence -1.
        print "\n"*(top_margin-1)

        # Strip whitespace and center it horizontally.
        slide = self.strip_ws(slide).center(cols)
        print slide

    def start(self):
        '''Start the presentation.
        This will loop as long as there are slides left.'''
        # This is a while instead of a for in case we implement slides that can
        # point to other slides. ¯\°_o/¯
        self.cursor(state='off')
        while self.slides:
            self.clear()
            self.do_slide()
            self.wait()

            try:
                # Next slide!
                s = self.slides # Shorthand for later.
                self.current_slide = s[s.index(self.current_slide)+1]
            except IndexError:
                # Out of slides!
                # Clear the screen before we end the presentation so junk isnt left over.
                self.clear()
                break
        self.cursor()

if __name__ == "__main__":
    slide3 = '''So as I was saying,
    there are lots of things that I would like to talk about.
    One of which is stuff.
    This slide is plain lucky.'''

    slide4 = '''Oh god what are you doing.
    Why is this slide so long?!
    What is wrong with you?!!?
    Just put it on different slides.
    Why don't you just fire up vim.
    You obviously have a lot to say.
    You should read the documentation.
    You know they're already bored.'''

    p = Presentation(["asfasdf", "werqwerqewrqwerqwer", slide3, slide4])
    p.start()
