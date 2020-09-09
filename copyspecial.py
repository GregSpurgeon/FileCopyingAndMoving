# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = """Greg Spurgeon with help from, JT,
pythonforbeginners.com
docs.pythong.org"""

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    dir_list = []
    all_files = os.listdir(dirname)
    for filename in all_files:
        if re.search(r'__\w+__', filename):  # use re to match pattern in file
            dir_list.append(os.path.abspath(os.path.join(dirname, filename)))
    return dir_list


def copy_to(path_list, dest_dir):
    """Copy all the given files to the given directory"""
    if not os.path.exists(dest_dir):    # create dir if doesnt exist
        os.makedirs(dest_dir)
    for path in path_list:
        filename = os.path.basename(path)
        shutil.copy(path, os.path.join(dest_dir, filename))


def zip_to(path_list, dest_zip):
    """Zip all given files to a new zip file with the provided dir name"""
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)   # adds cmd to path_list list
    print(" ".join(cmd))
    subprocess.run(cmd)     # runs the zip command from line 43


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to grab special files')
    ns = parser.parse_args(args)

    path_list = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(path_list, ns.todir)

    if ns.tozip:
        zip_to(path_list, ns.tozip)

    # prints all special files
    for path in path_list:
        print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
