import streamlit as st




st.title("足し算")

a = st.text_input("足し算 1つ目の数字を入力してください")
b = st.text_input("足し算 2つ目の数字を入力してください")

c = 0

if a.strip() == '' or b.strip() == '':
    print("エラー: 空文字列を整数に変換することはできません。")
else:
    c = float(a) + float(b)

st.text(c)

st.title("引き算")

aa = st.text_input("引き算 1つ目の数字を入力してください")
bb = st.text_input("引き算 2つ目の数字を入力してください")

cc = 0

if aa.strip() == '' or bb.strip() == '':
    print("エラー: 空文字列を整数に変換することはできません。")
else:
    cc = float(aa) - float(bb)

st.text(cc)

st.title("掛け算")

aaa = st.text_input("掛け算 1つ目の数字を入力してください")
bbb = st.text_input("掛け算 2つ目の数字を入力してください")

ccc= 0

if aaa.strip() == '' or bbb.strip() == '':
    print("エラー: 空文字列を整数に変換することはできません。")
else:
    ccc = float(aaa) * float(bbb)

st.text(ccc)

st.title("割り算")

aaaa = st.text_input("割り算 1つ目の数字を入力してください")
bbbb = st.text_input("割り算 2つ目の数字を入力してください")

cccc= 0

if aaaa.strip() == '' or bbbb.strip() == '':
    print("エラー: 空文字列を整数に変換することはできません。")
else:
    cccc = float(aaaa) / float(bbbb)

st.text(cccc)



st.image("https://us.123rf.com/450wm/sabuhinovruzov/sabuhinovruzov1706/sabuhinovruzov170600040/79339504-電卓のベクター-アイコン%E3%80%82黒と白のイラストをカウントします%E3%80%82概要線形アイコン%E3%80%82eps.jpg")
# st.image("https://www.ibs.it/images/3665361023319_0_536_0_75.jpg")
