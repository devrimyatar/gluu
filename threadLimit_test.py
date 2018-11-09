#!/usr/bin/python

import thread
import time
import requests

requests.packages.urllib3.disable_warnings()

my_url = 'https://c2.gluu.org/oxauth/restv1/authorize?response_type=code&client_id=@!F7CB.929B.4A73.EA6E!0001!EA93.FCCF!0008!CCA5.4735.7AFF.7646&redirect_uri=https://c3.gluu.org:8080/login_callback/'

def get_login_page():
    for i in range(10000):
        result = requests.get(my_url, verify=False)
        html = result.text
        if result.status_code == 403:
            print html


thread.start_new_thread(get_login_page, ())
thread.start_new_thread(get_login_page, ())
thread.start_new_thread(get_login_page, ())
thread.start_new_thread(get_login_page, ())

while 1:
   pass
