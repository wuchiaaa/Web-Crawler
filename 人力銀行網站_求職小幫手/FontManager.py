'''
確認 matplotlib 中的字體有哪些
 --> 幾乎為英文，少有中文
'''

from matplotlib.font_manager import FontManager
import subprocess

mpl_fonts = set(f.name for f in FontManager().ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)