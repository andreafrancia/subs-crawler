from mockito import mock, when, verify, mock as stub, verifyNoMoreInteractions
from .. import pages
from crawler import GetSubs, search_url_for
from nose import SkipTest

def test_whole_interaction():
    http = stub()
    destination = mock()
    
    search_url  = search_url_for('Family Guy', '10', '1')
    details_url = '/en/ppodnapisi/podnapis/details'

    when(http).get(search_url     ).thenReturn(pages.search_result_list(details_url))
    when(http).get(details_url    ).thenReturn(pages.details_page('/zip-file-url'))
    when(http).get('/zip-file-url').thenReturn(
            pages.a_zip_containing('subtitles.srt', 'contents of .srt file'))

    getsubs = GetSubs(http, destination)
    getsubs.run('Family Guy', '10', '1')

    verify(destination).place_file(
            named='subtitles.srt', 
            contents='contents of .srt file')
    verifyNoMoreInteractions(destination)

def test_whole_interaction2():
    http = stub()
    destination = mock()
    
    search_url  = search_url_for('Family Guy', '10', '1')
    details_url = '/en/ppodnapisi/podnapis/details'

    when(http).get(search_url     ).thenReturn(pages.search_result_list(details_url))
    when(http).get(details_url    ).thenReturn(pages.details_page('/zip-file-url'))
    when(http).get('/zip-file-url').thenReturn(
            pages.a_zip_containing('subtitles.srt', 'contents of .srt file'))

    getsubs = GetSubs(http, destination)
    getsubs.run('Family.GuyS10E01.rest.avi')

    verify(destination).place_file(
            named='Family.GuyS10E01.rest.srt', 
            contents='contents of .srt file')
    verifyNoMoreInteractions(destination)

