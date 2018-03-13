import requests
import re
import bn_utils as bn
import sys
### UNFINISHED

# Uploads the file at the given filepath to the given url
def upload_file(url, filepath):
    c = bn.log_in()
    info_for_post = {}
    info_for_post["submission[type]"] = 'FilesSub'
    info_for_post["submission[assignment_id]"] = '514'
    info_for_post["submission[user_id]"] = '1917'
    info_for_post["submission[time_taken]"] = '1.0'
    info_for_post["submission[student_notes]"] = ''
    nurl = "https://handins.ccs.neu.edu/courses/25/assignments/514/submissions/new"

    to_upload = {}
    to_upload["submission[upload_file]"] = open('bn_utils.py', 'rb')

    hs = {"Referer": nurl,
                "Cookie": "_bn_session=" + c.cookies['_bn_session'] + "; " +
                    "_passenger_route=" + c.cookies['_passenger_route']}

    print c.post(nurl, files=to_upload, data=info_for_post).content

upload_file('', '')
