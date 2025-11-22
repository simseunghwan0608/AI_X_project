# AI_X_project


데이터셋은 BDD - 100K 를 사용하려고 한다.
YOLO 모델은 v11을 이용하였다.

BDD-100K 
공식 사이트는 http://bdd-data.berkeley.edu/download.html 이고 
여기서 데이터셋을 다운 받을 수 있다!!!

YOLO 
github :
document : 


먼저 BDD-100k 데이터셋 다운에 대해서 설명할 예정이다.


<img width="965" height="409" alt="image" src="https://github.com/user-attachments/assets/a101e81c-80c8-4474-9c47-fa2862b275ae" />

위 사진에서 100K Images, Labels를 클릭해서 다운받아야 한다.
원래는 사진 용량을 위해서 10K Images 를 다운 받았으나 학습하는중에 계속 오류가 발생하여 확인해보니 
10K image/train에 사진중 label이 없는것들이 많아서 학습이 되지 않는다. 
<img width="830" height="380" alt="image" src="https://github.com/user-attachments/assets/89cdf7c6-2e19-45fe-b0dc-51da99bf9697" />

위와 같은 시행착오를 피하기 위해서는 용량과 시간이 오래 걸리더라도 100K Images 와 Labels를 받는것을 권장한다.




이제 다운받은 데이터셋을 바로 YOLO에 학습시키면 좋을 것 깉ㅈ;민 
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
