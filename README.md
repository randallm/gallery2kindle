gallery2kindle
==============
Python script that takes Imgur galleries and embeds them into blank web pages optimally formatted for Kindle web browser. Not perfect, but still better than the standard 'mobile' Imgur interface; images 'bump' down a little with each image change, simply readjust using the 4-way directional pad.

If using Dropbox storage, please change the bit.ly API key and Dropbox user ids to one other than the examples given in gallery2kindle.py.

Usage:
------

gallery2kindle.py [-h help] [-k Kindle version] [-n name of gallery] [-d Dropbox
directory] [Imgur Gallery URL]

Gallery names with white space in them should be enclosed within quotes to avoid unrecognized argument errors.

Example:
--------

gallery2kindle.py -k kindle3 -n Cats! [-d ~/Dropbox] http://imgur.com/a/gallery

Todo:
-----

* Make pictures match screen space
 * only button from keyboard that appears to register on page is spacebar as shown on this [slideshow](http://python-for-humans.heroku.com/#1)
 * look into viewport <meta> tag

License:
--------

Gallery2Kindle Copyright (c) 2012 Randall Ma - BSD 3-clause

Python bit.ly wrapper Copyright (c) 2010 Fabian Neumann - BSD 3-clause