#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
import yaml
import pprint
import platform

from github_tools.export_git_project_and_permalink import *
from github_tools.update_github_project import *

config_file = "config.yaml"

with open(config_file, "r+") as rf:
    config_yaml = yaml.load(rf)

    if "Windows" in platform.system():
        github_path = config_yaml['GithubPath']['win']
    else:
        github_path = config_yaml['GithubPath']['linux']

github_projects = []
project_list = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         config_yaml['GithubDefine']["github_workbench"]),
                            config_yaml['GithubDefine']["project_list"])
with open(project_list, "r+") as rf:
    project_yaml = yaml.load(rf)

    for item in project_yaml["GithubProject"]:
        for key, val in item.items():
            github_projects.append(val)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    export_git_project_and_permalink(github_path)

    for path in github_projects:
        update_github_project(path)







