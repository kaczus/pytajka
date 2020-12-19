#! /usr/bin/python	 
# -*- coding: utf-8 -*-
import sys
import dns
import dns.resolver
import re

site = sys.argv[1]
nameservers = {
	"dns5.home.pl": "62.129.252.215",
	"dns4.home.pl": "62.129.252.252",
	"Politechnika Bialostocka": "212.33.80.231",
	"Orange 1": "212.244.48.137",
	"Orange 2": "79.187.201.181",
	"Orange 3": "79.187.201.179",
	"Orange 4": "79.190.224.27",
	"Orange 5": "212.244.78.90",
	"Orange 6": "83.19.241.2",
	"Orange 7": "80.55.253.114",
	"Netia": "78.9.110.22",
	"INEA": "88.151.140.202",
	"Implix": "188.252.69.3",
	"MIT-GATEWAYS": "91.232.102.4",
	"Internetia": "5.57.148.177",
	"Polkomtel": "92.60.142.210",
	"Uniwersytet bydgoszcz": "89.191.129.104",
	"Netia": "213.241.88.98",
	"Polibuda GDA?": "153.19.105.120",
	"Uni biochem": "150.254.125.203",
	"SAT-MONT-SERVICE": "79.175.208.28",
	"Google 1": "8.8.8.8",
 	"Google 2": "8.8.4.4",
	"Quad9 1": "9.9.9.9",
	"Quad9 2": "149.112.112.112",
	"OpenDNS Home 1": "208.67.222.222",
	"OpenDNS Home 2": "208.67.220.220",
	"Cloudflare 1": 	"1.1.1.1",
	"Cloudflare 2": 	"1.0.0.1",
	"CleanBrowsing 1": "185.228.168.9",
	"CleanBrowsing 2": "185.228.169.9",
	"Verisign 1": "64.6.64.6",
	"Verisign 2": "64.6.65.6",
	"Alternate DNS 1": "198.101.242.72",
	"Alternate DNS 2": "23.253.163.53",
	"AdGuard DNS 1": 	"94.140.14.14",
	"AdGuard DNS 2": 	"94.140.15.15"
}

for ns in nameservers:
	try:
		print(ns)
		r = dns.resolver.Resolver()
		r.timeout = 2
		r.lifetime = 2
		r.nameservers = [nameservers[ns]]
		answer = r.query(site, 'A')
		if answer.rrset is not None:
			print(answer.rrset)
	except dns.exception.Timeout:
			print("DNS Timeout for", site, "using", r.nameservers[0])
			r.nameservers.remove(r.nameservers[0])
			pass
