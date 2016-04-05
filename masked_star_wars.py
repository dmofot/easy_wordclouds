# # Word Cloud
# =============================
# 
# Generating a masked word cloud from the Star Wars movie script "A New Hope".
# This version uses the recolor method and custom coloring functions.
#
# Wordcloud (`pip install wordcloud`) requires PIL/Pillow (`pip install pillow`) 
# and numpy (`pip install numpy`) to be installed.
# 
# To install all packages, use `pip install -r requirements.txt`

# Imports
from os import path
from PIL import Image
import numpy as np
import random
from wordcloud import WordCloud, STOPWORDS

# Function to create grey colors
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# Set path
d = path.dirname(__file__)

# Read the mask image
# Taken from: http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
sw_mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

# Movie script of "A New Hope" from: http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
# May the lawyers deem this fair use
text = open("a_new_hope.txt").read()

# Preprocessing to cleanup the text
text = text.replace("HAN", "Han")
text = text.replace("LUKE'S", "Luke")

# Add movie script specific stopwords
stopwords = STOPWORDS.copy()
stopwords.add("int")
stopwords.add("ext")

# Setup and generate word cloud
wc = WordCloud(max_words=1000, mask=sw_mask, stopwords=stopwords, margin=10, random_state=1).generate(text)

# Store default colored image, recolor, and save
default_colors = wc.to_array()
wc.recolor(color_func=grey_color_func, random_state=3)
wc.to_file("a_new_hope.png")

# Display the generated wordcloud image using pillow
image = wc.to_image()
image.show()