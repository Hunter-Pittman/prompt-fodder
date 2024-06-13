from os.path import dirname, join as joinpath
from os.path import exists


DATADIR = joinpath(dirname(__file__), 'config.toml')

if not exists(DATADIR):
    raise IOError("config.toml does not exists in the package directory!")