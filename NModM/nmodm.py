# N Mod M solution in Python 2 for CodeEval.com by Steven A. Dunn

import sys

for line in open(sys.argv[1], 'r'):
  line = line.rstrip('\n').split(',')
  N = int(line[0])
  M = int(line[1])

  x = N / M
  y = x * M
  mod = N - y

  print mod
