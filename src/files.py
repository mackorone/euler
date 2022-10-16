from os import path


def filepath(filename):
    """ Returns a relative path to file given by filename
    """
    return path.join(path.dirname(path.relpath(__file__)), filename)


def filename(filepath):
    """ Returns the name of file given by filepath
    """
    return path.basename(filepath)
