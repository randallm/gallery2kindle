#!/usr/bin/env python2
# coding: utf-8

import os
import re
import requests
import shutil
import argparse
import bitly

parser = argparse.ArgumentParser(
    description='Takes Imgur gallery and Kindle information; converts into Kindle-optimized gallery webpage.'
)

parser.add_argument('imgur_url',
    metavar='URL',
    help='URL of Imgur gallery'
)


parser.add_argument('gallery_name',
    metavar='Gallery Name',
    help='Title of new, generated gallery'
)

# parser.add_argument('-d',
#     dest='dropbox_dir',
#     help='Dropbox directory (ex: ~/Folder1/Dropbox)'
# )

args = vars(parser.parse_args())

for var, value in args.items():
    # puts all namespace entires into dictionary and uses first dictionary's
    # keys to get new variable names; then takes first dictionary's values
    # and uses them as new variable values
    globals()[var] = value


def imgur(imgur_url, gallery_name):
    # reformat URL
    imgur_url = re.sub('\d$', '', imgur_url)
    if imgur_url.endswith('#'):
        imgur_url = imgur_url[:-1]
    if '/all' not in imgur_url:
        imgur_url = imgur_url + '/all'
    if not imgur_url.startswith('http://'):
        imgur_url = 'http://' + imgur_url

    # find all lines with <img> tags in page
    html = requests.get(imgur_url).content.replace('\t', '').splitlines()
    images = [line for line in html if line.startswith('<img alt="" src="')]

    # reformat lines to links and remove thumbnailing
    images = [i[17:] for i in images]
    images = [fi[:-10] + '.jpg' for fi in images]

    final_html = '''<!doctype html>
<html>
<head>
<title>%s</title>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta charset="utf-8">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script src="http://malsup.github.com/jquery.cycle.all.js"></script>
<script>
$('#gallery').cycle({
    fx: 'none',
    timeout: 0,
    next: '#next',
    prev: '#back'
});
</script>
<style>
/* only tested on Kindle 3; should theoretically work on all 2/3/4 gen */
#gallery img{
    width: 600px;
    height: 675px;
}
</style>
</head>
<body>
<center>
<div id="gallery">''' % (gallery_name)

    for image in images:
        final_html += '<img src="' + image + '">'

    final_html += '''</div>
<a href="javascript:void(0)" id="next">next</a>&nbsp;&nbsp;&nbsp;
<a href="javascript:void(0)" id="back">back</a>'''
    final_html = open(gallery_name + '.html', 'w+').write(final_html)


# def dropbox(dropbox_dir, gallery_name):
#     dropbox_dir = os.path.expanduser(dropbox_dir)

#     shutil.copy2(gallery_name + '.html', dropbox_dir + '/Public/' + gallery_name + '.html')
#     os.remove(gallery_name + '.html')

#     # bitly = bitlyapi.BitLy('your_api_username', 'your_api_key')
#     bitly = bitly.BitLy('randallma', 'R_0d72dc04afb278011bbb2bf4bb15df2b')
#     # res = b.shorten(longUrl='http://dl.dropbox.com/u/your_user_id' + gallery_name + '.html')
#     res = bitly.shorten(longUrl='http://dl.dropbox.com/u/413327/' + gallery_name + '.html')
#     print
#     print 'bit.ly URL: ' + res['url']
#     print


if __name__ == '__main__':
    imgur(imgur_url, gallery_name)
    # if bool(dropbox_dir) == True:
    #     dropbox(dropbox_dir, gallery_name)