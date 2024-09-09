In this file we gonna take a deep dive into Shared Drives on Windows.
Our tool for now will be nmap then we gonna use CrackMapExec to identify Shared drives on a local network.
Let's begin.

First of all we're gonna need our tools.

```
https://nmap.org
```
^ Download the nmap client and run it.

For this one we're gonna need Python.
```
https://python.org
```
^ Follow the instructions.

Ok let's see. Next we're gonna download CrackMapExec via Python (pip).
```batch
pip install crackmapexec
```
^ Wait till it's installed.

```batch
nmap --script smb-enum-shares -p 445 192.168.1.0/24 -oN smb_shares.txt
```
^ This script will can the local network for the 445 port and gives us the ip's that match in the smb_shares.txt file.
Now if your smb_shares.txt is empty there are no local Shared drives on that network.
Ok but if you see ip's in the smb_shares.txt you have local Shared drives.

Time to get CrackMapExec going. 
Ok for this we gonna need a bit of automation.
We gonna validate our ips.
