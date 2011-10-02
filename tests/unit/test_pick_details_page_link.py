from nose.tools import assert_equals

def test_something():
    assert_equals(1,1)

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

def pick_first_details_link(page):
    expression="//x:a[starts-with(@href,'/en/ppodnapisi/podnapis')]"
    pass

