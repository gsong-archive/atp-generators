#!/usr/bin/env python

import argparse
import glob
import os
import shutil

def copy_files(outdir):
    if os.path.exists(outdir) and not os.path.isdir(outdir):
        raise os.error('%s exists but is not a directory!' % outdir)
    try:
        os.makedirs(outdir)
    except os.error:
        pass
    mypath = os.path.realpath(os.path.dirname(__file__))
    for app in glob.glob(os.path.join(mypath, 'applications/*.app')):
        dst = os.path.join(outdir, os.path.basename(app))
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(app, dst)
    for f in glob.glob(os.path.join(mypath, 'ms-word-template/*.dot')):
        shutil.copy2(f, outdir)


def setup_parser():
    """
    Setup the command line utility.
    """
    desc = "Copies the MS Word template and Applications to designated \
            directory."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        'outdir', metavar='OUTPUT_DIRECTORY',
        help='the directory to copy the files to')
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    copy_files(args.outdir)


if __name__ == '__main__':
    main()
