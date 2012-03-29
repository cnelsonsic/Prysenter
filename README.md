Prysenter
=========

Prysenter is an absolutely minimal, text-only, terminal-only presentation runner.
It shows a sequence of strings, centered in your terminal.

Installing
----------
Download and run presenter.py for an example of what it looks like.

Usage
-----
Crank the font size on your terminal, run your presentation.

### New Presentations ###
```python
from presentation import Presentation
slides = ['Intro to Prysenter',
          'Prysenter presents',
          'Simple',
          'Minimal',
          'Quick',
          'Thank You.',
          'https://github.com/cnelsonsic/Prysenter']
Presentation(slides=slides).start()
```
