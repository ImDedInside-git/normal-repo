import time
import sys

time.sleep(2)

somecode = '''
#include <iostream>


using namespace std;

void halftri() {
  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < i; ++j) {
      cout << "*";
    }
    cout << "\n";
  }
}

int main() {
  halftri();
  return 0;
}
'''

print(f"Hacking darrindenny75@gmail.com\'s IP ")

for c in somecode:
    time.sleep(0.1)
    print(c, end = '')
    sys.stdout.flush()

time.sleep(1)


from tqdm import tqdm

print("Looking for Facebook account linked to darrindenny75@gmail.com")

time.sleep(1)

for i in tqdm(range(38), desc='Searching                      '):
    time.sleep(0.04)

time.sleep(1.2)

print("Target found, downloading images                       ")

for i in tqdm(range(38), desc='Downloading images             '):
    time.sleep(0.04)

time.sleep(2)

print("Dumping images...")
for i in tqdm(range(38), desc='Loading dumped images          '):
    time.sleep(0.04)