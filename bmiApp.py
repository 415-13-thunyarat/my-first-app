import streamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ(Title)
st.markdown("# :red[🏋️ คำนวนค่าดัชนีมวลกายBMI]")
st.write("กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

#ส่วนที่2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
weight= = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):",min_value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):,min_value=1.0)
                            
