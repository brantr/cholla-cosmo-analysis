#!/usr/bin/bash
#python3 plot_density.py --help

export CDIR=2048_50Mpc_v22_DESI/OmegaM_CosmoConstant_Study/2048_50Mpc_v22_DESI_CMB_Pantheon_CosmoConstant/data
export NFILE=17
python3 plot_temperature.py  --nprocs 512 --snapshot ${NFILE} --izmin 0 --izmax 512 --output plots/temperature_${NFILE}.png --dir ${CDIR} --cmap gist_heat
