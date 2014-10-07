from p2pool.bitcoin import networks

PARENT = networks.nets['dogecoin']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 12*60*60//15 # shares
REAL_CHAIN_LENGTH = 12*60*60//15 # shares
TARGET_LOOKBEHIND = 20 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = 'AF69154D2CE1B4CE'.decode('hex')
PREFIX = 'B353F75435546C41'.decode('hex')
P2P_PORT = 8555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = '54.68.63.254'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
