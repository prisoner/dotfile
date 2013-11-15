#! /usr/bin/env python

from scriptine import run, path, log, shell
import os

os_name = os.uname()[0].lower()
# user_home = os.environ['HOME']
user_home = "/home/chenpeng/temp/home"

def _remove_osname(text):
	return text.replace("_linux", "").replace("_mac", "")

def _get_files_by_os(dir):
	files = set()
	for f in path(dir).listdir():
		abs_path = f.abspath()
		files.add(_remove_osname(abs_path))

	paths = set()
	for f in files:
		item = path(f + "_" + os_name)
		if not item.exists():
			item = path(f)
		paths.add(item)
	return paths

def link_command():
	paths = _get_files_by_os("link")
	for item in paths:
		link = path(user_home + "/." + _remove_osname(item.basename()))
		if link.exists():
			link.remove()
		item.symlink(link)
		log.mark("link %s to %s", item, link)

def copy_command():
	paths = _get_files_by_os("copy")
	for item in paths:
		link = path(user_home + "/." + _remove_osname(item.basename()))
		if item.isdir():
			if link.isdir():
				shell.call(["rm", "-rf", link])
			item.copytree(link)
		if item.isfile():
			if link.isfile():
				link.remove()
			item.copyfile(link)
		log.mark("copy %s to %s", item, link)

def install_ubuntu_pkg():
	lines = path("conf/ubuntu_packages.lst").lines()
	for item in lines:
		shell.call(["sudo", "apt-get", "install", item.replace("\n", "")])
	# pkgs = " ".join(lines).replace("\n", "")
	# cmd = "sudo apt-get install " + pkgs

def init_command():
	link_command()
	copy_command()
	install_ubuntu_pkg()

if __name__ == '__main__':
	run()