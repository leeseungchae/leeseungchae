import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
matplotlib.rcParams["font.family"] = "malgun Gothic" #한글 적용
matplotlib.rcParams["font.size"] = 15 #폰트크기
matplotlib.rcParams["axes.unicode_minus"] = False #글자 출력가

df_confirmed = pd.read_csv("C:/Users/Steve-Lee/Desktop/pjt1/data/confirmed.csv",encoding="euc-kr",index_col=0)
df_dose = pd.read_csv("C:/Users/Steve-Lee/Desktop/pjt1/data/dose.csv",encoding="UTF-8",index_col=0)
df_confirmed[["21.06","21.07","21.08","21.09","21.1"]] = df_confirmed[["21.06","21.07","21.08","21.09","21.1"]].apply(pd.to_numeric)
df_dose[["21.06","21.07","21.08","21.09","21.1"]] = df_dose[["21.06","21.07","21.08","21.09","21.1"]].apply(pd.to_numeric)
result = round((df_confirmed/df_dose)*100,2)

matplotlib.rcParams["font.family"] = "malgun Gothic" #한글 적용
matplotlib.rcParams["font.size"] = 15 #폰트크기
matplotlib.rcParams["axes.unicode_minus"] = False #글자 출력가

df_confirmed = df_confirmed.iloc[1:].to_numpy()
df_dose = df_dose.iloc[1:].to_numpy()

# guro = df_confirmed.loc["구로구"].to_numpy()

print(result)
# print(df_confirmed["종로구"])

# x = np.arange(len(jonro))

# years = df_confirmed[["21.06","21.07","21.08","21.09","21.1"]]


# plt.bar(x+0.2, jonro ,width=0.1)
# plt.bar(x+0.4, guro ,width=0.1)


# plt.xticks(x, years)
# plt.legend(df_confirmed.columns[1:6],loc ="lower left")

# plt.show()
