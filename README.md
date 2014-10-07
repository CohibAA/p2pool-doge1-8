A fork of [Rav3nPL](https://github.com/Rav3nPL/p2pool-rav)'s p2pool-rav to support Dogecoin v1.8 (DOGE) p2pool support for the DOGE 1.8 wallet fork.

NOTE: Please notify me of any issues.  The source has been tested for DOGE 1.8 and is in production currently on an Ubuntu 14.04 Server at [http://www.dogecoin-p2pool.com](http://www.dogecoin-p2pool.com)

NOTICE: the hash rate on the Doge p2pool network is very low due to [LTC p2pool](http://www.litecoin-p2pool.com) merge mining, so expect significant variance on payouts, especially with low hash rates.


Build Requirements:
-------------------------
Generic:
* Bitcoin >=0.8.5
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages


Notes for Litecoin and Dogecoin Support:
=========================
Requirements:
-------------------------

In order to run P2Pool with the Litecoin or Dogecoin 1.8 network, you need to build and install the included
ltc_scrypt module which provides the scrypt proof of work code that Litecoin uses for hashes.

Linux:

    cd ~
    git clone https://github.com/CohibAA/p2pool-doge1-8.git ~/p2pool-doge
    cd ~/p2pool-doge/litecoin_scrypt
    sudo python setup.py install
    cd ..

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local dogecoind (or other wallet server).
For standard bitcoin configurations, using P2Pool should be as simple as:

    python ~/p2pool-doge/run_p2pool.py
    
A normal dogecoind 1.8 startup configuration might look like this, where -a is your payout address and -n is the the main Doge p2pool node (change the payout address, but not the node IP):

    python ~/p2pool-doge/run_p2pool.py --net dogecoin -a DQfThymvPs1bgCjPvmkmpUYJtiLSFQBmok -n 54.68.63.254

Then run your miner program, connecting to 127.0.0.1 on port 9332 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    1939BZFZnHEdKyHn2cYrg8kbUPz1UgkuqQ (BTC)
    DQfThymvPs1bgCjPvmkmpUYJtiLSFQBmok (DOGE)
    LcjmUck1PB2dZun9My9N2W8hwFpAfeEkfP (LTC)
    

This git currently also supports the following altcoins:

Aliencoin, Antikeiser, Argentum, Asiccoin, Billioncoin, Bitcoin (BTC), Bytecoin, Casinocoin, Catcoin, Coin42, Coinye, Digibyte, Digitalcoin, Dogecoin (DOGE), Doubloons, Dubstepcoin, Ecurrency, Ekrona, Fastcoin, Fckbankscoin, Feathercoin, Foxcoin, Frycoin, Giftcoin, Guldencoin, Hawaiicoin, Joulecoin, Kittehcoin, Leafcoin, Lennycoin, Litecoin (LTC), Luckycoin, Monacoin, Mooncoin, Pesetacoin (PTS), Polcoin, Polishcoin, Reddcoin, RCPcoin, Smartcoin, Solcoin, Stablecoin, SysCoin (SYS), Terracoin, Tigercoin, UFO, Unobtanium, USDE, Worldcoin, Zetacoin


Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd


Running P2Pool:
-------------------------
Run P2Pool with the "--net litecoin" or "--net dogecoin" option.
Run your miner program, connecting to 127.0.0.1 on port 9327.
Forward port 9338 to the host running P2Pool.

Litecoin's use of ports 9332 and 9332 conflicts with P2Pool running on
the Bitcoin network. To avoid problems, add these lines to litecoin.conf
and restart litecoind.  This should not affect Dogecoin ports:

    rpcport=10332
    port=10333

Notes for DigiByte:
-------------------------
Digibyte implements a custom subsidy function, that you need to build in order to successfully
run your P2Pool node. See digibyte_subsidy/README.txt for installation details.

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
* Rav3nPL for contributions to p2pool nodes
