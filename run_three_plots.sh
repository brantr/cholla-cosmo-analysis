#!/usr/bin/bash
#python3 plot_density.py --help
export i=230
python3 plot_density.py    --snapshot ${i} --izmax 512 --output fitsmap-pngs/density_${i}.png
python3 plot_energy.py     --snapshot ${i} --izmax 512 --cmap cubehelix --output fitsmap-pngs/energy_${i}.png -v
#python3 plot_energy.py     --snapshot ${i} --izmax 512 --cmap winter --output fitsmap-pngs/energy_${i}.png -v
python3 plot_gas_energy.py --snapshot ${i} --izmax 512 --cmap gist_heat --output fitsmap-pngs/gas_energy_${i}.png -v
