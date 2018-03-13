#!/usr/bin/local/python
import json
import os
import commands
import sys

# EFFECT: Prints the users that are registered locally
def list_users():
    if os.path.exists('users.json') and not open('users.json', 'r').read() == '':
        prev_json_file = open('users.json', 'r')
        current_json = prev_json_file.read()
        cur_json_dict = json.loads(current_json)
    else:
        cur_json_dict = {}

    if len(cur_json_dict) == 0:
        print "No users registered"
    else:
        for name in cur_json_dict.keys():
            print name

# Standard main function/boilerplate
def main():
    list_users()

if __name__ == "__main__":
    main()
