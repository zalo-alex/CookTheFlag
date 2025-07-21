from src.module import Module
from src.layout import *
from src.regexs import RegExs
from src.exec import Exec

import json
import dns.resolver

class CustomModule(Module):
    name = "DNS Lookup"
    category = "tool"
    layout = [
        Input("Domain name", "dn-input", regex=RegExs.DOMAIN),
        Submit("Lookup", "lookup"),
        Input("WHOIS", "whois-output", textarea=True),
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
                all_records[record_type] = [f"Error: {str(e)}"]
            all_records[record_type] = "\n".join([ " - " + record for record in all_records[record_type] ])

        return "\n\n".join([f"{record[0]}:\n{record[1]}" for record in all_records.items()])
    
    def submit(type, data):
        yield {
            "records-output": CustomModule.get_all_dns_records(data["dn-input"]),
        }
    
        yield from Exec(["whois", data["dn-input"]]).stream_output("whois-output")