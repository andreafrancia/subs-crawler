from lxml import etree
from urllib2 import urlopen
from urllib import quote_plus
from nose.tools import assert_equals

def url(showname):
    return ("http://www.sub-titles.net/en/ppodnapisi/search?"
            "tbsl=1&"
            "asdp=1&"
            "sK=%(showname)s&" # showname
            "sM=0&"
            "sJ=9&" # language
            "submit=Search&"
            "sAKA=1&"
            "sY=&"
            "sR=" # Release
        % {'showname':quote_plus(showname)})

def read_page(url):
    try:
        f=urlopen(url)
        return f.read()
    finally:
        f.close()

from lxml import html
def _test_should_extract_the_address():
    dom=html.parse(url("Family Guy"))
    for i in dom.xpath("//table[@class='list']//tr/td[1]/a[2]/@href"):
        print i

from urlparse import urljoin
def _test_how_to_extract_zip_location():
    href="/en/ppodnapisi/podnapis/i/629411/family-guy-1999-sottotitoli"
    url=urljoin('http://www.sub-titles.net/', href)
    dom=html.parse(url)
    for i in dom.xpath("//a[img/@title='Download']/@href"):
        print urljoin(url, i) 
    
    assert False

    pass


