# needs dns module/python installed - HT - http://www.dnspython.org/examples.html
import dns.resolver
import sys

if len (sys.argv) != 3 :
    print 'Usage: please specify <MX|NS> <mx domain name|nameserver>'
    sys.exit (1)

domain = sys.argv[2]
answers = dns.resolver.query(domain, sys.argv[1])
for server in answers:
    print server
