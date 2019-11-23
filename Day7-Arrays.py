#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())

arr = list(map(int, input().rstrip().split()))
rarr = map(str, arr[::-1])
print(" ".join(rarr))
