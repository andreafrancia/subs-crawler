from nose.tools import assert_equals

import re
def test():
    def parse(filename):

        match=re.finditer("(.*)S(..)E(..)", filename).next()

        showname = match.group(1).replace('.',' ').strip()
        season   = match.group(2).lstrip('0')
        episode  = match.group(3).lstrip('0')

        return (showname, season, episode)

    assert_equals(('Family Guy', '11',  '6'), parse('Family.Guy.S11E06.rest.avi'))
    assert_equals(('Family Guy', '11', '60'), parse('Family.Guy.S11E60.rest.avi'))
    assert_equals(('Family Guy',  '1', '60'), parse('Family.Guy.S01E60.rest.avi'))
    assert_equals(('TheSeaEar',  '1', '60'), parse('TheSeaEar.S01E60.rest.avi'))


    
