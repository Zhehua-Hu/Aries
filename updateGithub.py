#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
import yaml
import pprint
import platform

from github_tools.export_git_project_and_permalink import *


config_file = "config.yaml"
with open(config_file, "r+") as rf:
    config_yaml = yaml.load(rf)

    if "Windows" in platform.system():
        github_path = config_yaml['GithubPath']['win']
    else:
        github_path = config_yaml['GithubPath']['linux']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    export_git_project_and_permalink(github_path)








