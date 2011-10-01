from nose.tools import assert_equals
import unittest
from StringIO import StringIO

@unittest.skip("WIP")
def test_should_extract_the_zip_link():
    page=file('test-data/drive-2011-subtitrari').read()
    assert_equals('http://www.sub-titles.net/en/ppodnapisi/download/i/1315272/k/92ed8a52c45ac0eb804a1e56954aaac178e660fd', 
                  extract_zip_link(page))

xpath_to_use='//a[h1/text()="Download"]/@href'

def extract_zip_link(page):
    from lxml.html.soupparser import fromstring
    root=fromstring(page)
    assert_equals('', root.find(xpath_to_use))

def test_how_xpath_works():
    page = make_details_page('/link')
    zip_link = extract_zip_link(page) 

    assert_equals('/link', zip_link)

def extract_zip_link(page):
    from lxml import etree
    root=etree.parse(StringIO(page))
    return root.xpath(xpath_to_use)[0]

def make_details_page(ziplink):
    return (
    """
    <html>
       <a href="{0}">
          <h1>Download</h1>
       </a> 
    </html>
    """.format(ziplink) )
