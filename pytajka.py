#! /usr/bin/python     
# -*- coding: utf-8 -*-
import sys
import dns
import dns.resolver
import re
nameservers = {
	"Google1": "8.8.8.8",
 	"Google2": "8.8.4.4",
	"Quad91": "9.9.9.9",
	"Quad92": "149.112.112.112",
	"OpenDNS Home1": "208.67.222.222",
	"OpenDNS Home2": "208.67.220.220",
	"Cloudflare1": 	"1.1.1.1",
	"Cloudflare2": 	"1.0.0.1",
	"CleanBrowsing1": "185.228.168.9",
	"CleanBrowsing2": "185.228.169.9",
	"Verisign1": "64.6.64.6",
	"Verisign2": "64.6.65.6",
	"Alternate DNS1": "198.101.242.72",
	"Alternate DNS2": "23.253.163.53",
	"AdGuard DNS": 	"94.140.14.14",
	"AdGuard DNS": 	"94.140.15.15"
}

for ns in nameservers:
	print(ns)
	r = dns.resolver.Resolver()
	r.nameservers = [nameservers[ns]]
	answer = r.query(sys.argv[1], 'A')
	if answer.rrset is not None:
		print(answer.rrset)
