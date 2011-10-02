from nose.tools import assert_equals
from crawler import pick_first_details_link

def test_howto_pick_link_of_details_page():
    page="""
    <html>
      ...
      <a href='/en/ppodnapisi/podnapis/details' /> 
      ...
    </html>
    """
    assert_equals('/en/ppodnapisi/podnapis/details', 
                  pick_first_details_link(page))

def test_integration_howto_pick_link_of_details_page():
    page=file('test_data/home-page.html').read()

    assert_equals('/en/ppodnapisi/podnapis/i/1316202/psych-2006-podnapisi',
                  pick_first_details_link(page))
