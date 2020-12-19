#! /usr/bin/python     
# -*- coding: utf-8 -*-
import sys
import dns
import dns.resolver
import re
nameservers = {
    "dns5.home.pl": "62.129.252.215",
    "dns4.home.pl": "62.129.252.252",
    "Politechnika Bialostocka": "212.33.80.231",
    "Orange1": "212.244.48.137",
    "Orange2": "79.187.201.181",
    "Orange3": "79.187.201.179",
    "Orange4": "79.190.224.27",
    "Orange5": "212.244.78.90",
    "Orange6": "83.19.241.2",
    "Orange7": "80.55.253.114",
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
