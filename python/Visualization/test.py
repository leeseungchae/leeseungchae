import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

matplotlib.rcParams["font.family"] = "malgun Gothic" #한글 적용
matplotlib.rcParams["font.size"] = 15 #폰트크기
matplotlib.rcParams["axes.unicode_minus"] = False #글자 출력가

df = pd.read_csv("score.csv" )

kor = df["국어"].to_numpy()
eng = df["영어"].to_numpy()
math = df["수학"].to_numpy()
sin = df["과학"].to_numpy()
soc = df["사회"].to_numpy()


x = np.arange(len(kor))

years = df["이름"]


plt.bar(x+0, kor ,width=0.1)
plt.bar(x+0.2, eng ,width=0.1)
plt.bar(x+0.4, math ,width=0.1)
plt.bar(x+0.6, sin ,width=0.1)
plt.bar(x+0.8, soc ,width=0.1)


plt.xticks(x, years)
plt.legend(df.columns[4:9],loc ="lower left")

plt.show()

