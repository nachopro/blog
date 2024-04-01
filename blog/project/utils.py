from os.path import abspath, dirname, join


PROJECT_ROOT = join(abspath(dirname(__file__)), '..')


def root_join(*path):
    return join(abspath(PROJECT_ROOT), *path)
