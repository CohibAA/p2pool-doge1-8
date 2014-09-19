A fork of Rav3nPL's p2pool-rav working on re-implementing Dogecoin (DOGE) p2pool support for the DOGE 1.8 wallet fork.

NOTE: This fork is under heavy beta, and likely will not produce accepted blocks on the new DOGE fork.  This readme will be updated when this issue is resolved.  Other alt coins should work as expected in the original version.


Requirements:
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

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local bitcoind (or other altcoin wallet server).
For standard configurations, using P2Pool should be as simple as:

    python run_p2pool.py

Then run your miner program, connecting to 127.0.0.1 on port 9332 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    1PYyUSb426qvVBg3jvX2DPHweEWXNCBNqE

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Notes for Litecoin and Dogecoin Support:
=========================
Requirements:
-------------------------
In order to run P2Pool with the Litecoin/Dogecoin network, you need to build and install the
ltc_scrypt module that includes the scrypt proof of work code that Litecoin uses for hashes.

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

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
