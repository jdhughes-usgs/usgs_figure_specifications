import os
import matplotlib.font_manager as mplfm

import spnspecs

print('{} - initializing fonts'.format(spnspecs.__name__))

# load files
pth = os.path.dirname(os.path.abspath(spnspecs.__file__))
pth = os.path.join(pth, 'fonts')
print('loading fonts from..."{}"'.format(pth))

# get list of available font files
font_files = mplfm.findSystemFonts(fontpaths=pth)

# create font list
font_list = mplfm.createFontList(font_files, fontext='otf')

# add Oblique to oblique (italic) fonts
for font in font_list:
    if font.style == 'oblique':
        font.name += ' Oblique'

# write summary of available fonts
print('\navailable fonts:')
for idx, font in enumerate(font_list):
    print('  {} - {}'.format(idx+1, font))

# add files to matplotlib
mplfm.fontManager.ttflist.extend(font_list)