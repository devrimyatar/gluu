import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import mechanize
import cookielib
op_host = 'https://c1.gluu.org'




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

    print mail, last_name

    html = br.response().read()
    #print html
    name = mail.split('.')
    nn = html.find(first_name)
    print "Logged in as:", html[nn-5:nn+len(user)+5]

    del br
    
m = open('gluu_people.txt')
i=1
for l in m:
    print
    print i, "Trying to login with", l.strip()
    login(l.strip())
    i += 1
