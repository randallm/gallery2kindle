gallery2kindle
==============
Python script that takes Imgur galleries and embeds them into blank web pages optimally formatted for Kindle web browser. **NOT PERFECT**, but still better than the standard 'mobile' Imgur interface; images 'bump' down a little with each image change, simply readjust using the 4-way directional pad.

If using Dropbox storage, please change the bit.ly API key and Dropbox user ids to one other than the examples given in gallery2kindle.py.

Usage:

gallery2kindle.py [-h help] [-k Kindle version] [-n name of gallery] [-d Dropbox
directory] [Imgur Gallery URL]

Gallery names with white space in them should be enclosed within quotes to avoid unrecognized argument errors.

Example:

gallery2kindle.py -k kindle3 -n Cats! [-d ~/Dropbox] http://imgur.com/a/gallery

License:

Gallery2Kindle Copyright (c) 2012 Randall Ma
Python bit.ly wrapper Copyright (c) 2010 Fabian Neumann
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. The name of the author may not be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.