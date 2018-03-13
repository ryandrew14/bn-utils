#!/usr/bin/local/python
import json
import os
import commands
import sys

# EFFECT: Adds the given user to users.json
def add_user(name, username, password):
    if os.path.exists('users.json') and not open('users.json', 'r').read() == '':
        prev_json_file = open('users.json', 'r')
        current_json = prev_json_file.read()
        cur_json_dict = json.loads(current_json)
    else:
        cur_json_dict = {}
    if name in cur_json_dict.keys():
        raise Exception(name, "This name has already been used!")
    cur_json_dict[name] = {"username":"%s" % username,
                            "password":"%s" % password}
    open('users.json', 'w').write(json.dumps(cur_json_dict))

# Standard main function/boilerplate
def main():

    args = sys.argv[1:]

    if not len(args) == 3:
        print "usage: python add_user.py ref-name username password"
        sys.exit(1)
        return

    add_user(str(args[0]), str(args[1]), str(args[2]))
    print "User added with ref-name %s" % args[0]

if __name__ == "__main__":
    main()
