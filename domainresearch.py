#!/usr/bin/env python
import whois
import argparse

def registrar(dom):
	"""
	Function that takes in a domain name and returns information
	"""
	d = whois.whois(str(dom))
	domain = str(d.domain_name)
	transferstat = str(d.status)
	creation = str(d.creation_date)
	cd = str(creation)
	cdd = cd.split('u')
	if len(cdd) == 2:
		cdate = cdd[1]
	else:
	 	cdate = None
	update = str(d.update_date)
	registrar = str(d.registrar)
	refurl = str(d.referral_url)
	whoserver = str(d.whois_server)
	dnssec = str(d.dnssec)
	address = str(d.address)
	regcity = str(d.city)
	regstate = str(d.state)
	regzip = str(d.zipcode)
	expdate = str(d.expiration_date)
	nameservers = str(d.name_servers).split(',')
	ns1 = nameservers[0][3:-1]
	ns2 = nameservers[1][3:-1]
	if len(nameservers) > 2:
		ns3 = nameservers[2][3:-1]
	else:
		ns3 = None
	org = str(d.org)
	emails = str(d.emails)
	elist = emails.split(',')
	return domain, transferstat, cdate, update, registrar, refurl, whoserver, dnssec, address, regcity, regstate, regzip, expdate, ns1, ns2, ns3, org, elist

def cleanreg(r):
	"""
	Takes the output from the registrar function and cleans it, prints it
	"""
	print "Domain Name: %s\n" % r[0]
	print "Transfer Status: %s\n" % r[1].split(',')[0][3:-1]
	if r[2] != None:
		print "Creation Date: %s\n" % r[2][1:-2]
	else:
		pass
	print "Date Updated: %s\n" % r[3]
	print "Registrar Name: %s\n" % r[4]
	print "Referral URL: %s\n" % r[5]
	print "Whois Server: %s\n" % r[6]
	print "DNSSEC: %s\n" % r[7]
	# if r[8] != None:
	# 	print "Registered Organization: %s\n" % r[8].split(',')[1][3:-2]
	# else:
	# 	pass
	print "Registered Address: %s\n" % r[8]
	print "Registered City: %s\n" % r[9]
	print "Registered State: %s\n" % r[10]
	print "Registered Zip: %s\n" % r[11]
	# print "Expiration Date: %s\n" % r[12].split('u')[1][1:-3]
	print "Nameserver 1: %s\n" % r[13]
	print "Nameserver 2: %s\n" % r[14]
	if r[15] != None:
		print "Nameserver 3: %s\n" % r[15][0:-1]
	else: 
		pass
	print "Whois Organization: %s\n" % r[16]
	print "Email 1: %s\n" % r[17][0][3:-1]
	print "Email 2: %s\n" % r[17][1][3:-2]

def main():
    parser = argparse.ArgumentParser(add_help = True, prog='python script to fetch whois information for domain', description = "Python script to fetch whois information for domain.", usage='Use like so: python urlresearch.py --url example.com')
    parser.add_argument('--url', action='store', dest='url', help='example.com')
    parser.add_argument('--debug', action='store', dest='debug', help='Turn DEBUG output ON')
    options = parser.parse_args()
    # if len(options.url) != 1:
    #     parser.print_help()
    domname = options.url
    r = registrar(domname)
    cleaned = cleanreg(r)

if __name__ == '__main__':
    main()
    