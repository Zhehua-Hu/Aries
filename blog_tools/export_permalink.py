#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import datetime
import os
import yaml
import sys
import pprint

from mypy.file_tools.FileList import FileList

current_folder = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.dirname(current_folder)

config_file = os.path.join(project_folder, "config.yaml")
f = open(config_file, "r+")
config_yaml = yaml.load(f)

# Import Config
home_url = config_yaml["BlogDefine"]["home_url"]
paper_list = config_yaml["BlogDefine"]["paper_list"]
blog_foldername = config_yaml["BlogDefine"]["blog_workbench"]

output_yaml = {"last modified": datetime.date.today(), "Blog": [
    {"Category": "PaperPermalink"}]}


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
                if not filename.startswith("."):  # not hiden file
                    file_names.append(os.path.join(root, filename))
                    ret_cnt += 1
        else:
            for item in filenames:
                if not item.startswith("."):  # not hiden file
                    file_names.append(os.path.join(root, item))
            ret_cnt = len(file_names)
            break
    return file_names, ret_cnt


def exportPermalink(path_arg, output_name="paper_list.yaml"):
    path = os.path.join(make_perfect_path(path_arg), "_posts")
    file_names = FileList(path, search_type="Recursive").get_files_path_list()
    _yaml_path = os.path.join(project_folder,
                              os.path.join(blog_foldername, output_name))

    with open(_yaml_path, "w+") as f:
        for item in file_names:
            title_name = os.path.basename(item)
            folder_name = os.path.basename(os.path.dirname(item))

            date_str = title_name[:10].replace("-", "/")
            title_str = title_name[11:][:-3] + ".html"
            integrated_str = home_url + "/" + date_str + "/" + title_str

            output_yaml["Blog"].append({folder_name: integrated_str})
        yaml.dump(output_yaml, f)
    print("Permalinks of \"%s\" have been exported!" % path_arg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_arg", help="blog folder[Must be jekyll+Github Page!]", type=str)
    parser.add_argument("--output", "-o", help="output filename", type=str)
    args = parser.parse_args()

    if args.output:
        paper_list = args.output
    exportPermalink(args.path_arg, paper_list)

    # exportPermalink(r"/home/zhehua/Zhehua-Hu.github.io")