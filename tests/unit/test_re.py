from nose.tools import assert_equals
from crawler import parse

def test():
    assert_equals(('Family Guy', '11',  '6'), parse('Family.Guy.S11E06.rest.avi'))
    assert_equals(('Family Guy', '11', '60'), parse('Family.Guy.S11E60.rest.avi'))
    assert_equals(('Family Guy',  '1', '60'), parse('Family.Guy.S01E60.rest.avi'))
    assert_equals(('TheSeaEar' ,  '1', '60'), parse('TheSeaEar.S01E60.rest.avi'))

