import streamlit as st
import pandas as pd
import numpy as np



def main():
    st.title('서울, 수도권, 경기도')
    
    # 서울의 위도와 경도
    seoul_coordinates = (37.5665, 126.9780)
    
    # 위도와 경도를 담은 데이터프레임 생성
    data = pd.DataFrame({'LATITUDE': [seoul_coordinates[0]], 'LONGITUDE': [seoul_coordinates[1]]})
    
    # st.map()을 사용하여 지도를 출력
    st.map(data, zoom=9)

if __name__ == '__main__':
    main()

