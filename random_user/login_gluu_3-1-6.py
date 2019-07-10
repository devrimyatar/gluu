import ssl
import sys
import re
import time
ssl._create_default_https_context = ssl._create_unverified_context

import mechanize
import cookielib
op_host = 'https://c3.gluu.org'

gt = 0
myn = 0
def login_gluu(username, password,c):
    global gt, myn
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=10)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    t1 = time.time()
    r = br.open(op_host)

    br.select_form(nr=0)

    # Let's Login
    br.form['loginForm:username'] = username
    br.form['loginForm:password'] = password
    try:
        br.submit()

    except:
        print br.response().read()
        sys.exit()

    html = br.response().read()
    t2 = time.time()
    tt = t2-t1
    gt += tt
    myn += 1
    nn = html.find('glyphicon-user')
    if nn > -1:
        print c,'\t', '{:0.3f}'.format(tt).rjust(8), '{:0.3f}'.format(gt/myn).rjust(8), "    Logged in as", re.findall('\<\p style="font-size: 14px;  color: whitesmoke;">(.*?)\<\/p>', html.replace('\n',''))[0].strip()
    else:
        print "NOT LOGGED IN"


pf = open('/root/gluu_people.txt')

c=0
for l in pf:
    try:
        username = l.strip().split()[1]
        pw = username.split('@')[0].split('.')[1]
        login_gluu(username, pw,c)
        c +=1
    except:
        print "ERROR", l.strip()