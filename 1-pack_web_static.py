#!/usr/bin/env python3
# A Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local
from datetime import datetime
import os.path
from os import path


def do_pack():
    # create the folder versions if not exists
    if path.isdir("versions") is False:
        local("mkdir -p versions")
        if path.isdir("versions") is False:
            return None
    t = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        t.year, t.month, t.day, t.hour, t.minute, t.second)
    local("tar -czvf versions/{} web_static".format(archive_name))
    return "versions/" + archive_name
