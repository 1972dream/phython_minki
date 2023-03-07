"""
그래프그리기
모듈(module)설치
터미널 창에서 커맨드를 이용
pip install 모듈 이름
pip list
<matplotlib>
모듈 불러오기
import모듈 이름
"""
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0,1,2], [0,1,2],'r',[0,1,2],[0,1,4],'g')
plt.xlabel("height")
plt.ylabel("weight")
plt.show()
