# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:05:45 2024

@author: admin
"""

import streamlit as st

if st.button('Submit'):
    st.write('Submitted!')

if st.button('Confirm'):
    st.write('Confirmed!')
    
st.write("---")
    
# if st.button('First Button'):
#     st.write('The first button was clicked.')
#     if st.button('Second Button'):
#         # This will never execute!
#         st.write('The second button was clicked')
    # 内层条件的语句不会执行, 因为当点击Second Button时, 网页会刷新, 导致第一个按钮没有执行
    
# 为此, 需要使用session_state

if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False,2:False} # 创建了点击状态的初值
    
def clicked(button):
    st.session_state.clicked[button] = True

st.button("First Button",on_click=clicked,args=[1])

if st.session_state.clicked[1]: # 注意条件, 已经变成了点击状态了, 它是不会随着网页刷新变化的
    st.write('The first button was clicked')
    st.write(f'st.session_state.clicked[1] = {st.session_state.clicked[1]}')
    st.button('Second Button',on_click=clicked,args=[2]) # 按钮被点击后, 初值将改变
    if st.session_state.clicked[2]:
        st.write('The second button was clicked')
        st.write(f'st.session_state.clicked[2] = {st.session_state.clicked[2]}')
        
        
# %%

st.write("---")

if 'favorite_color' not in st.session_state:
    st.session_state.favorite_color = None
def confirm_color():
    st.session_state.favorite_color = st.session_state.color_picker



name = st.text_input('Name:')
if name != '':
    st.write(f'Hi, {name}! Nice to meet you.')
    st.write("What's your favorite color?")
    color = st.color_picker('Color:', key='color_picker',on_change=confirm_color)
    st.write(f"st.session_state.color_picker = {st.session_state.color_picker}")
    
    if st.session_state.favorite_color is None:
        st.button('Confirm Black',on_click=confirm_color)
        st.write(f'st.session_state.favorite_color = {st.session_state.favorite_color}')
    else:
        st.write(f'<span style="color:{color}">Oh, nice color choice! </span>',unsafe_allow_html=True)
    # 这样写, 后面的else的内容不会被执行
    
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_stage(stage):
    st.session_state.stage = stage

st.write('---')
st.write("Welcome! Click to begin")
st.button('Begin', on_click=set_stage,args = [1])

if st.session_state.stage > 0:
    st.write('This is stage 1. Do some things')
    st.button('Next', on_click=set_stage, args=[2])
if st.session_state.stage >1 :
    st.write('This is stage 2. Do some more things')
    st.button('Finish', on_click=set_stage, args=[3])
if st.session_state.stage > 2:
    st.write('This is the end. Thank you!')
    st.button('Reset', on_click=set_stage, args=[0])
    

#%% 
st.write('---')
st.write('# 给表格增加数据')
import pandas as pd
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({'A':[1,2,3],
                                        'B':[4,5,6],
                                        'C':[7,8,9]})
df = st.session_state.df

st.write(df)


cols = st.columns(3)
cols[0].number_input('A',0,100,step=1,key='A')
cols[1].number_input('B',0,100,step=1,key='B')
cols[2].number_input('C',0,100,step=1,key='C')

def add_row():
    # 对于df数据, 添加一行
    row = [st.session_state.A, st.session_state.B, st.session_state.C]
    next_row = len(df)
    df.loc[next_row] = row
    st.session_state.df = df
    
st.button('Add Row',on_click=add_row)



#%% 嵌入自己的css格式

st.write("# 嵌入自己的css格式")
css='''
<style>
    .stButton > button {
        color: red;
    }
    .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    .stButton > button:focus {
        color: purple !important;
        border-color: purple !important;
        box-shadow: purple 0 0 0 .2rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

st.button('Click me!')

section1 = st.container()
section2 = st.container()
section3 = st.container()
section4 = st.container()

# Write to the different containers for your display elements
section1.subheader('Section 1')
section1.button('Button 1')

section2.subheader('Section 2')
section2.button('Button 2')

section3.subheader('Section 3')
section3.button('Button 3')

section4.subheader('Section 4')
section4.button('Button 4')

css2='''
<style>
    section.main > div > div > div > div:nth-of-type(3) .stButton > button {
        color: green;
    }
    section.main > div > div > div > div:nth-of-type(3) .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    section.main > div > div > div > div:nth-of-type(3) .stButton > button:focus {
        color: purple !important;
        border-color: purple !important;
        box-shadow: purple 0 0 0 .2rem;
    }
</style>
'''

st.markdown(css2, unsafe_allow_html=True)


#%% 嵌入javascript 语法

st.write('# 嵌入javascript 语法')
st.write('''<h3>长与宽随着窗口大小变化 <br>The app container is <span id="root-width"></span> x 
<span id="root-height"></span> px.</h3>''',unsafe_allow_html=True)

js = '''
<script>
    var container = window.parent.document.getElementById("root")

    var width = window.parent.document.getElementById("root-width")
    var height = window.parent.document.getElementById("root-height")

    function update_sizing(){
        width.textContent = container.getBoundingClientRect()['width']
        height.textContent = window.parent.innerHeight
    }
    update_sizing()

    window.parent.addEventListener('resize', function(event) {
        update_sizing()
    }, true);
    
</script>
'''

st.components.v1.html(js)


#%% 
st.write("---")
st.write("**file_uploader 并不保存本地的一个文件， 而是将本地文件存储到内存中，通过io读取二进制数据**")


file = st.file_uploader("Choose a file: ", key="loader", type="csv")

if file != None:
    df = pd.read_csv(file)
    st.write(df)


# import io

st.write("---")
file = st.file_uploader("Choose a file:", type=['css','py'])


if file != None:
    bytes_object = file.getvalue()
    string_object = bytes_object.decode("utf-8")
    # st.write(string_object) # 不能直接使用write的格式， 否则代码文件的展示效果不好
    st.code(string_object)


#%%

st.write("---")
st.write("st.session_state.my_key的值会附加到st.slider上，即便我们想改变")

st.code("""
import streamlit as st
st.session_state.my_key=1
st.slider('Test',0,10,value=5)        
        """,language="python")

st.session_state.my_key = 1
st.slider('Test',0,10,key='my_key',value=5)  


st.write("如果组件没有被渲染, 那么与组件有关的数据，包括在st.session_state中的数据都被删除")
st.code("""
switch = st.radio('Choice',options=[1,2])
match switch:
    case 1:
        st.checkbox('1',key='1')
    case 2:
        st.checkbox('2',key='2')
        """,language="python")

switch = st.radio('Choice',options=[1,2])

match switch:
    case 1:
        st.checkbox('1',key='1')
    case 2:
        st.checkbox('2',key='2')














