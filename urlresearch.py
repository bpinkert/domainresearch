#!/usr/bin/env python
import whois

def registrar(dom):
	d = whois.whois(str(dom))
	domain = str(d.domain_name)
	transferstat = str(d.status)
	creation = str(d.creation_date)
	cd = str(creation)
	cdd = cd.split('u')
	cdate = cdd[1]
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
	org = str(d.org)
	emails = str(d.emails)
	elist = emails.split(',')
	return domain, transferstat, cdate, update, registrar, refurl, whoserver, dnssec, address, regcity, regstate, regzip, expdate, ns1, ns2, ns3, org, elist

def cleanreg(r):
	print "Domain Name: %s\n" % r[0]
	print "Transfer Status: %s\n" % r[1].split(',')[0][3:-1]
	print "Creation Date: %s\n" % r[2][1:-2]
	print "Date Updated: %s\n" % r[3]
	print "Registrar Name: %s\n" % r[4]
	print "Referral URL: %s\n" % r[5]
	print "Whois Server: %s\n" % r[6]
	print "DNSSEC: %s\n" % r[7]
	print "Registered Organization: %s\n" % r[8].split(',')[1][3:-2] 
	print "Registered Address: %s\n" % r[8].split(',')[0][3:-1]
	print "Registered City: %s\n" % r[9]
	print "Registered State: %s\n" % r[10]
	print "Registered Zip: %s\n" % r[11]
	print "Expiration Date: %s\n" % r[12].split('u')[1][1:-3]
	print "Nameserver 1: %s\n" % r[13]
	print "Nameserver 2: %s\n" % r[14]
	print "Nameserver 3: %s\n" % r[15][0:-1]
	print "Whois Organization: %s\n" % r[16]
	print "Email 1: %s\n" % r[17][0][3:-1]
	print "Email 2: %s\n" % r[17][1][3:-2]

registrar('savantdigital.net')
