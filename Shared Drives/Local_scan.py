import os

try:
  import re
except(e):
  os.system('pip install re')
  
# Runs Nmap with the local search command
os.system('nmap --script smb-enum-shares -p 445 192.168.1.0/24 -oN smb_shares.txt')

# Open the Nmap output file
with open('smb_shares.txt', 'r') as file:
    data = file.read()

# Regular expression to find IP addresses with shared drives
pattern = re.compile(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)\n.*?445/tcp open  microsoft-ds', re.DOTALL)

# Find all matches
matches = pattern.findall(data)

# Print the IP addresses
for match in matches:
    os.system(f'crackmapexec -smb {match} --shares')
