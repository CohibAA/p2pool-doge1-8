from p2pool.bitcoin import networks

PARENT = networks.nets['litecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9338
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9327
BOOTSTRAP_ADDRS = 'forre.st vps.forre.st 95.211.21.103 37.229.117.57 66.228.48.21 180.169.60.179 112.84.181.102 74.214.62.115 209.141.46.154 78.27.191.182 66.187.70.88 88.190.223.96 78.47.242.59 158.182.39.43 180.177.114.80 216.230.232.35 94.231.56.87 62.38.194.17 82.67.167.12 183.129.157.220 71.19.240.182 216.177.81.88 109.106.0.130 113.10.168.210 218.22.102.12 85.69.35.7:54396 201.52.162.167 95.66.173.110:8331 109.65.171.93 95.243.237.90 208.68.17.67 87.103.197.163 101.1.25.211 144.76.17.34 209.99.52.72 198.23.245.250 46.151.21.226 66.43.209.193 59.127.188.231 178.194.42.169 85.10.35.90 110.175.53.212 98.232.129.196 116.228.192.46 94.251.42.75 195.216.115.94 24.49.138.81 61.158.7.36 213.168.187.27 37.59.10.166 72.44.88.49 98.221.44.200 178.19.104.251 87.198.219.221 85.237.59.130:9310 218.16.251.86 151.236.11.119 94.23.215.27 60.190.203.228 176.31.208.222 46.163.105.201 198.84.186.74 199.175.50.102 188.142.102.15 202.191.108.46 125.65.108.19 15.185.107.232 108.161.131.248 188.116.33.39 78.142.148.62 69.42.217.130 213.110.14.23 185.10.51.18 74.71.113.207 77.89.41.253 69.171.153.219 58.210.42.10 174.107.165.198 50.53.105.6 116.213.73.50 83.150.90.211 210.28.136.11 86.58.41.122 70.63.34.88 78.155.217.76 68.193.128.182 198.199.73.40 193.6.148.18 188.177.188.189 83.109.6.82 204.10.105.113 64.91.214.180 46.4.74.44 98.234.11.149 71.189.207.226'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-ltc'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Litecoin to >=0.8.5.1!' if v < 80501 else None
