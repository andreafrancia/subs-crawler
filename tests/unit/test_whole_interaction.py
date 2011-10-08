from mockito import when, mock as stub
from .. import pages
from crawler import GetSubs, search_url_for
from mock import Mock

def test_whole_interaction():

    http = stub()
    place_file  = Mock()
    
    search_url   = search_url_for('Family Guy', '10', '1')
    details_url  = '/en/ppodnapisi/podnapis/details'
    details_url2 = "http://www.sub-titles.net" + details_url 

    when(http).get(search_url     ).thenReturn(pages.search_result_list(details_url))
    when(http).get(details_url2   ).thenReturn(pages.details_page('http://zip-file-url'))
    when(http).get('http://zip-file-url').thenReturn(
            pages.a_zip_containing('subtitles.srt', 'contents of .srt file'))

    getsubs = GetSubs(http, place_file)
    getsubs.run('Family.GuyS10E01.rest.avi')

    place_file.assert_called_with('Family.GuyS10E01.rest.srt', 
                                  'contents of .srt file')

