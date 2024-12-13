import re

class Regexs:
    
    BIN = re.compile(r"^(0b)?[01]+(?:\s[01]+)*$")
    HEX = re.compile(r"^(0x)?[0-9a-fA-F]+(?:\s[0-9a-fA-F]+)*$")
    DEC = re.compile(r"^\d+(?:\s\d+)*$")
    
    BASE64 = re.compile(r"^[A-Za-z0-9+\/]{4}*(?:[A-Za-z0-9+\/]{2}([A-Za-z0-9+\/]{2}|[A-Za-z0-9+\/]{1}=|={2}))$")
    
    BLAKE2B = re.compile(r"^[a-fA-F0-9]{128}$")
    BLAKE2S = re.compile(r"^[a-fA-F0-9]{64}$")
    MD5 = re.compile(r"^[a-fA-F0-9]{32}$")
    SHA1 = re.compile(r"^[a-fA-F0-9]{40}$")
    SHA256 = re.compile(r"^[a-fA-F0-9]{64}$")
    SHA512 = re.compile(r"^[a-fA-F0-9]{128}$")
    
    IPV4 = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    IPV4_HEX = re.compile(r"^([0-9a-fA-F]{1,2}\.){3}[0-9a-fA-F]{1,2}$")
    
    DOMAIN = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})*\.[A-Za-z]{2,}$")
    URL = re.compile(r"^https?:\/\/([A-Za-z0-9.-]+)(:[0-9]{1,5})?(\/[^\s]*)?$")