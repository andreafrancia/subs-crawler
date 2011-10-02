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

        zip_file = zipfile.ZipFile(StringIO(zip_file_contents), 'r')
        for name in zip_file.namelist():
            zipped_file=zip_file.open(name).read()
            break
        zip_file.close()
        
        self.destination.place_file(named='subtitles.srt',
                                    contents=zipped_file)

class HtmlPage:
    def __init__(self, contents):
        from lxml.html.soupparser import fromstring
        self.dom=fromstring(contents)
    def xpath(self,expr):
        return self.dom.xpath(expr)

def extract_zip_link(page_contents):
    page=HtmlPage(page_contents)
    return page.xpath('//a[h1/text()="Download"]/@href')[0]

def download_and_unpack_subtitles_file(url, dest_name):
    zip_file_contents = readurl(url)
    unpack_all_files_as(zip_file_contents, dest_name)

def unpack_all_files_as(zip_file_contents, dest_name):
    for zipped_file in all_zipped_file_in(zip_file_contents):
        with zipped_file, file(dest_name,'w') as dest:
            shutil.copyfileobj(zipped_file, dest)

def readurl(url):
    with closing(urlopen(url)) as f:
        return f.read()

def all_zipped_file_in(zipfile_contents):
    zipstream = zipfile.ZipFile(StringIO(zipfile_contents))
    for name in zipstream.namelist():
        yield zipstream.open(name)

def pick_first_details_link(page_contents):
    page=HtmlPage(page_contents)
    return page.xpath("//a[starts-with(@href,'/en/ppodnapisi/podnapis')]/@href")[0]

