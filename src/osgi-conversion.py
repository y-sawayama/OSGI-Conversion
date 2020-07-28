#!/usr/bin/env python3

import shutil
from argparse import ArgumentParser

# ex) -p ui.apps/src/main/content/jcr_root/apps/system/config/xxxxx.config
def option():
    argparse = ArgumentParser()
    argparse.add_argument("-p", "--src", default="", help="変換対象ファイル")
    return argparse.parse_args()


def convertionToOSGInode(): 
    rename_file = option().src.replace(".config", ".xml")

    with open(option().src) as before_file, open(shutil.copy(option().src, rename_file), "w", newline="\n") as new_file:

        #read = before_file.read()
        #before_convertion = read.rstrip()

        new_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        new_file.write("<jcr:root xmlns:sling=\"http://sling.apache.org/jcr/sling/1.0\" xmlns: jcr=\"http://www.jcp.org/jcr/1.0\"\n")
        new_file.write("\t" + "jcr:primaryType=\"sling: OsgiConfig\"\n")

        for line in before_file:
            if not "# Configuration created by Apache Sling JCR Installer" in line:
                new_file.write("\t" + line)

        new_file.write("/>")

def main():
    convertionToOSGInode()

if __name__ == "__main__":
    main()
