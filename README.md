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







이제 다운받은 데이터셋을 바로 YOLO에 학습시키면 좋을 것 같지만 
YOLO에 데이터를 학습시키기 위해서는 YOLO format에 맞게 구조를 넣어주어야 한다.
yolo에 custom 한 데이터셋을 넣기 위해서는 크게 두가지를 충족 시켜야 한다.

먼저 dataset의 구조이다. 
<img width="764" height="601" alt="image" src="https://github.com/user-attachments/assets/774dcd85-18a2-4b44-8e94-014c474b0d11" />
위와 같은 구조로 되어야 하기 때문에 BDD-100K 데이터셋을 받아온 후 위와 같이 정리해주었다.

또한  YOLO는 label(정답지라고 생각하면 편하다)들을 .txt 파일 형식을 원하는데 라벨링된 format은 다음과 같다. 

class x_center y_center width height  

<img width="832" height="780" alt="image" src="https://github.com/user-attachments/assets/a3ac8eae-9235-410d-a504-20540278a70b" />

그러나 BDD-100K 데이터셋의 경우 저렇게 되어 있지 않기 때문에 변형을 해주어야 한다. 
위와 같이 변형을 해주는 package를 만들어 두었으니 다음과 같이 실행하면 된다.

git clone ~ 이거 하고
YOLO도 설치해야하고, bdd-100k_to_yolo 를 변형하기 위해서는 requirement들이 필요해서 파이썬 가상환경을 권장한다. 


2. 가상환경 만들기 및 가상환경 키키

python3 -m venv venv  
source ./venv/bin/activate

3. 필요한 dependencies 설치

cd bdd_to_yolo
pip3 install -r requirements.txt
pip install PyYAML
pip install opencv-python


4-1. BDD-100K 데이터셋 중 필요한 부분 필터링

우리 팀의 프로젝트의 경우 10만장의 데이터를 모두 쓰기에는 무리가 있고, 우리 팀이 사용하기로 했던 데이터는 이 중에서도 몇가지의 필터링이 핑요했다. 

<img width="1155" height="310" alt="image" src="https://github.com/user-attachments/assets/d497ad85-8e85-4c53-bcba-14c67aeff609" />

위 사진은 BDD-100K 논문 중 figure를 가져온 것이다. 우리는 이 중에서도 우리팀의 목적에 맞게 

weather은 "clear" 한 경우
scene 은 상관이 없도록 
timeofday는 "daytime" 으로 한정하였고 

이미지의 train, val, test의 경우도 개수를 한정하여 사용하였다. 

mae_bdd_subset/config.yaml에 추후 개발 편의를 위해서 변경을 용이하게 해 두었으니 참고하길 바란다.



python3 make_bdd_subset.py --config config.yaml

위 .py를 실행하고 나면 bdd_to_yolo 디렉토리 밑에 bdd100k_subset_filtered 가 만들어질 것이다.



4-2. bdd-100k 데이터셋을 yolo에 맞게 변환 시키기 시작

bdd_to_yolo 디렉토리에 들어간 후 

python3 converter.py 

위 실행을 마치고 난 후   

<img width="1107" height="825" alt="image" src="https://github.com/user-attachments/assets/77d54f7a-8e0b-41a2-abca-3cbf8f6161d3" />

위와 같이 정상적으로 변형이 된 것을 볼 수 있다.



5. 매칭이 완벽하게 끝났는지 확인하기 (옵션이지만 하는 것을 매우 권장한다.)

실행 후 주피터 노트북을 통해 시각적으로 과연 결과와 matching이 잘 되었는지 확인할 수 있게 해 두었다.
주피터 노트북을 실행하고 (기본 경로는 train들의 데이터들이 잘 matching이 되어 있는지 확인이 되어 있다.)
val 이나 test의 경우들도 matching 확인을 해보는 것을 권장한다.

<img width="1168" height="578" alt="image" src="https://github.com/user-attachments/assets/5a87ee15-9d39-42c9-897e-480904a617c3" />

위 와 같이 정상적으로 matching이 완료된 것을 볼 수 있다.


-------------------------------------------------------------

데이터셋을 변형하는 과정이 끝났으므로 이제 본격적으로 YOLO 학습을 진행해야한다.

일단 실행을 하기 위해서는 yolo를 설치해주어야 한다.

아까 이미 해당 가상환경을 실행을 시켰을 것이므로 그 가상환경에서 

pip install ultralytics 

YOLO에 관련한 코드들은 scripts에 있다.

YOLO11 이라 하더라도 크기에 따라 다양한 모델이 있는데 우리 팀은 컴퓨팅 환경을 고려하여
yolo11n.pt를 기본 모델로 진행하였다.



각 파일이 있으므로 간단히 설명을 하도록 하겠다.

yolo_predict_notrain.py 
- 위 파일은 그냥 YOLO11 에서 제공하는 기본 모델로 우리 data 이미지를 예측해본것이다. 당연히 yolo11n.pt는 coco 데이터셋으로 학습되어서 우리가 원하는 lane과 같은 부분들은 정답을 제공하지 않지만 꽤 좋은 성능을 보여준다.

yolo_predict_trained.py
-위 파일은 우리가 학습시킨 모델로 data 이미지를 예측해는 것이다.

yolo_train.py
-위 파일은 yolo 학습을 진행하고 .onnx 파일로 보내는 과정을 포함하고 있다.








추가적인 정보는 
https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format 











