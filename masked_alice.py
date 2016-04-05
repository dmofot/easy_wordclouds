# # Word Cloud
# =============================
# 
# Generating a masked word cloud from the text of Alice In Wonderland.
#
# Wordcloud (`pip install wordcloud`) requires PIL/Pillow (`pip install pillow`) 
# and numpy (`pip install numpy`) to be installed.
# 
# To install all packages, use `pip install -r requirements.txt`

# Imports
from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

# Set path
d = path.dirname('__file__')

# Read the whole text
text = open(path.join(d, 'alice.txt')).read()

# Read the mask image
# Taken from: http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

# Setup and generate wordcloud
# Additional wordcloud parameters here: http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=STOPWORDS.add("said")).generate(text)

# Save word cloud to file
wc.to_file(path.join(d, "alice.png"))

# Display the generated wordcloud image using pillow
image = wc.to_image()
image.show()