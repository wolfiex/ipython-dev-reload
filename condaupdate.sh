#sudo conda install conda-build
#conda install anaconda-client
#anaconda login

conda-build .

conda convert --platform all ~/opt/anaconda3/conda-bld/osx-64/ipyreload-1.2-py37_0.tar.bz2 -o converted/

anaconda upload ./converted/*/*.tar.bz2
