<img src="https://raw.githubusercontent.com/jndmose/DArTView/refs/heads/main/client/public/images/snp-64.old.png" width="64">

<hr />

**Table of contents:**
- [About DArTView](#about-dartview)
- [Installation](#installation)
- [Try out DArTView](#try-out-dartview)
- [Screenshots](#screenshots)

## About DArTView
DArTview is a web application for marker data curation via metadata filtering. 
Its primary goal is to overcome tedious manual calculation of marker data through common spreadsheet applications like excel. 
It offers a novel approach for gaining insights from genotypic data through sorting, filtering, metadata recalculations and interactive visualization. 

The metadata statistical recalculations enables the user to quickly know how many markers they are loosing based on a metadata filtering criteria.
The instant recalculation also enables the user get rid of monomorphic markers upon filtering.

## Run as a docker container

docker build -t dartview .   
docker run  -d  -p 3000:3000 dartview 


## Screenshots
![DArTView GUI](https://github.com/jndmose/DArTView/blob/main/client/public/images/un-checked.png?raw=true)

![DArTView GUI](https://github.com/jndmose/DArTView/blob/main/client/public/images/sort.png?raw=true)





