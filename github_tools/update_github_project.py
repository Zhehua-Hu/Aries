#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
from .update_git import *

def update_github_project(project_folder):
    save_pwd = os.getcwd()
    os.chdir(project_folder)
    print(os.getcwd())

    update_git()

    os.chdir(save_pwd)
    print(os.getcwd())


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("project_folder_arg", help="git commit", type=str)
    # args = parser.parse_args()
    #
    # update_github_project(args.project_folder_arg)
    update_github_project("/home/zhehua/Github/Enchain.wiki")

