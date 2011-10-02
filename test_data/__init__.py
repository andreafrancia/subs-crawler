def load(path):
    contents = file(resolve(path)).read()
    return contents

def resolve(path):
    return 'test_data/' + path
