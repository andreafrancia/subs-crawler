def search_result_list(first_link):
    return """
    <html>
      ...
      <a href='%(first_link)s' /> 
      ...
      <a href='other-links 1' /> 
      <a href='other-links 2' /> 
      ...
    </html>
    """ % locals()

def details_page(ziplink):
    return (
    """
    <html>
      ...
      <a href="{0}">
         <h1>Download</h1>
      </a> 
      ...
    </html>
    """.format(ziplink))

def a_zip_containing(filename, contents):
    from StringIO import StringIO
    import zipfile
    zip_file_contents=StringIO()
    
    zip_file = zipfile.ZipFile(zip_file_contents, 'w')
    zip_file.writestr(filename, contents)
    zip_file.close()

    return zip_file_contents.getvalue()
