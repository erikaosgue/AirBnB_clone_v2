#!/usr/bin/python3
""" A Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:"""


import os.path
from os import path
from fabric.api import env, put, run

evn.host = ['35.237.57.250', '34.75.204.221']


def do_deploy(archive_path):
    """ Deploy archive!"""

    # archive_path is the hole path
    # ej --> versions/web_static_20170315003959.tgz -i
    # my_ssh_private_key -u ubuntu

    # archive_name is the name of the archive file with extension.tgz
    # ej --> web_static_20170315003959.tgz
    archive_name = archive_path.split("/")[1]

    # name archive file without the extension .tgz
    # ej --> web_static_20170315003959
    name = archive_name.split(".")[0]

    if path.isfile(archive_path) is False:
        return False
    if put(archive_path, "/tmp/{}".format(archive_name)).failed is True:
        return False
    if put("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(archive_name, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(archive_name)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
