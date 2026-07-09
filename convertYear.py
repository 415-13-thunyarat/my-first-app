import  streamlit as st
st.title("แอปพลิเคชั่นแปปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.text_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ce_year=bh_yaer-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
