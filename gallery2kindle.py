#!/usr/bin/python2.7

# TODO:
# fix code to conform to style guide (http://www.python.org/dev/peps/pep-0008/)
# change width of webpage to account for kindle scrolling size
# add bit.ly shortening functionality
# add local image mirror functionality

import os
import re
import urllib2
import shutil
import argparse

parser = argparse.ArgumentParser(description='Takes Imgur gallery and Kindle information; converts into Kindle-optimized gallery webpage.')
parser.add_argument('imgur_url', metavar='URL', help='URL of Imgur gallery')
parser.add_argument('-k', dest='kindle_type', default='3', help='Kindle model (defaults to Kindle 3); possible values include 1, 2, 3 & dx')
parser.add_argument('-n', dest='gallery_name', default='Gallery', help='Name of new, generated gallery')
parser.add_argument('-d', dest='dropbox_dir', help='Dropbox directory (ex: ~/Folder1/Dropbox)')
args = vars(parser.parse_args())

for var, value in args.items():
    # puts all namespace entires into dictionary and uses first dictionary's keys to get new variable names; then takes first dictionary's values and uses them as new variable values 
    globals()[var] = value

def imgur(imgur_url, kindle_type, gallery_name):
    imgur_url = re.sub('\d$', '', imgur_url)
    if imgur_url.endswith('#'):
        imgur_url = imgur_url[:-1]
    if '/all' not in imgur_url:
        imgur_url = imgur_url + '/all'
    if imgur_url.startswith('http://') == False:
        imgur_url = 'http://' + imgur_url

    imgur_url = urllib2.urlopen(imgur_url).read().splitlines()
      
    imgur_url = [line for line in imgur_url if line.startswith('<img alt="" src="')]
    imgur_url = '\n'.join(imgur_url)
    imgur_url = re.findall(r'(https?://[^\s]+)', imgur_url)

    number_urls = 0
    while number_urls < len(imgur_url):
        if imgur_url[number_urls].endswith('s.jpg"/>'):
            imgur_url[number_urls] = imgur_url[number_urls][:-8] + '.jpg'
        elif imgur_url[number_urls].endswith('s.png"/>'):
            imgur_url[number_urls] = imgur_url[number_urls][:-8] + '.png'
        elif imgur_url[number_urls].endswith('s.gif"/>'):
            imgur_url[number_urls] = imgur_url[number_urls][:-8] + '.gif'
        else:
            pass
        number_urls = number_urls + 1

    print imgur_url

    for url in imgur_url:
        url = url[:-7]

    # Add kindle res info //still need to account for 'page down' size
    if kindle_type == '3':
        kindle_width = '632'
        kindle_height = '800'

    final_html = '<!doctype html><title>%s - Gallery2Kindle</title><style>img{max-width:100%%;max-height:100%%;}div{width:%spx;height:%spx;}</style><div><h1>%s</h1></div>' % (gallery_name, kindle_width, kindle_height, gallery_name)
    for url in imgur_url:
        final_html = final_html + '<div><img src="' + url + '"></div>'
    final_html = open(gallery_name + '.html', 'w+').write(final_html)

def dropbox(dropbox_dir, gallery_name):
    dropbox_dir = os.path.expanduser(dropbox_dir)

    shutil.copy2(gallery_name + '.html', dropbox_dir + '/Public/' + gallery_name + '.html')
    os.remove(gallery_name + '.html')

if __name__ == '__main__':
    imgur(imgur_url, kindle_type, gallery_name)
    if dropbox_dir == True:
        dropbox(dropbox_dir, gallery_name)