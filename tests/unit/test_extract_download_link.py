from nose.tools import assert_equals
from crawler import extract_zip_link

def test_should_extract_the_zip_link():
    page=file('test-data/drive-2011-subtitrari.html').read()
    assert_equals('/en/ppodnapisi/download/i/1315272/k/'
                  '92ed8a52c45ac0eb804a1e56954aaac178e660fd', 
                  extract_zip_link(page))

def test_howto_extract_link_to_zip_file():
    page = make_details_page('/link')
    zip_link = extract_zip_link(page) 

    assert_equals('/link', zip_link)

def make_details_page(ziplink):
    return (
    """
    <html>
       <a href="{0}">
          <h1>Download</h1>
       </a> 
    </html>
    """.format(ziplink))
