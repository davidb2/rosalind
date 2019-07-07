#!/usr/bin/env bash
FILE=''

read -r -d '' -p '' FILE <<"EOF"
#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  pass


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('name', type=str)
  parser.add_argument('-n', type=int, required=True)
  parser.add_argument('-x', nargs='+', type=float)

  args = parser.parse_args()
  main(args)
EOF

echo "$FILE" > "$1.py"
chmod u+x "$1.py"
