# Project YOCO(Your Own Coloring book)  


## Contents  


- [**Weekly Record**](https://github.com/7-B/yoco#weekly-recordsweek1week5)  
- [**Reference**](https://github.com/7-B/yoco/wiki/%EC%B0%B8%EA%B3%A0-%EC%9E%90%EB%A3%8C)  
-  
-   


# Weekly records(Week1~Week5)    
 
<details>
<summary> Week1 </summary>
<div markdown="1">
- Test opensource style transfer  [Deep Photo Style Transfer ](https://arxiv.org/abs/1703.07511)[(Github repo)](https://github.com/luanfujun/deep-photo-styletransfer)   

> <img src="data/base1.jpg" width="200"> **+** <img src="data/suzy.png" width="150">  **=**   <img src="data/week1_suzy_result_.gif" width="150">     

> <img src="data/base2.png" width="200"> **+** <img src="data/bird.jpg" width="150">  **=**   <img src="data/week1_bird_result_.gif" width="150">     


- __문제점__ : 얼굴,피부,머리,옷,배경 등을 Segmentation시킬 필요가 있음, 노이즈 제거 등    
---  
- ### 회의기록    
**1. 목표(구체적으로)**   
  - 내사진(input) -> 컬러링북(output)   
  **Our Goal :** <img src="data/moana_raw.jpg" width="300"> **->** <img src="data/moana_converted.png" width="200"> 
  - 차별점 : 그냥 선따기만 하는게 아니고, 일정한 패턴들이 폐곡선을 구성하여 시중 컬러링 북과 같은 느낌을 내는 것.   
  - GAN/Image Segmentation등 으로 1차 이미지 생성 -> Edge Detection/Denoising autoencoder 와 같은 기법으로 다듬어서 결과 이미지 생성   

**2. (예상)데이터셋 구축 & 모델링 방법 제안**   
  - 3 Suggestions    
  - 1. 희태 + 준
  - 2. 세원+유라
  - 3. 예진+미희+ 덕민  

**3. 필요 기술(필수) 및 요구사항**  
- 데이터셋을 어떻게 구성 할 것인지(가장 중요할 듯)  
- GAN을 적용하여 어떻게 컬러링북스타일을 학습/추론 할 것인지(How to determine What Generator/Discriminator is?)  
- ~~(오브젝트디텍션+세그멘테이션+라벨링)->YOLO로? But, YOLO는 외곽선따는게 아니고 Bounding Box 생성하는 문제점~~ -> YOLO는 segmentation하지 않음, mmdetection으로 segmentation     
- Input 사진 제한해야할 것으로 예상됨(ex: 사람 상반신 사진)   
- (추후)Edge Detection/Denoising autoencoder 와 같은 후처리 기법 조사 필요  
- [현재 Edge Detection 방법으로는 딱 이거다 라고 결정 지을 수는 없음(Controversial한 영역)](https://www.reddit.com/r/computervision/comments/8jjkjp/what_is_the_state_of_the_art_algorithm_for_edge/) -> 우리 프로젝트에 적합한 엣지검출 방법을 찾아야함  

- 0824토요일  
  - [mmdetection](https://github.com/open-mmlab/mmdetection)으로 인물/배경 분리 성공  
  > <img src="data/segtest.jpg" width="200">   
  - 자세한 알고리즘은 슬라이드에  
  - 선을 딴 이미지에다가 패턴을 합성할 때에 어떤 기술을 적용해야 하는지 의문. -> 당장은 GAN이 떠오르긴 하지만, GAN은 연속적인 명암 및 색상을 가진 fake Image를 생성하는 기술인 것 같은데, line image -> Patterned line image인 우리 프로젝트에 GAN을 이용하는것이 맞는건가?  

**4. 더 자세한 계획/역할분담은 연구실 자문 받고 결정**   

</div>
</details>

---  
<details>
<summary> Week2 </summary>
<div markdown="1">
 
</div>
</details>
## Collaborators  
- 김덕민  
- 김  준  
- 노희태  
- 서유라  
- 이세원  
- 진예진  
- 한미희  
