<img src="https://raw.githubusercontent.com/jndmose/DArTView/refs/heads/main/client/public/images/snp-64.old.png" width="64">

<hr />

**Table of contents:**
- [About DArTView](#about-dartview)
- [Acknowledgements](#acknowledgements)
- [License](#license)
- [Run as a Docker container](#run-as-a-docker-container)
- [Screenshots](#screenshots)

## About DArTView
DArTview is a web application for marker data curation via metadata filtering. 
Its primary goal is to overcome tedious manual calculation of marker data through common spreadsheet applications like excel. 
It offers a novel approach for gaining insights from genotypic data through sorting, filtering, metadata recalculations and interactive visualization. 

The metadata statistical recalculations enables the user to quickly know how many markers they are loosing based on a metadata filtering criteria.
The instant recalculation also enables the user get rid of monomorphic markers upon filtering.

## Acknowledgements

The original concept and an earlier Java-based implementation of DArTView was developed by <a href="https://www.diversityarrays.com/" style="text-decoration:none" target="_blank">Diversity Arrays Technology</a>
.  
The Java version was coded by **Andrew Kowalczyk** and **Brian Pearce** of Diversity Arrays Technology.  

This project builds upon their pioneering work, reimagined here as a modern web application. Any changes, omissions, or additions are the responsibility of the current authors.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Run as a docker container
`$ git clone https://github.com/jndmose/DArTView.git`   
`$ cd DArTView`   
`$ docker build -t dartview .`   
`$ docker run  -d  -p 3000:3000 dartview`   
Test it on  http://localhost:3000




## Screenshots
![DArTView GUI](https://github.com/jndmose/DArTView/blob/main/client/public/images/un-checked.png?raw=true)

![DArTView GUI](https://github.com/jndmose/DArTView/blob/main/client/public/images/sort.png?raw=true)





