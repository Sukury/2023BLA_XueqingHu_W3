import streamlit as st

my_list=[10,20,30,40,50,60,70,80,90,100]

num_list = len(my_list)
i=1

#first way
while i in range(1,num_list):
    st.write(my_list[i])
    i += 2

#second way
#for i in range(1,num_list,2):
#    st.write(my_list[i])