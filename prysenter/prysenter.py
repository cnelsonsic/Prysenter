#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
import time
import sys
from select import select

# Import Color support module, uses Colorama
import colors

SHAMELESS_ADVERTISING = "Prysenter\nhttp://git.io/prysenter"
GOBACK = ("\x1bOM", ',', '<', 'h', 'k', '[', '\\')

def typewriter(duration_between_key):
    def transition(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            if not c.isspace():
                time.sleep(duration_between_key)
        sys.stdout.write('\n')
    return transition

def no_transition(text):
    print text

class Prysentation(object):
    '''Show a text-based presentation in your terminal.
    Make sure your font size is cranked to 72 or something
    equally ridiculous.
    Fair warning: Long, verbose slides are NOT SUPPORTED.
    Remember: smaller, quicker hunks of info to remind
    people what you are talking about.
    '''
    def __init__(self, slides, timeout=None):
        '''Initialize our presentation.
        Takes a list of slide strings like:
        >>> Prysentation(['Why prysenter is cool.', 'It lets you do tiny slides.'])
        '''
        self.slides = list(slides)
        self.timeout = timeout
        self.current_slide = self.slides[0]
        height, width = self.get_term_size()
        for slide in self.slides:
            self.checklen(slide, width)

    def __del__(self):
        # Turning the cursor on here so we get our cursor back
        # even on errors.
        self.cursor()
        if colors.HAS_COLORS:
            colors.deinit()

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
    def center(string, width):
        '''Center all lines of a string horizontally.'''
        if colors.HAS_COLORS:
            return colors.center(string, width)
        else:
            return  '\n'.join((line.center(width) for line in string.split("\n")))

    def checklen(self, slide, maxlen=20):
        for line in slide.split("\n"):
            if len(line) > maxlen:
                self.clear()
                raise Exception("%s was too long." % slide)

    @staticmethod
    def clear():
        '''Clears the screen. Should work everywhere.'''
        os.system('cls' if os.name=='nt' else 'clear')

    def input(self):
        if not self.timeout:
            return raw_input()
        else:
            rlist, _, _ = select([sys.stdin], [], [], self.timeout)
            if rlist:
                return sys.stdin.readline()
            else:
                return ""

    def wait(self):
        '''Wait for the presenter to hit "Enter", then return.'''
        # TODO: Could be a fancy input loop and wait for any input at all?

        input_ = self.input()
        if input_ in GOBACK:
            self.prev_slide()
            self.prev_slide()

    def curr_slide_num(self):
        return self.slides.index(self.current_slide)

    def next_slide(self):
        self.current_slide = self.slides[self.curr_slide_num()+1]

    def prev_slide(self):
        self.current_slide = self.slides[self.curr_slide_num()-1]

    def do_slide(self, slide=None):
        '''Print the given slide to the terminal.'''
        # We weren't passed a specific slide, just show the current one.
        if not slide:
            transition = no_transition
            if len(self.current_slide) == 2:
                slide, transition = self.current_slide
            else:
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

        # If colors are enabled, replace formatting with ANSI color output.
        # Otherwise, color tags are stripped.
        slide = slide.format(**colors.COLOR_DICT)

        # Strip whitespace and center it horizontally.
        slide = self.center(self.strip_ws(slide), cols)

        transition(slide)

    def start(self):
        '''Start the presentation.
        This will loop as long as there are slides left.'''

        if colors.HAS_COLORS:
            # Colorize Output via Colorama, autoreset enabled so
            # text returns to original color after each slide.
            colors.init(autoreset=True)

        # Tack on our advertising slide:
        self.slides.append(SHAMELESS_ADVERTISING)

        # Turn off the cursor on linux machines.
        self.cursor(state='off')

        # This is a while instead of a for in case we implement slides that can
        # point to other slides. ¯\°_o/¯
        while self.slides:
            self.clear()
            self.do_slide()
            try:
                self.wait()
            except KeyboardInterrupt:
                break

            try:
                # Next slide!
                self.next_slide()
            except IndexError:
                # Loop around
                if self.curr_slide_num() > 0:
                    self.current_slide = self.slides[0]
                if self.curr_slide_num() < 0:
                    self.current_slide = self.slides[-1]

        # Clear the screen before we end the presentation so junk isnt left over.
        self.clear()
        self.cursor()

if __name__ == "__main__":
    slide3 = '''So as I was saying,
    there are lots of things that I would like to talk about.
    One of which is stuff.
    This slide is plain lucky.'''

    slide4 = '''Oh {f_blue}god{f_reset} what are you doing.
    Why is this slide so long?!
    What is wrong with you?!!?
    Just put it on different slides.
    Why don't you just fire up vim.
    You obviously have a lot to say.
    You should read the documentation.
    You know they're already bored.'''

    p = Prysentation(["{f_red}asfasdf", "werqwerqewrqwerqwer", slide3, slide4])
    p.start()
