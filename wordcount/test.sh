#!/bin/bash

python -m cProfile wordcountCppExtension.py --topcount alice.txt
python -m cProfile wordcountCppExtension.py --topcountcpp alice.txt
