from tqdm import tqdm
import time
import sys


print("\nGatheringLocation info...")

time.sleep(1)

for i in tqdm(range(50), desc='Searching                      '):
    time.sleep(0.037)

time.sleep(1)

print("\nDumping Location data")
time.sleep(1)
loc='''

Location

Coordinates: 26.230371445944645, 50.583153517874486
Country: BH
City: Manama
Road: 716 
Block: 307

Google Maps Link
https://www.google.com/maps/place/Rd+No+716,+Manama/@26.2249265,50.5732468,7705m/data=!3m1!1e3!4m5!3m4!1s0x3e49af5baf1971b5:0x213571e4f701fca8!8m2!3d26.23043!4d50.5831867
'''



for c in loc:
    time.sleep(0.05)
    print(c, end = '')
    sys.stdout.flush()

print("\n")

print("Generating ASCII image of the map")