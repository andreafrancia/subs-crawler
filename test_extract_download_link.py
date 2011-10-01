from nose.tools import assert_equals

def test():
    assert_equals(1,1)

def test_should_extract_the_zip_link():
    page=file('test-data/drive-2011-subtitrari').read()
    assert_equals('http://www.sub-titles.net/en/ppodnapisi/download/i/1315272/k/92ed8a52c45ac0eb804a1e56954aaac178e660fd', 
                  extract_zip_link(page))

xpath_to_use='//a[h1/text()="Download"]/@href'

def extract_zip_link(page):
    from lxml.html.soupparser import fromstring
    root=fromstring(page)
    assert_equals('', root.find(xpath_to_use))

