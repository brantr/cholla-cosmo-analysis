#!/usr/bin/bash
#python3 plot_density.py --help

export CDIR=2048_50Mpc_v22_DESI/OmegaM_CosmoConstant_Study/2048_50Mpc_v22_DESI_CMB_Pantheon_CosmoConstant/data
export NFILE=17
python3 plot_density.py     --nprocs 512 --snapshot ${NFILE} --izmin 0 --izmax 512 --output plots/density_${NFILE}.png --dir ${CDIR}
python3 plot_energy.py      --nprocs 512 --snapshot ${NFILE} --izmin 0 --izmax 512 --output plots/energy_${NFILE}.png --dir ${CDIR} --cmap cubehelix
python3 plot_gas_energy.py  --nprocs 512 --snapshot ${NFILE} --izmin 0 --izmax 512 --output plots/gas_energy_${NFILE}.png --dir ${CDIR} --cmap gist_heat
