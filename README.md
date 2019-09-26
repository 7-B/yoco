
<h1 align="center">
  <br>
  <a href="https://141.223.140.22"><img src="img/YOCO-logo.png" alt="YOCO" width="200"><a>
  <br>
</h1>

## Contents  

- [**Weekly Record**](https://github.com/7-B/yoco/wiki/Development-Record)  
- [**Reference**](https://github.com/7-B/yoco/wiki/%EC%B0%B8%EA%B3%A0-%EC%9E%90%EB%A3%8C)  
- [**Demo Video**](https://www.youtube.com/watch?v=Zw67sh-4jSI)  

<h4 align="center"> 사용자가 정한 이미지로 컬러링북을 제작합니다.</h4>

## Development Environments  
- OS : Ubutn 16.04 LTS  
- ImageMagick   
- Editor : VScode, Pycharm, Vim     
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
$ conda activate yoco
$ cd yoco

# VScode, Pycharm, Vim 등 파이썬을 사용할 수 있는 에디터에서 app.py를 실행한다.
# 단, Python Interpreter는 아까 만들었던 yoco 가상환경이어야 한다.  
$ python app.py
http://0.0.0.0:8000/ 에 접속하여 웹 페이지에 나와있는 가이드를 따라 테스트 해본다. 이미지를 넣으면 약 10초후 페이지가 바뀌며, 색칠할 수 있는 컬러링북이 생성된다. 
```

## Pattern  
- [Demo Video](https://youtu.be/jX-nO-Tvo8Q)  
- 이미지를 전처리(Segmentation, Style Transfer)하여 원하는 부위에 패턴을 입힙니다.        
- 작성 예정(진예진)    


## Deployment(Web 배포)   
- 작성 예정(이세원)  


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
