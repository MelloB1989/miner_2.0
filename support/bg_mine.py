import os
import sys

wallet = "0xC724ee49DF30f9381c3965C4Bf2E9523Baa39759"
work = sys.argv[1]
start_mining = os.sys('cd && cd //home/ubuntu/gminer && nohup sudo ./miner --algo ethash --api 0.0.0.0:80 --server us1.ethermine.org:4444 --user {}.{} &'.format(wallet, work))
exit