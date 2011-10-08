from nose.tools import assert_equals
from crawler import place_file

def test_place_file():
    with Sandbox('sandbox'):
        place_file('sandbox/filename', 'file contents')
        assert_equals('file contents', file('sandbox/filename').read())
    
import os
import shutil
class Sandbox:
    def __init__(self, path):
        self.path = path
    
    def __enter__(self):
        self.ensure_is_an_empty_dir()

    def __exit__(self, exc_type, exc_value, traceback):
        self.ensure_does_not_exists()

    def ensure_is_an_empty_dir(self):
        self.ensure_does_not_exists()
        os.mkdir(self.path)
        assert os.path.isdir(self.path)
        
    def ensure_does_not_exists(self):
        shutil.rmtree(self.path, ignore_errors = True)
        assert not os.path.exists(self.path)


     
