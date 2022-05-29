#sudo conda install conda-build
#conda install anaconda-client
#anaconda login

conda-build .

conda convert --platform all ~/opt/*conda3/conda-bld/osx-64/ipyreload-*.tar.bz2 -o converted/

anaconda upload ./converted/*/*.tar.bz2
