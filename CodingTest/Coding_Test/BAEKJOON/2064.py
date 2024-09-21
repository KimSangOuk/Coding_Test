n=int(input())
ips=[]

for i in range(n):
    ip=list(map(int,input().split('.')))
    ips.append(ip)

def makeNetworkIP(ips):
    ipNetwork=[0]*4
    netWorkMask=[0]*4
    for byte in range(4):
        for bit in range(8):
            defaultBit=(ips[0][byte]>>(8-1-bit))&1
            for i in range(1,n):
                if defaultBit^((ips[i][byte]>>(8-1-bit))&1):
                    return ipNetwork,netWorkMask
            ipNetwork[byte]|=(defaultBit<<(8-1-bit))
            netWorkMask[byte]|=1<<(8-1-bit)
    return ipNetwork,netWorkMask

ipNetwork,netWorkMask=makeNetworkIP(ips)
print(".".join(map(str,ipNetwork)))
print(".".join(map(str,netWorkMask)))