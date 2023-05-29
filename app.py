import streamlit as st
import pandas as pd

from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml


def main():
    st.title('안녕하세요4')
    st.title('안녕하세요3')
    st.title('안녕하세요')
    st.title('자동차 가격 예측 앱')
    menu = ['Home','EDA','ML']

    choice =  st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        run_app_home()
    elif choice == menu[1]:
        run_app_eda()
    else :
        run_app_ml()

## 이게 무슨 뜻인지

if __name__=='__main__':
    main()

