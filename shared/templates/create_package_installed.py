#!/usr/bin/python2

#
# create_package_installed.py
#   automatically generate checks for installed packages
#
# NOTE: The file 'template_package_installed' should be located in the same
# working directory as this script. The template contains the following tags
# that *must* be replaced successfully in order for the checks to work.
#
# PKGNAME - the name of the package that should be installed
#

import sys

from template_common import *

def output_checkfile(target, package_info):
    pkgname = package_info[0]
    if pkgname:
        if target == "oval":
            file_from_template(
                "./template_OVAL_package_installed",
                { "PKGNAME" : pkgname },
                "./oval/package_{0}_installed.xml", pkgname
            )

        elif target == "bash":
            file_from_template(
                "./template_BASH_package_installed",
                { "PKGNAME" : pkgname },
                "./bash/package_{0}_installed.sh", pkgname
            )

        elif target == "ansible":
            file_from_template(
                "./template_ANSIBLE_package_installed",
                { "PKGNAME" : pkgname },
                "./ansible/package_{0}_installed.yml", pkgname
            )

        elif target == "anaconda":
            file_from_template(
                "./template_ANACONDA_package_installed",
                { "PKGNAME" : pkgname },
                "./anaconda/package_{0}_installed.anaconda", pkgname
            )

        elif target == "puppet":
            file_from_template(
                "./template_PUPPET_package_installed",
                { "PKGNAME" : pkgname },
                "./puppet/package_{0}_installed.pp", pkgname
            )

        else:
            raise UnknownTargetError(target)

    else:
        print "ERROR: input violation: the package name must be defined"

def help():
    print("Usage:\n\t" + __file__ + " <bash/oval/ansible/anaconda/puppet> <csv file>")
    print("CSV should contains lines of the format: " +
               "PACKAGE_NAME")

if __name__ == "__main__":
    main(sys.argv, help, output_checkfile)
