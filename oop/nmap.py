import nmap
begin=44
end=80

target= "192.168.10.5"

nm = nmap.PortScanner()


for i in range(begin,end+1):
    res = nm.scan(target,str(i))
    res = nm['scan'][target]['tcp'][i]['state']
    print(f"port {i} is {res}")
