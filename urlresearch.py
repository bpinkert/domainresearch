#!/usr/bin/env python
import whois

def lookup(domain):
	
	return d

def updated(d):
	return update

def status(d):

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
	nameservers = str(d.name_servers)
	org = str(d.org)
	emails = str(d.emails)
	return domain, transferstat, cdate, update, registrar, refurl, whoserver, dnssec, address, regcity, regstate, regzip, expdate, nameservers, org, emails

def cleanreg(domain, transferstat, cdate, update, registrar, refurl, whoserver, dnssec, address, regcity, regstate, regzip, expdate, nameservers, org, emails)

