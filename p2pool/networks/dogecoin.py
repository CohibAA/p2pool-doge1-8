from p2pool.bitcoin import networks

PARENT = networks.nets['dogecoin']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 12*60*60//15 # shares
REAL_CHAIN_LENGTH = 12*60*60//15 # shares
TARGET_LOOKBEHIND = 20 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = '42654e6963655472794861766546756e'.decode('hex')
PREFIX = '54727942654e6963654861766546756e'.decode('hex')
P2P_PORT = 8555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
