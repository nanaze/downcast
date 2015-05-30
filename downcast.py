"""Downcast will fetch an RSS feed and write out the paths to the media
files (MP3, etc) to standard out.

Example:
downcast.py http://feeds.thisamericanlife.org/talpodcast

This can be used in conjunction with xargs/wget to download podcasts.

Example:
downcast.py <url> | xargs wget
"""

import sys
import urllib2
import xml.sax



def main():
  if len(sys.argv) != 2:
    sys.exit(__doc__)

  url = sys.argv[1]
  req = urllib2.urlopen(url)
  handler = RssHandler()
  result = xml.sax.parse(req, handler)

class RssHandler(xml.sax.handler.ContentHandler):

  def startElement(self, name, attrs):
    if name == 'enclosure':
      if attrs.has_key('url'):
        print attrs.getValue('url')

if __name__ == '__main__':
  main()
