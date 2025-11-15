# AI_X_project
I will train yolov11 with BDD-100K dataset


YOLO에 데이터를 학습시키기 위해서는 YOLO format에 맞게 구조를 넣어주어야 한다.
yolo에 custom 한 데이터셋을 넣기 위해서는 크게 두가지를 충족 시켜야 한다.

먼저 dataset의 구조이다. 
<img width="764" height="601" alt="image" src="https://github.com/user-attachments/assets/774dcd85-18a2-4b44-8e94-014c474b0d11" />
위와 같은 구조로 되어야 하기 때문에 BDD-100K 데이터셋을 받아온 후 위와 같이 정리해주었다.

아래는 편의를 위해 쉘 스크립트를 작성해 두어서 데이터셋을 다운 받은후 아래의 쉘 스크립트를 실행하면 위와 같은 구조로 데이터 셋을 정리 할 수 있다.

(여기에 코드 쓰기)


그리고 YOLO는 .txt 파일 형식을 원하는데 라벨링된 format은 다음과 같다. 

class x_center y_center width height  

<img width="832" height="780" alt="image" src="https://github.com/user-attachments/assets/a3ac8eae-9235-410d-a504-20540278a70b" />

그러나 BDD-100K 데이터셋의 경우 저렇게 되어 있지 않기 때문에 변형을 해주어야 한다. 


추가적인 정보는 
https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format 
