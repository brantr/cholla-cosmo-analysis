#!/usr/bin/bash
#python3 plot_density.py --help

export NFILE=1
python3 plot_density.py --nprocs 8 --snapshot ${NFILE} --izmin 0 --izmax 128 --output plots/1.png
