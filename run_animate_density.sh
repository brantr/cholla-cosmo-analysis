#!/usr/bin/bash
#python3 plot_density.py --help
#python3 plot_density.py --snapshot 180 --izmax 512 --output plots/180.png
#for i in $(seq 0 190);
for i in $(seq 135 190);
do
    #echo $i
    python3 plot_density.py --snapshot $i --izmax 512 --output plots/$i.png
done
