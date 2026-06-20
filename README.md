# ioc-checker
A Python-based IOC checker that queries the VirusTotal API to analyze hashes, IP addresses, and domains — helping SOC analysts quickly identify malicious indicators during threat investigations.

## Requirements
- Python 3.x
- requests library (`pip install requests`)
- VirusTotal API key (free at virustotal.com)

## How to Use
1. Clone the repository
2. Add your VirusTotal API key to the script
3. Run: `python ioc.py`
4. Enter IOC type (hash/ip/domain)
5. Enter the IOC value
6. Get instant verdict

## Example Output
IOC: 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
Malicious: 63
Suspicious: 0
Harmless: 0
Undetected: 2
Verdict: High Risk

## Output screenshot 
<img width="842" height="766" alt="image" src="https://github.com/user-attachments/assets/90213ec6-db35-40a8-86c6-285300792efc" />

