#!/usr/bin/env python2
# coding: utf-8

import argparse
import re
import requests

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


args = vars(parser.parse_args())

for var, value in args.items():
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
    max-width: 600px;
    max-height: 675px;
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


if __name__ == '__main__':
    imgur(imgur_url, gallery_name)
