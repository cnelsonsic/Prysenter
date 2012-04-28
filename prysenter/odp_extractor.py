
import zipfile
from bs4 import BeautifulSoup
from formatters import multiline, subtitle

TITLE_NAME = 'AL1T0' # Default title slide layout name.

class ODPExtractor(object):
    '''This class takes a given odp file and parses it for content meaningful
    to Prysenter.'''

    def __init__(self, odp):
        with zipfile.ZipFile(odp) as myzip:
            if 'content.xml' not in myzip.namelist():
                raise ValueError("Passed zipfile did not contain ODF content.")

            self.odp_file_content = myzip.read('content.xml')

        self.all_slides = []
        self.convert()

    def convert(self):
        '''Returns a list of slides suitable for prysenter.'''
        soup = BeautifulSoup(self.odp_file_content)

        self.all_slides = []

        # Get all the slides
        for slide in soup.find_all('draw:page'):
            current_slide = []

            title_slide = False

            # Get all lines in the slide
            for text in slide.find_all('draw:text-box'):
                page_layout = 'presentation:presentation-page-layout-name'
                try:
                    if text.parent.parent[page_layout] == TITLE_NAME:
                        title_slide = True
                except KeyError:
                    # If the text box's grandparent has no page layout
                    # attribute, then it isn't a title slide.
                    pass

                line = text.get_text()
                if line:
                    current_slide.append(line)

            if len(current_slide) >= 1:
                # Pick which formatting function to use
                if title_slide:
                    # If it's a title slide, it should be subtitled.
                    func = subtitle
                else:
                    # If it's any other slide, it can be multiline'd.
                    func = multiline
                current_slide = func(*current_slide)

            # If it's not empty, add it to the presentation.
            if current_slide:
                self.all_slides.append(current_slide)

        return self.all_slides


def main():
    '''A quick test method to make sure everything's probably working.'''
    my_presentation = ODPExtractor('tests/Untitled 1.odp').all_slides
    for slide in my_presentation:
        print
        print slide

if __name__ == "__main__":
    main()



