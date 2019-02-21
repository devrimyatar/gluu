import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context

import mechanize
import cookielib
op_host = 'https://c3.gluu.org'




def login(mail):

    user, domain = mail.split('@')
    

    first_name, last_name = user.split('.')

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
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


    r = br.open(op_host)

    br.select_form(nr=0)



    # Let's Login
    br.form['loginForm:username'] = mail
    br.form['loginForm:password'] = last_name
    br.submit()

    # Get code from url
    cur_url = br.geturl()
    n = cur_url.find('#code')
    url = br.geturl()[n+1:]

    # Final brwosing
    br.open(op_host+'/identity/authentication/getauthcode?'+ url)

    html = br.response().read()
    name = mail.split('.')
    nn = html.find(first_name)
    print "Logged in as:", html[nn:nn+len(user)]

    del br
    
m = open('gluu_people.txt')

for l in m:
    print
    print "Trying to login with", l.strip()
    t1=time.time()
    try:
       login(l.strip())
       print "Login time: {:02f}".format(time.time()-t1)
    except:
       print "---->Failed to login"


