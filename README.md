
<h1 align="center">
  <br>
  <a href="https://141.223.140.22"><img src="https://github.com/7-B/yoco/blob/modify-readme/YOCO-logo.png" alt="YOCO" width="200"><a>
  <br>
</h1>

## Contents  

- [**Weekly Record**](https://github.com/7-B/yoco/wiki/Development-Record)  
- [**Reference**](https://github.com/7-B/yoco/wiki/%EC%B0%B8%EA%B3%A0-%EC%9E%90%EB%A3%8C)  
- [**Demo Video**](https://www.youtube.com/watch?v=Zw67sh-4jSI)  

<h4 align="center"> 사용자가 정한 이미지로 컬러링북을 제작합니다.</h4>

## Development Environments  
- OS : Unutn 16.04 LTS  
- Editor : VScode  
- Virtual Envrionment : Anaconda  


## Getting Started
`git clone https://github.com/7-B/yoco.git`

### Installing

#### Setting with Anaconda (recommended)

You can install Anaconda in [here](https://www.anaconda.com/distribution/)

```
# create virtual envrionment using conda with python3.6
$ conda create -n yoco python=3.6

# activate virtual environment named yoco
$ conda activate yoco

# move into project directory
$ cd yoco
# now you are in ~/yoco

# install requirements, it may takes a few minutes
# 여기서 필요한 패키지가 전부 깔리진 않고, 일부는 conda 명령어로 설치해야 함.
$ pip install -r requirements.txt

# install pytorch
$ conda install pytorch=0.4.1 cuda90 -c pytorch

# install openCV  
$ conda install -c conda-forge opencv  

# Download pre-trained model(이미 트레이닝 된 선따기 해주는 GAN 모델을 다운받는다.)  
$ bash download_models.sh  

# install potrace  
$ conda install -c bioconda potrace  

# 이상이 없었다면 필요한 Package는 모두 설치한 것.
```

## Running the tests

move to yoco project root and run example.

```
# 웹페이지 실행
$ cd yoco
$ python app.py
http://0.0.0.0:8000/ 에 접속하여 웹 페이지에 나와있는 가이드를 따른다.  
```

## Deployment(Web)  

Add additional notes about how to deploy this on a live system

## Built With

* [flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used  
* [gunicorn](http://docs.gunicorn.org/en/stable/index.html) - WSGI Server  

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

#### 문의사항이 있디면, rlawns3244@naver.com 으로 자유롭게 연락주세요. ^^  
