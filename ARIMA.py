# 기본
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import xlrd
import openpyxl
from openpyxl import Workbook
# 경고 뜨지 않게 설정
import warnings
warnings.filterwarnings('ignore')

# 그래프 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['font.size'] = 16
plt.rcParams['figure.figsize'] = 20, 10
plt.rcParams['axes.unicode_minus'] = False

# ARIMA (시계열 예측)
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm

# 시간 측정을 위한 시간 모듈
import datetime


# 데이터 수집
import requests
from bs4 import BeautifulSoup
import re
import time
import os
import json

# 한국어 형태소 분석
from konlpy.tag import Okt, Hannanum, Kkma, Mecab, Komoran

# 워드 클라우드를 위한 라이브러리
# from collections import Counter
# import pytagcloud
# from IPython.display import Image

# 저장
import pickle

# 06
# estate=pd.read_excel('/Users/sangeun/Downloads/아파트 실거래가(기간별)2022_8_22_23_2_0.xls')
# restate=estate[['단지[준공년도]','계약일','거래금액','층']]
# rcestate=restate.loc[[2,3,28,29,30,31,40,41,42,43,44,45,46,47,48,122,123,124,125,126,127,128,129,155,156,157,158,159,160,197,198,99,200,201,202,203,204,284,285,286,287]]
# with pd.ExcelWriter("실거래가전처리데이터.xlsx")as writer:
#     rcestate.to_excel(writer,sheet_name="06")

# # 06
# data06=pd.read_excel('/Users/sangeun/Downloads/아파트 실거래가(기간별)_06.xls')
# buf06=data06[['단지[준공년도]','계약일','거래금액','층']]
# final06=buf06.loc[[2,3,28,29,30,31,40,41,42,43,44,45,46,47,48,122,123,124,125,126,127,128,129,155,156,157,158,159,160,197,198,99,200,201,202,203,204,284,285,286,287]]
# with pd.ExcelWriter('ARIMA전처리데이터.xlsx') as writer :
#     final06.to_excel(writer,sheet_name="06")
#
# # 07
# data07=pd.read_excel('/Users/sangeun/Downloads/아파트 실거래가(기간별)_07.xls')
# buf07=data07[['단지[준공년도]','계약일','거래금액','층']]
# # final07=buf07.loc[[2,3,28,29,30,31,40,41,42,43,44,45,46,47,48,122,123,124,125,126,127,128,129,155,156,157,158,159,160,197,198,99,200,201,202,203,204,284,285,286,287]]
# with pd.ExcelWriter('ARIMA전처리데이터임시.xlsx') as writer :
#     buf07.to_excel(writer,sheet_name="07")


# with open('/Users/sangeun/Downloads/서울시 부동산 실거래가 정보.csv',newline='') as csvfile:
#     estate = csv.reader(csvfile,delimiter=' ', quotechar='|')
#     for i in estate:
#         print(', '.join(i))


#isin 사용하기
apt_list=['DMC마포청구아파트\n[1994]','강변힐스테이트\n[2004]','공덕1삼성래미안\n[1999]','공덕2삼성래미안\n[2004]','공덕3삼성래미안\n[2004]','대우미래사랑\n[2005]','도화동현대\n[1996]','마포쌍용황금아파트\n[2000]','마포용강삼성래미안\n[2003]','상암월드컵파크2단지\n[2003]']
data06=pd.read_excel('/Users/sangeun/Downloads/아파트 실거래가(기간별)_06.xls')
buf06=data06[['단지[준공년도]','계약일','거래금액','층']]
final=buf06[buf06['단지[준공년도]'].isin(apt_list)]
with pd.ExcelWriter('Test.xlsx') as writer :
    final.to_excel(writer)
