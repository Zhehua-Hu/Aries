#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
import datetime
import yaml

yfile = {"last modified": datetime.date.today(),
		"Permalink": [{"Category":"Paper"}]}

def make_perfect_path(path):
	if type(path) != str:
		print(r"<%s> is not valid path!" % path)
		return
	if path[-1] == "/":
		return path[:-1]
	return path

def getContainedFiles(folder, type="NotRecursive"):
	file_names = []
	ret_cnt = 0

	for root, dirs, filenames in os.walk(folder):
		if type == "Recursive":
			for filename in filenames:
				if not filename.startswith("."): # not hiden file
					file_names.append(os.path.join(root, filename))
					ret_cnt += 1
		else:
			for item in filenames:
				if not item.startswith("."): # not hiden file
					file_names.append(os.path.join(root, item))
			ret_cnt = len(file_names)
			break
	return file_names, ret_cnt

def exportPermalink(path_arg, output_name="paper_list.yaml"):
	path = os.path.join(make_perfect_path(path_arg), "_posts")
	file_names, ret_cnt = getContainedFiles(path, type="Recursive")

	current_folder = os.path.dirname(__file__)
	filename = os.path.join(current_folder, "blog_workbench/" + output_name)
	with open(filename, "w+") as f:
		for item in file_names:
			title_whole = os.path.basename(item)
			folder = os.path.basename(os.path.dirname(item))

			date_str = title_whole[:10].replace("-","/")
			title_str = title_whole[11:][:-3] + ".html"
			integrated_str = "{{site.zhehua.home}}/" + date_str + "/" + title_str

			yfile["Permalink"].append({folder:integrated_str})
		yaml.dump(yfile, f)

if __name__ == "__main__":
	# parser = argparse.ArgumentParser()
	# parser.add_argument("path_arg", help="blog folder[Must be jekyll+Github Page!]", type=str)
	# args = parser.parse_args()
	# exportPermalink(args.path_arg)

	exportPermalink(r"C:\A_Blog\Zhehua-Hu.github.io")
