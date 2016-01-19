#!/usr/bin/env python

from __future__ import print_function

import sys, os, cgi

print ("Blah!", file=sys.stderr)

#print("HTTP/1.1 302 Found")
#print("Location: http://www.google.com/")

#print("Content-type: text/plain")
#print("")
#print("Hello, this is the CGI script!")
#print("I am process %i" % os.getpid())

print("Content-type: text/html")
print("")
print("<html><body><form method='POST'><input name='x'></form></body></html>")

#print(os.environ)
print("")

form = cgi.FieldStorage()
print(form.getvalue("x"))
