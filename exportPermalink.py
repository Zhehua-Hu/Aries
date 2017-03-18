#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
import datetime
import yaml
import sys


blog_foldername = "blog_workbench"
home_url_var = "{{site.zhehua.home}}/"
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

	current_folder = os.path.dirname(os.path.abspath(sys.argv[0]))
	filename = os.path.join(current_folder, os.path.join(blog_foldername, output_name))
	with open(filename, "w+") as f:
		for item in file_names:
			title_whole = os.path.basename(item)
			folder = os.path.basename(os.path.dirname(item))

			date_str = title_whole[:10].replace("-","/")
			title_str = title_whole[11:][:-3] + ".html"
			integrated_str = home_url_var + date_str + "/" + title_str

			yfile["Permalink"].append({folder:integrated_str})
		yaml.dump(yfile, f)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("path_arg", help="blog folder[Must be jekyll+Github Page!]", type=str)
	parser.add_argument("--output", "-o", help="output filename", type=str)
	args = parser.parse_args()

	output_name = "paper_list.yaml"
	if args.output:
		output_name = args.output
	exportPermalink(args.path_arg, output_name)

