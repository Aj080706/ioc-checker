import requests

API_KEY = "your_api_key_here"

def check_hash(hash):
    url = f"https://www.virustotal.com/api/v3/files/{hash}"
    headers = {"x-apikey": API_KEY}
    response= requests.get(url, headers=headers)
    return response.json()


def check_ip_address(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": API_KEY}
    response= requests.get(url, headers=headers)
    return response.json()

    

def check_domain(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"x-apikey": API_KEY}
    response= requests.get(url, headers=headers)
    return response.json()



def print_result(result, ioc_value):
    stats = result['data']['attributes']['last_analysis_stats']
    print(f"Malicous: {stats['malicious']}")
    print(f"Suspicious: {stats['suspicious']}")
    print(f"Harmless: {stats['harmless']}")
    print(f"Undetected:{stats['undetected']}")
    if stats['malicious']>10:
        print("Verdict : High Risk")
    elif stats['malicious']>0:
        print("Verdict:Suspicious")
    else:
        print("Verdict: Clean")
    

print("="*50)
print("       IOC CHECKER - SOC TOOL")
print("="*50)


ioc_type = input("Enter IOC type (hash/ip/domain): ")
value = input("Enter IOC value: ")

result = "none"

if ioc_type == "hash":
    result = check_hash(value)
elif ioc_type == "ip":
    result = check_ip_address(value)
elif ioc_type == "domain":
    result = check_domain(value)
else:
    print("invalid")

print_result(result, value) 
    
    

