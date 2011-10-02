from nose.tools import assert_equals
import unittest
from mockito import mock, when, verify, mock as stub, verifyNoMoreInteractions
from .. import pages
from crawler import GetSubs

search_url='/search'

def test_whole_interaction():
    http = stub()
    destination = mock()
    when(http).get(search_url     ).thenReturn(pages.search_result_list('/details-page'))
    when(http).get('/details_page').thenReturn(pages.details_page('/link-to-zip-file'))
    when(http).get('/zip-file').thenReturn(
            pages.a_zip_containing('subtitles.srt', 'contents of .srt file'))

    getsubs = GetSubs(http, destination)
    getsubs.run('Family Guy', '10', '1')

    verify(destination).place_file(
            named='subtitles.srt', 
            contents='contents of .srt file')
    verifyNoMoreInteractions(destination)


