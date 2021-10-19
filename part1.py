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
    time.sleep(0.0005)
    print(c, end = '')
    sys.stdout.flush()

time.sleep(1)
