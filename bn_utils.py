import requests
import re
import json

# This is a basic utilities modules, which should hold functions to be
# used in the other modules.

# EFFECT send a post request to the handins server with my creds
def log_in(user):
    with requests.Session() as c:
        to_read = open('users.json', 'r').read()
        parsed = json.loads(to_read)
        if user in parsed.keys():
            user_name = parsed[user]['username']
            user_pass = parsed[user]['password']
        else:
            raise Exception(user, "Given name not registered locally! Look into add_user.py")
        url = "https://handins.ccs.neu.edu/users/sign_in"
        got = c.get(url)
        a_t = get_authenticity_token(got.content)
        info = {'authenticity_token': a_t,
                'user[username]': user_name,
                'user[password]': user_pass,
                'commit': 'Log in'}
        hs = {"Referer": "https://handins.ccs.neu.edu/",
                "Cookie": "_bn_session=" + c.cookies['_bn_session'] + "; " +
                    "_passenger_route=" + c.cookies['_passenger_route']}
        r = c.post(url, data=info, headers=hs)
        return c

# Returns a string containing the authenticity_token from a given webpage
def get_authenticity_token(webpage):
    reg = r'name="csrf-token"\scontent="(.+)"\s/>'
    ret = re.search(reg, webpage).group(1)
    return ret
