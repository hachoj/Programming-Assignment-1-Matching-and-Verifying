#!/bin/bash

python analysis/benchmark.py
python analysis/plot_runtime.py
python main.py -i data/example.in -o data/example.out -v
pytest