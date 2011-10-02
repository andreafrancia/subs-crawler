from urllib import urlopen
import shutil
from contextlib import closing
import zipfile
from StringIO import StringIO

def extract_zip_link(page):
    xpath_to_use='//a[h1/text()="Download"]/@href'
    from lxml.html.soupparser import fromstring
    root=fromstring(page)
    return root.xpath(xpath_to_use)[0]

def download_and_unpack_subtitles_file(url, dest_name):
    for zipped_file in all_zipped_file_in(readurl(url)):
        with zipped_file, file(dest_name,'w') as dest:
            shutil.copyfileobj(zipped_file, dest)

def readurl(url):
    with closing(urlopen(url)) as f:
        return f.read()

def all_zipped_file_in(zipfile_contents):
    zipstream = zipfile.ZipFile(StringIO(zipfile_contents))
    for name in zipstream.namelist():
        yield zipstream.open(name)

