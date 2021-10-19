
from tqdm import tqdm
import time
import sys

for i in tqdm(range(100), desc='Looking for Device info'):
    time.sleep(0.017)

time.sleep(2)
print("Dumping Device info...")

lmao='''

..............                                     [darindenny75@gmail.com]kali@kali
            ..,;:ccc,.                             ---------------------
          ......'\'';lxO.                           OS: Windows 10 x64
.....'\'''..........,:ld;                           Host: Lenovo V14-IIL Laptop - Type 82C4 
           .';;;:::;,,.x,                          Kernel: Windows NT 10.0; Win64; x64
      ..'\''.            0Xxoc:,.  ...              Orientation: landscape-primary 
  ....                ,ONkc;,;cokOdc',.            Resolution: 1366 x 768
 .                   OMo           ':ddo.          DE: Windows 10 Dark
                    dMc               :OO;         CPU: Intel(R) i5-1035G1 @ 1.000GHz 
                    0M.                 .:o.       GPU: Intel(R) UHD Graphics
                    ;Wd                            Memory: 12GiB 
                     ;XO,                          Battery: Unknown
                       ,d0Odlc;,..                 
                           ..',;:cdOOd::,.         Date/Time: 2021-10-13 11:13:55 UTC 
                                    .:d;.':;.      IP: 95.84.93.156
                                       'd,  .'     ISP: Stc Bahrain B.s.c Closed
                                         ;l   ..   Browser: Chrome (94.0.4606.81)                        
                                          .o       Ad Blocker: No                        
                                            c      Language: en-US
                                            .'     User Time: Wed Oct 13 2021 14:13:56 GMT+0300 (Arabian Standard Time)
                                             .
'''

for c in lmao:
    time.sleep(0.009)
    print(c, end = '')
    sys.stdout.flush()


print("Looking for Facebook account linked to darrindenny75@gmail.com")

time.sleep(1)

for i in tqdm(range(50), desc='Searching                      '):
    time.sleep(0.037)

time.sleep(1.2)

print("Target found, downloading images                       ")

for i in tqdm(range(38), desc='Downloading images             '):
    time.sleep(0.04)

time.sleep(2)

print("Dumping images...")
for i in tqdm(range(38), desc='Loading dumped images          '):
    time.sleep(0.04) 
