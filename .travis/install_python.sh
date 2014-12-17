#! /bin/bash

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    OS="MacOSX-x86_64";
else
    OS="Linux-x86_64";
fi
sudo apt-get update 2> /dev/null || echo "No apt-get"
if [[ "$TRAVIS_PYTHON_VERSION" == 2.* ]]; then
      wget http://repo.continuum.io/miniconda/Miniconda-latest-$OS.sh -O miniconda.sh;
else
      wget http://repo.continuum.io/miniconda/Miniconda3-latest-$OS.sh -O miniconda.sh;
fi
echo "Install miniconda"
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
echo "Using this conda: $(which conda)"
hash -r
conda config --set always_yes yes --set changeps1 no
echo "Update conda"
conda update -q conda
echo "conda info"
conda info -a
echo "Install packages"
cat requirements.txt | xargs conda create -q -n test-env python=$TRAVIS_PYTHON_VERSION
echo "Activate environment"
source activate test-env
echo "Using this python: $(which python)"
conda install coverage
conda install sphinx
