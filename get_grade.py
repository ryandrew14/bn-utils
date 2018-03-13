#!/usr/bin/local/python
import requests
import re
import bn_utils as bn
import sys

# Returns a string containing the current number grade for
# the course with the given url
def get_grade(url, which, user):
    session = bn.log_in(user)
    wanted = session.get(url).content
    if which == 'c':
        regexp = r'Grade\sso\sfar:.+?(\d\d\.\d\d)'
    elif which == 'h':
        regexp = r'Maximum\sgrade:.+?(\d\d\.\d\d)'
    else:
        raise InputError('c', 'must give get_grade either c or h as second arg')
    match = re.search(regexp, wanted, re.DOTALL).group(1)
    return match

# Abstraction to print usage in multiple "fail" cases
def print_usage():
    print "usage: python [-c] [-h] ref-name"
    print "  -c (or --current) for current grade"
    print "  -h (or --highest) for highest possible grade"

# Standard main function/boilerplate
def main():

    args = sys.argv[1:]

    if not args or not len(args) == 2:
        print_usage()
        sys.exit(1)

    if args[0] == '-c' or args[0] == '--current':
        del args[0]
        print get_grade("https://handins.ccs.neu.edu/courses/25/assignments", 'c', args[0])
    elif args[0] == '-h' or args[0] == '--highest':
        del args[0]
        print get_grade("https://handins.ccs.neu.edu/courses/25/assignments", 'h',  args[0])

if __name__ == "__main__":
  main()
