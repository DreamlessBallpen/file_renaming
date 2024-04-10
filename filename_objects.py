# Apparently, I should have added the .py when creating the filename at the top

class FileNameObj:
    def __init__(self, fname_str, type='', delim='-'):
        self.fname = fname_str
        self.type = type
        self.delim = delim

        # We parse the contents into a list
        self.namelist = fname_str.split(delim)
