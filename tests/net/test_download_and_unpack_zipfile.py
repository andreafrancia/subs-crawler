from crawler import download_and_unpack_subtitles_file

def test_howto_download_and_unpack_a_subttiles_files():
    ensure_empty_dir('sandbox')

    url='http://www.sub-titles.net/en/ppodnapisi/download/i/146050/k/6dd75fd863296d91c6936e6a01eddedf1f8021d0'
    dest_name='sandbox/output.srt'

    download_and_unpack_subtitles_file(url, dest_name)
   
    assert_file_equals('sandbox/output.srt', 'test-data/expected.srt')

def ensure_empty_dir(path):
    import os
    import shutil
    shutil.rmtree(path, ignore_errors=True)
    assert not os.path.exists(path)
    os.makedirs(path)
    assert os.path.isdir(path)

def assert_file_equals(expected, actual):
    import filecmp
    assert filecmp.cmp(expected, actual, False)

