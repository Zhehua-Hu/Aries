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
home_url = config_yaml["GithubDefine"]["home_url"]
paper_list = config_yaml["GithubDefine"]["project_list"]
blog_foldername = config_yaml["GithubDefine"]["github_workbench"]

output_yaml = {"last modified": datetime.date.today(), "GithubProject": [
                {"Project": "Permalink"}]}


def make_perfect_path(path):
    if type(path) != str:
        print(r"<%s> is not valid path!" % path)
        return
    if path[-1] == "/":
        return path[:-1]
    return path

def export_git_project_and_permalink(path_arg, output_name="project_list.yaml"):
    path = make_perfect_path(path_arg)

    file_names = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isdir(file_path):
            if not os.path.basename(file_path).startswith('.'):
                file_names.append(file_path)

    yaml_path = os.path.join(project_folder,
                             os.path.join(blog_foldername, output_name))

    with open(yaml_path, "w+") as wf:
        for item in file_names:
            title_name = os.path.basename(item)
            output_yaml["GithubProject"].append({item: os.path.join(home_url, title_name)})

        yaml.dump(output_yaml, wf)
    print("GithubProject of \"%s\" have been exported!" % path_arg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_arg", help="blog folder[Must be jekyll+Github Page!]", type=str)
    parser.add_argument("--output", "-o", help="output filename", type=str)
    args = parser.parse_args()

    if args.output:
        paper_list = args.output
    export_git_project_and_permalink(args.path_arg, paper_list)

    # export_git_project_and_permalink(r"/home/zhehua/Github")