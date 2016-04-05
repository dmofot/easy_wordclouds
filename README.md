# wordcloud

A few examples of generating word clouds in Python.

## Installation

### Downloading the repo
There are three ways to download the repo from GitLab.  First option is using git and ssh to clone the repo in your terminal:  
`git clone git@github.com:dmofot/easy_wordclouds.git`

Second option is using git and https to clone the repo in your terminal:  
`git clone https://github.com/dmofot/easy_wordclouds.git`

The third option is useful if you don't have `git` installed.  Simply download the entire repo as a [zip file](https://github.com/dmofot/easy_wordclouda/archive/master.zip) and unzip it.

Once the repo is downloaded, you can move into the project directory:  
`cd wordcloud`

### Installing Python Environment
These examples were tested on Mac OS X 10.11.3 El Capitan, using Python version 2.7.11.  If you are on a Mac, Python version 2.7.10 should already be installed on your system and will probably work.  On Windows, you'll need to install Python from [python.org](https://www.python.org/downloads/windows/).  If your version of Python doesn't have `pip` installed, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run `python get-pip.py`.  This will install or upgrade pip. Additionally, it will install setuptools and wheel if they’re not installed already.

These examples should preferably be run in a virtualenv to avoid installing a bunch of project specifc packages.  To install virtualenv, simply run:  
`pip install virtualenv`  

Setup your virtualenv project:  
`virtualenv venv`

Activate your virtualenv project:  
`source venv/bin/activate`

You should see a (venv) appear at the beginning of your terminal prompt indicating that you are working inside the virtualenv. Now install the project's required packages:  
`pip install -r requirements.txt`

Alternatively, instead of using the requirements.txt, you can install the packages individually:  
`pip install numpy`
`pip install pillow`
`pip install wordcloud`

When you are finished running through the examples below, don't forget to deactivate the virtualenv:  
`deactivate`

## Running the examples
These examples are based on the examples provided in the [wordcloud](https://github.com/amueller/word_cloud) package, but hopefully somewhat easier and more straightforward.

### Simple word cloud
The simple word cloud example takes the text from the US Constitution (`constitution.txt`) and builds a square word cloud with default settings.  The script will save the word cloud to a file called `constitution.png` and will also display the image.  To run the simple example:  
`python simple_constitution.py`

### Masked word clouds
There are two examples for creating a masked word cloud.  One is based off the text from Alice In Wonderland (`alice.txt`) and the other is based off the script text from the Star Wars movie "A New Hope" (`a_new_hope.txt`).  These examples build word clouds that fit within a masked image (`alice_mask.png` or `stormtrooper_mask.png`) with additional parameter settings, e.g. background, mask, stopwords, etc.  The script will save the masked word cloud to an image file (`alice.png` or `a_new_hope.png`).  It will also display the image.

To run the masked alice example:  
`python masked_alice.py`

To run the masked star wars example:  
`python masked_star_wars.py`

## Example Outputs
Simple word cloud example using the Constitution:  
![Simple Word Cloud - Constitution](/example_pngs/constitution.png)  

Masked word cloud example using Alice In Wonderland:  
![Masked Word Cloud - Alice](/example_pngs/alice.png)  

Masked word cloud example using script from the Star Wars movie "A New Hope":  
![Masked Word Cloud - Star Wars](/example_pngs/a_new_hope.png)