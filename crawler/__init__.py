import zipfile
from StringIO import StringIO

class GetSubs:
    def __init__(self, http, destination):
        self.destination = destination
        self.http = http

    def run(self, *args):
        if len(args)==3:
            showname=args[0]
            season=args[1]
            episode=args[2]
            subs_filename='subtitles.srt'
        else:
            filename=args[0]
            showname, season, episode = parse(filename)
            subs_filename=filename.replace('.avi', '.srt') # TODO: not robust

        results_page = self.http.get(search_url_for(showname, season, episode))
        link_to_details_page = pick_first_details_link(results_page)
         
        details_page = self.http.get(link_to_details_page)
        link_to_zip_file = extract_zip_link(details_page)

        zip_file_contents=self.http.get(link_to_zip_file)
        subtitles_file=extract_first_zipped_file(zip_file_contents)

        self.destination.place_file(named=subs_filename,
                                    contents=subtitles_file)
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

