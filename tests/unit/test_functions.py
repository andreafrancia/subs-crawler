from nose.tools import assert_equals
from .. import pages

from crawler import pick_first_details_link
def test_howto_pick_link_of_details_page():
    page=pages.search_result_list('/en/ppodnapisi/podnapis/details')
    assert_equals('/en/ppodnapisi/podnapis/details', 
                  pick_first_details_link(page))

from crawler import extract_zip_link
def test_howto_extract_the_zip_link():
    page = pages.details_page('/link')
    zip_link = extract_zip_link(page) 

    assert_equals('/link', zip_link)

from crawler import search_url_for
def test_search_url():
    assert_equals('http://www.sub-titles.net/'
                  'en/ppodnapisi/search?'
                  'tbsl=3&'
                  'asdp=1&'
                  'sK=Family+Guy&'
                  'sM=0&'
                  'sJ=9&'
                  'sO=desc&'
                  'sS=time&'
                  'submit=Search&'
                  'sAKA=1&'
                  'sTS=SS&'
                  'sTE=EE&'
                  'sY=&'
                  'sR=&'
                  'sT=1', search_url_for('Family Guy', 'SS', 'EE'))

