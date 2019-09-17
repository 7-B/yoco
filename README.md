
<h1 align="center">
  <br>
  <a href="https://141.223.140.22"><img src="https://github.com/7-B/yoco/blob/modify-readme/YOCO-logo.png" alt="YOCO" width="200"><a>
  <br>
</h1>

## Contents  

- [**Weekly Record**](https://github.com/7-B/yoco/wiki/Development-Record)  
- [**Reference**](https://github.com/7-B/yoco/wiki/%EC%B0%B8%EA%B3%A0-%EC%9E%90%EB%A3%8C)  


<h4 align="center"> 사용자가 정한 이미지로 컬러링북을 제작합니다.</h4>


## Getting Started

`git clone https://github.com/7-B/yoco.git`


### Prerequisites

> Ubuntu 16.04 LTS  
> Python>=3.6  
> torch==0.4.1  
> cuda==9.0  
> and so on...  


### Installing

#### Setting with local environment (not recommended)

```
# install requirements on your local environment
$ pip install -r requirements.txt
```

#### Setting with Anaconda (recommended)

**Option1.** You can install Anaconda in [here](https://www.anaconda.com/distribution/)

```
# create virtual envrionment using conda with python3.6
$ conda create -n yoco python=3.6

# activate virtual environment named yoco
$ conda activate yoco

# install requirements 
$ pip install -r requirements.txt

# install pytorch
$ conda install pytorch=0.4.1 cuda90 -c pytorch

#install opencv
$ pip install opencv-python  
작성 중
```

**Option2.** or you can use environment.yml to create whole conda environment.

```
$ conda env create -f environment.yml
```


## Running the tests

move to yoco project root and run example.

```
$ cd yoco
$ python app.py
작성중
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used  
* [gunicorn](http://docs.gunicorn.org/en/stable/index.html) - WSGI Server  

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **김덕민** - [Github](https://github.com/dimsim21)  
* **김  준** - [Github](https://github.com/rlawns324)  
* **노희태** - [Github](https://github.com/heetea)  
* **서유라** - [Github](https://github.com/SEO-YURA)  
* **이세원** - [Github](https://github.com/Crispiness)  
* **진예진** - [Github](https://github.com/YEEN6)  
* **한미희** - [Github](https://github.com/miheeee)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
