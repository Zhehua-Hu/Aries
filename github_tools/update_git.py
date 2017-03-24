#!/usr/bin/env python
# coding=utf-8
""" """

import argparse
import os
import datetime


def quick_push_git(comment=(datetime.datetime.now().__str__())):
    command = "git add *"
    os.system(command)
    print("------> %s" % command)

    command = "git commit -m \"" + comment + u"\""
    os.system(command)
    print("------> %s" % command)

    command = "git push origin master"
    os.system(command)
    print("------> %s" % command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", "-m", help="git commit", type=str)
    args = parser.parse_args()

    if args.m:
        quick_push_git(args.m)
    else:
        quick_push_git(datetime.datetime.now().__str__())

