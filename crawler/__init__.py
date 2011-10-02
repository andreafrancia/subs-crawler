from urllib import urlopen
import shutil
from contextlib import closing
import zipfile
from StringIO import StringIO

class GetSubs:
    def __init__(self, http, destination):
        self.destination = destination
        self.http = http

    def run(self, showname, season, episode):
        zip_file_contents=self.http.get('/zip-file')

        subtitles_file=extract_first_zipped_file(zip_file_contents)

        self.destination.place_file(named='subtitles.srt',
                                    contents=subtitles_file)

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
    page=HtmlPage(page_contents)
    return page.xpath('//a[h1/text()="Download"]/@href')[0]

def pick_first_details_link(page_contents):
    page=HtmlPage(page_contents)
    return page.xpath("//a[starts-with(@href,'/en/ppodnapisi/podnapis')]/@href")[0]

