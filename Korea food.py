import streamlit as st

st.title("🍜 ร้านอาหารเกาหลี")

st.subheader("เมนูอาหาร")

tteokbokki = st.number_input("ต็อกบ๊กกี 150 บ. จำนวน:", min_value=0, step=1)
bibimbap = st.number_input("บิบิมบัม 150 บ. จำนวน:", min_value=0, step=1)
kimchi = st.number_input("กิมจิ 50 บ. จำนวน:", min_value=0, step=1)
naengmyeon = st.number_input("แนงมยอน 80 บ. จำนวน:", min_value=0, step=1)
kimbap = st.number_input("คิมบับ 60 บ. จำนวน:", min_value=0, step=1)

# คำนวณราคารวม
total = (tteokbokki * 150) + (bibimbap * 150) + (kimchi * 50) + (naengmyeon * 80) + (kimbap * 60)

# ส่วนลด
if total > 500:
    discount = total * 0.10
elif total >= 300:
    discount = total * 0.05
else:
    discount = 0

price_after_discount = total - discount

# VAT 7%
vat = price_after_discount * 0.07
net_price = price_after_discount + vat

st.header(f"💰 ราคาก่อนส่วนลด: {total:.2f} บาท")
st.header(f"🏷️ ส่วนลด: {discount:.2f} บาท")
st.header(f"💵 VAT 7%: {vat:.2f} บาท")
st.header(f"🧾 ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.write("ร้านอาหารเกาหลี")import streamlit as st

st.title("🍜 ร้านอาหารเกาหลี")

st.subheader("เมนูอาหาร")

tteokbokki = st.number_input("ต็อกบ๊กกี 150 บ. จำนวน:", min_value=0, step=1)
bibimbap = st.number_input("บิบิมบัม 150 บ. จำนวน:", min_value=0, step=1)
kimchi = st.number_input("กิมจิ 50 บ. จำนวน:", min_value=0, step=1)
naengmyeon = st.number_input("แนงมยอน 80 บ. จำนวน:", min_value=0, step=1)
kimbap = st.number_input("คิมบับ 60 บ. จำนวน:", min_value=0, step=1)

# คำนวณราคารวม
total = (tteokbokki * 150) + (bibimbap * 150) + (kimchi * 50) + (naengmyeon * 80) + (kimbap * 60)

# ส่วนลด
if total > 500:
    discount = total * 0.10
elif total >= 300:
    discount = total * 0.05
else:
    discount = 0

price_after_discount = total - discount

# VAT 7%
vat = price_after_discount * 0.07
net_price = price_after_discount + vat

st.header(f"💰 ราคาก่อนส่วนลด: {total:.2f} บาท")
st.header(f"🏷️ ส่วนลด: {discount:.2f} บาท")
st.header(f"💵 VAT 7%: {vat:.2f} บาท")
st.header(f"🧾 ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.write("ร้านอาหารเกาหลี")
