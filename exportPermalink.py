#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os

def make_perfect_path(path):
	if type(path) != str:
		print('"%s" is not valid path!' % path)
		return
	if path[-1] == '/':
		return path[:-1]
	return path

def getContainedFiles(folder, type="NotRecursive"):
	file_names = []
	ret_cnt = 0

	for root, dirs, filenames in os.walk(folder):
		if type == "Recursive":
			for filename in filenames:
				if not filename.startswith('.'): # not hiden file
					file_names.append(os.path.join(root, filename))
					ret_cnt += 1
		else:
			for item in filenames:
				if not item.startswith('.'): # not hiden file
					file_names.append(os.path.join(root, item))
			ret_cnt = len(file_names)
			break
	return file_names, ret_cnt

import datetime
import yaml




filename = "test2.yaml"
f = open(filename, "w+")

yfile = {'last modified': datetime.date(1976, 7, 31),
		'Permalink': ["Permalink"]}










def exportPermalink(path_arg):
	path = os.path.join(make_perfect_path(path_arg), "_posts")
	file_paths, ret_cnt = getContainedFiles(path, type="Recursive")
	file_names = []
	for item in file_paths:
		file_names.append(os.path.basename(item))

	for item in file_names:
		print(item)

# /2016/03/02/Git.html
print(name[:10])
print(name[11:])

	yaml.dump(yfile, f)
	f.close()
# {{site.zhehua.home}}


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("path_arg", help="blog folder[Must be jekyll+Github Page!]", type=str)
	args = parser.parse_args()
	exportPermalink(args.path_arg)

