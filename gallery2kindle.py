#!/usr/bin/python2.7

# TODO:
# fix code to conform to style guide (http://www.python.org/dev/peps/pep-0008/)
# change width/height dynamically to conform with kindle web browser screen real estate
# add dropbox + bit.ly functionality
# add local image mirror functionality

import re
import urllib2
import os

class gallery2kindle(object):

	def __init__(self):
		self.numberlines = 0
		self.numberurls = 0

	def imgurfetch(self):
		self.imgur_url = raw_input("Imgur Gallery URL [http://imgur.com/a/gallerycode] > ")
		
		# strips and formats gallery url
		self.imgur_url = re.sub('\d$', '', self.imgur_url)
		if self.imgur_url.endswith('#'):
			self.imgur_url = self.imgur_url[:-1]
		if "/all" not in self.imgur_url:
			self.imgur_url = self.imgur_url + '/all'
		if self.imgur_url.startswith('http://') == False:
			self.imgur_url = 'http://' + self.imgur_url
		
		# grabs image links from gallery
		self.imgur_url = urllib2.urlopen(self.imgur_url).read()
	
		self.imgur_url = self.imgur_url.splitlines()
		self.imgur_url = [line for line in self.imgur_url if '<img id="thumb--' and 's.jpg' in line] # imgur doesn't care about file extensions as long as they're valid image extensions
 		self.imgur_url = '\n'.join(self.imgur_url)
		self.imgur_url = re.findall(r'(https?://[^\s]+)', self.imgur_url)	
	
		# changes thumbnail links to normal links
		while self.numberurls < len(self.imgur_url):
			if self.imgur_url[self.numberurls].endswith('s.jpg"'):
				self.imgur_url[self.numberurls] = self.imgur_url[self.numberurls][:-6] + '.jpg'
			else:
				pass
			self.numberurls = self.numberurls + 1

	def imgurembed(self):
		# Add kindle res info //UNIMPLEMENTED
		self.kindletype = raw_input("Kindle Type [3, 4, DX]")

		if self.kindletype == "3" or self.kindletype == "4":
			self.kindleres = "800"

		self.galleryname = raw_input("Gallery Title: ")
		self.gallerynameheader = raw_input("Gallery Title --> Header in Web Page [no] > ")

		self.finalhtml = '<!doctype html>\n<html lang="en">\n<head>\n\t<title>"%s - Gallery2Kindle"</title>\n\t' % self.galleryname

		self.finalhtml = self.finalhtml + '<style>div{height: %spx;}</style>\n</head>\n<body>' % self.kindleres
		for url in self.imgur_url:
			self.finalhtml = self.finalhtml + '\n<div>\n\t<img src="' + url + '" alt="">\n</div>'
		self.finalhtml = self.finalhtml + '\n</body>\n</html>'
		
		self.htmlfile = open('gallery.html', 'w+').write(self.finalhtml)

script = gallery2kindle()
script.imgurfetch()
script.imgurembed()
