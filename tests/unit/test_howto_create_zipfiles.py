from nose.tools import assert_equals
import zipfile
from StringIO import StringIO
from ..pages import a_zip_containing

def test_howto_create_zipfile():
    zipdata = a_zip_containing('foo.txt', 'foo\n')
    
    reading = zipfile.ZipFile(StringIO(zipdata))

    assert_equals(['foo.txt'], reading.namelist())
    assert_equals('foo\n', reading.open('foo.txt').read())

