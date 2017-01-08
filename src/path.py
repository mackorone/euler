from os import path


def dirpath():
    """ Returns the relative path of containing directory
    """
    return path.join(path.dirname(path.relpath(__file__)), '')


def filename(filepath):
    """ Returns the name of file given by filepath
    """
    return path.basename(filepath)
