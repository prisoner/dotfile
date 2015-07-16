#!/usr/bin/python
#-*- utf-8 -*-

import os
import glob
import shutil
import subprocess

home = os.path.expandvars("${HOME}")

def links():
    fs = glob.glob(os.path.join(home, ".dotfile", "link", "*"))
    for f in fs:
        bn = os.path.basename(f)
        dot = os.path.join(home, "." + bn)
        if os.path.exists(dot):
            if not os.path.samefile(dot, f):
                if os.path.isdir(dot):
                    shutil.rmtree(dot)
                else:
                    os.remove(dot)
                os.symlink(f, dot)
                print "link %s to %s" % (f, dot)
        else:
            os.symlink(f, dot)
            print "link %s to %s" % (f, dot)

def links2():
    links = os.path.join(home, ".dotfile", "conf", "links")
    with open(links) as f:
        lks = [line.split('\t') for line in f.read().splitlines()]
        for item in lks:
            src = os.path.join(home, ".dotfile", item[0])
            dest = os.path.join(home, item[1])
            up = os.path.abspath(os.path.join(dest, os.pardir))
            if not os.path.isdir(up):
                os.makedirs(up)
            try:
                os.remove(dest)
                os.symlink(src, dest)
            except OSError, e:
                print "link %s to %s err, %s" % (src, dest, e)
            else:
                print "link %s to %s" % (src, dest)

def pkgs():
    fs = os.path.join(home, ".dotfile", "conf", "pkgs.lst")
    print fs
    with open(fs) as f:
        for line in f:
            pkg = line.strip()
            subprocess.check_call(["sudo", "apt-get", "install", "-y", pkg])

if __name__ == "__main__":
    # pkgs()
    links2()
    links()