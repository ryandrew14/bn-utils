#!/usr/bin/local/python
import json
import os
import commands
import sys

# EFFECT: Removes the given user from users.json
def remove_user(name):
    if os.path.exists('users.json') and not open('users.json', 'r').read() == '':
        prev_json_file = open('users.json', 'r')
        current_json = prev_json_file.read()
        cur_json_dict = json.loads(current_json)
    else:
        cur_json_dict = {}

    if not name in cur_json_dict.keys():
        print "Could not delete - name not registered"
    else:
        del cur_json_dict[name]
        open('users.json', 'w').write(json.dumps(cur_json_dict))

# Standard main function/boilerplate
def main():

    args = sys.argv[1:]

    if not len(args) == 1:
        print "usage: python remove_user.py ref-name"
        sys.exit(1)
        return

    remove_user(str(args[0]))
    print "User %s removed from registry" % args[0]

if __name__ == "__main__":
    main()
