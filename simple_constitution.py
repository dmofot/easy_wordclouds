# # Word Cloud
# =============================
# 
# Generating a square word cloud from the US constitution using default arguments.
#
# Wordcloud (`pip install wordcloud`) requires PIL/Pillow (`pip install pillow`) 
# and numpy (`pip install numpy`) to be installed.
# 
# To install all packages, use `pip install -r requirements.txt`

# Imports
from os import path
from wordcloud import WordCloud

# Set path
d = path.dirname('__file__')

# Read the whole text
text = open(path.join(d, 'constitution.txt')).read()

# Setup and generate wordcloud
# Additional wordcloud parameters here: http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
wc = WordCloud().generate(text)

# Save word cloud to file
wc.to_file(path.join(d, "constitution.png"))

# Display the generated wordcloud image using pillow
image = wc.to_image()
image.show()