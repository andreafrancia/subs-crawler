import zipfile
from StringIO import StringIO

from urllib2 import urlopen, URLError
from urlparse import urljoin

def main():
    import sys
    class http:
        def get(self, url):
            print url
            try:
                return urlopen(url).read()
            except URLError, e:
                raise IOError('URL: %s, %s' % (url, repr(e)))
    getsubs = GetSubs(http(), 
                      place_file)
    getsubs.run(*sys.argv[1:])

def place_file(filename, contents):
    with file(filename, 'wb') as f:
        f.write(contents)

class GetSubs:
    def __init__(self, http, place_file):
        self.http = http
        self.place_file = place_file

    def run(self, *args):
        filename=args[0]

        (  
        FigureOutEpisodeCoords(
            FigureOutSearchUrl(
         FindLinkToDetailsPage(self.http,
            LocateUrlOfZipFile(self.http,
           DownloadZipContents(self.http, 
                 WriteSubsFile(subs_filename(filename),
                               self.place_file)
                               )))))
        )(filename)

def subs_filename(filename):
    import os
    root, _ = os.path.splitext(filename)
    return root + '.srt'

class FigureOutEpisodeCoords:
    def __init__(self, output):
        self.output = output
    def __call__(self, filename):
        showname, season, episode = parse(filename)
        self.output(showname, season, episode)
        
class WriteSubsFile:
    def __init__(self, filename, output):
        self.filename = filename
        self.output = output
    def __call__(self, file_contents):
        self.output(self.filename, file_contents)

class FigureOutSearchUrl:
    def __init__(self, output):
        self.output = output
    def __call__(self, showname, season, episode):
        search_results_url = search_url_for(showname, season, episode)
        self.output(search_results_url)

class FindLinkToDetailsPage:
    def __init__(self, http, output):
        self.http = http
        self.output = output
    def __call__(self, search_results_url):
        search_results_page = self.http.get(search_results_url)
        link_to_details_page = pick_first_details_link(search_results_page)
        subsfile_details_url = urljoin(search_results_url, link_to_details_page)
        self.output(subsfile_details_url)

class LocateUrlOfZipFile:
    def __init__(self, http, output):
        self.http = http
        self.output = output 

    def __call__(self, subsfile_details_url):
        subsfile_details_page = self.http.get(subsfile_details_url)
        link_to_zipfile = extract_zip_link(subsfile_details_page)
        url_to_zipfile = urljoin(subsfile_details_url, link_to_zipfile)
        self.output(url_to_zipfile)
                 
class DownloadZipContents:
    def __init__(self, http, output):
        self.http = http
        self.output = output
    def __call__(self, url_to_zipfile):
        zip_file_contents=self.http.get(url_to_zipfile)
        zipped_file_contents=extract_first_zipped_file(zip_file_contents)
        self.output(zipped_file_contents)

class Parser:
    def __init__(self, outbox):
        self.outbox = outbox
    def parse(self,filename):
        result = parse(filename)
        self.outbox(result)


def parse(filename):
    import re

    match=re.finditer("(.*)S(..)E(..)", filename).next()

    showname = match.group(1).replace('.',' ').strip()
    season   = match.group(2).lstrip('0')
    episode  = match.group(3).lstrip('0')

    return (showname, season, episode)

def extract_first_zipped_file(zip_file_contents):
    zip_file = zipfile.ZipFile(StringIO(zip_file_contents), 'r')
    for name in zip_file.namelist():
        zipped_file=zip_file.open(name).read()
        break
    zip_file.close()
    return zipped_file

class HtmlPage:
    def __init__(self, contents):
        from lxml.html.soupparser import fromstring
        self.dom=fromstring(contents)
    def xpath(self,expr):
        return self.dom.xpath(expr)

def extract_zip_link(page_contents):
    return get_first_xpath(page_contents, '//a[h1/text()="Download"]/@href')

def get_first_xpath(page_contents, expr):
    page=HtmlPage(page_contents)
    results = page.xpath(expr)

    try:
        return results[0]
    except IndexError:
        raise RuntimeError(page_contents)

def pick_first_details_link(page_contents):
    return get_first_xpath(page_contents, 
                           "//a[starts-with(@href,'/en/ppodnapisi/podnapis')]/@href")

from urllib import quote_plus
def search_url_for(showname, season, episode):
    return ("http://www.sub-titles.net/"
            "en/ppodnapisi/search?"
            "tbsl=3&"
            "asdp=1&"
            "sK=%(showname)s&" # showname
            "sM=0&"
            "sJ=9&" # language
            'sO=desc&'
            'sS=time&'
            "submit=Search&"
            "sAKA=1&"
            'sTS=%(season)s&'
            'sTE=%(episode)s&'
            "sY=&"
            "sR=&" # Release
            "sT=1"
        % {'showname':quote_plus(showname),
           'season':season,
           'episode': episode})

if __name__ == '__main__':
    main()

