# Install entire sparse grid libraries, IPOPT and PYIPOT at once

# unpack and compile Tasmanian Sparse grid library, and test python example
unzip TasmanianSparseGrids_v4.0.zip
cd TasmanianSparseGrids
make
# cd InterfacePython
# python example.py  ##test
echo " Tasmanian library is installed "

# Install IPOPT and PYIPOPT
cd ../
cd pyipopt_midway
./install.sh
echo " IPOPT and PYIPOPT is installed "


