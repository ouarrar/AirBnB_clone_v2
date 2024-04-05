#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from my_functions import do_pack
from my_functions import do_deploy

def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
