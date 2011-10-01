from nose.tools import assert_equals
from urllib import urlopen
import shutil
import unittest
from contextlib import closing
import hashlib
import zipfile
from StringIO import StringIO
import filecmp

def test_howto_download_a_file():
    ensure_empty_dir('sandbox')

    url='http://www.sub-titles.net/en/ppodnapisi/download/i/146050/k/6dd75fd863296d91c6936e6a01eddedf1f8021d0'
    dest_name='sandbox/output.srt'

    download_and_unpack(url, dest_name)
    
    assert filecmp.cmp('sandbox/output.srt', 'test-data/expected.srt', False)

def download_and_unpack(url, dest_name):
    for zipped_file in all_zipped_file_in(readurl(url)):
        with zipped_file, file(dest_name,'w') as dest:
            shutil.copyfileobj(zipped_file, dest)

def readurl(url):
    with closing(urlopen(url)) as f:
        return f.read()

def all_zipped_file_in(zipfile_contents):
    zipstream = zipfile.ZipFile(StringIO(zipfile_contents))
    for name in zipstream.namelist():
        yield zipstream.open(name)

def ensure_empty_dir(path):
    import os
    shutil.rmtree(path, ignore_errors=True)
    assert not os.path.exists(path)
    os.makedirs(path)
    assert os.path.isdir(path)
    

    
