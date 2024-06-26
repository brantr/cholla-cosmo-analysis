#import sys
#import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from astropy.io import fits
#from astropy.wcs import WCS
import argparse
from tqdm import tqdm
import time
import h5py
mpl.use('Agg')

#######################################
# Create command line argument parser
#######################################

def create_parser():

  # Handle user input with argparse
  parser = argparse.ArgumentParser(
    description="Imaging snapshot options from user.")

  parser.add_argument('--dir',
    dest='dir',
    default='data',
    metavar='dir',
    type=str,
    help='Directory containing snapshots.')

  parser.add_argument('--output',
    dest='output',
    default='out.png',
    metavar='output',
    type=str,
    help='Output image filename.')

  parser.add_argument('--snapshot',
    dest='snapshot',
    default=0,
    type=int,
    help='Snapshot id.')

  parser.add_argument('-n','--nprocs',
    dest='nprocs',
    default=512,
    type=int,
    help='Number of mpi processes.')

  parser.add_argument('--izmin',
    dest='izmin',
    default=0,
    type=int,
    help='Minimum z slice.')

  parser.add_argument('--izmax',
    dest='izmax',
    default=2048,
    type=int,
    help='Maxmium z slice.')

  parser.add_argument('--cmap',
    dest='cmap',
    default='magma',
    metavar='cmap',
    type=str,
    help='Color map.')

  parser.add_argument('-v', '--verbose',
    dest='verbose',
    action='store_true',
    help='Print helpful information to the screen? (default: False)',
    default=False)

  return parser

#######################################
# main() function
#######################################
def main():

  #begin timer
  time_global_start = time.time()

  #create the command line argument parser
  parser = create_parser()

  #store the command line arguments
  args   = parser.parse_args()

  #verbose
  if(args.verbose):
    print(f'Directory {args.dir}.')
    print(f'Snapshot  {args.snapshot}.')
    print(f'Output    {args.output}.')


  #file name
  fdir = f'{args.dir}/{args.snapshot}'

  #loop over nprocs
  for i in tqdm(range(args.nprocs)):
  #for i in tqdm(range(100)):
    fname = f'{fdir}/{args.snapshot}.h5.{i}'
    #print(f'Filename {fname}')

#['Current_a', 'Current_z', 'Git Commit Hash', 'H0', 'Macro Flags', 'Omega_L', 
#'Omega_M', 'bounds', 'cholla', 'density_unit', 'dims', 
#'dims_local', 'domain', 'dt', 'dx', 'energy_unit', 'gamma', 
#'length_unit', 'mass_unit', 'n_fields', 'n_step', 'nprocs', 
#'offset', 't', 'time_unit', 'velocity_unit']
#['Energy', 'GasEnergy', 'density', 'momentum_x', 'momentum_y', 'momentum_z']
#density.shape (256, 256, 256)


    f = h5py.File(fname,'r')
    energy = f['GasEnergy']
    if(i==0):
      energy_image = np.zeros((f.attrs['dims'][1],f.attrs['dims'][0]))
      print(f'Filename {fname}')
      print(list(f.attrs.keys()))
      print(f.attrs['dims'])
      print(f.attrs['dims_local'])
      print(f.attrs['offset'])
      print(list(f.keys()))
      print(f'energy.shape {energy.shape}')
 
    ox = f.attrs['offset'][0]
    oy = f.attrs['offset'][1]
    oz = f.attrs['offset'][2]
    nxl = f.attrs['dims_local'][0]
    nyl = f.attrs['dims_local'][1]
    nzl = f.attrs['dims_local'][2]


    #project a subset of the box energy
    if((oz>=args.izmin)&(oz+nzl<=args.izmax)):
      izmin = np.max( [oz-args.izmin, 0] )
      izmax = np.min( [(args.izmax - (oz+nzl)), nzl] )
      energy_image[ox:ox+nxl,oy:oy+nyl] += np.sum(energy[:,:,izmin:izmax],axis=2)
    

  #save the energyfield
  plt.imsave(args.output,np.log10(energy_image),origin='lower',cmap=f'{args.cmap}')

  #end timer
  time_global_end = time.time()
  if(args.verbose):
    print(f"Time to execute program: {time_global_end-time_global_start}s.")

#######################################
# Run the program
#######################################
if __name__=="__main__":
  main()
