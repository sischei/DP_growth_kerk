# DP growth kerk

This is a introductory course for Kerk Philipps on how to use adaptive sparse grids in economic applictions.
The material is based on a course that was held at the 
Open Source Macroeconomics Laboratory Bootcamp (BFI, University of Chicago) in July 2018.

This repository should serve as a starting point to transform the framework into 
a solver for OLG models.

v1.: Kerk Philipps, Simon Scheidegger, July 2018


### Prerequisites

```
mpi4py
python 2.7
```

### introductory material

```
$cd /doc
```
* SG_lecture_1.pdf -- introductory lecture on sparse grids

* SG_lecture_3.pdf -- analytical examples computed with sparse grids

* SG_lecture_4.pdf -- detailed explanation on how to solve an infinite-horiizon growth model with sparse grids and dynamic programming


### Cache your GitHub username and password

```
$ git config --global credential.helper cache
$ git config --global credential.helper 'cache --timeout=3600'
```

### Checking out the sources

```
git clone https://github.com/sischei/DP_growth_kerk.git```
```

### Installing the library

```
./install_SG.sh
```

### Running analytical examples

```
$cd src/analytical_examples/TASMANIAN_Python
$python OSM_example.py

```

### Running the growth model

```
$cd src/growth_model
$python main.py

```


