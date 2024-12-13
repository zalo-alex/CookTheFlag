from src.module import Module
from src.layout import *
from src.regexs import Regexs

import json
import whois
import dns.resolver

class CustomModule(Module):
    name = "DNS Lookup"
    category = "Tool"
    layout = [
        Input("Domain name", "dn-input", regex=Regexs.DOMAIN),
        Submit("Lookup", "lookup"),
        Input("DNS Lookup", "lookup-output", textarea=True),
        Input("DNS Records", "records-output", textarea=True),
    ]
    
    def get_all_dns_records(domain):
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'PTR', 'CNAME', 'SRV']
        all_records = {}

        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                all_records[record_type] = [answer.to_text() for answer in answers]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException) as e:
                all_records[record_type] = f"Error: {str(e)}"

        return all_records
    
    def submit(type, data):
        return {
            "lookup-output": str(whois.whois(data["dn-input"])),
            "records-output": json.dumps(CustomModule.get_all_dns_records(data["dn-input"]), indent=4),
        }