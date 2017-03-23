#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
import yaml
import pprint
import platform

from blog_tools.export_permalink import *
from blog_tools.name_check import *


config_file = "config.yaml"
with open(config_file, "r+") as rf:
    config_yaml = yaml.load(rf)

    if "Windows" in platform.system():
        folder_blog = config_yaml['BlogPath']['win']
    else:
        folder_blog = config_yaml['BlogPath']['linux']






if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--list", "-l", action='store_true', help="Show All Papers")
    args = parser.parse_args()

    exportPermalink(folder_blog)

    if args.list:
        nameCheck(folder_blog)





