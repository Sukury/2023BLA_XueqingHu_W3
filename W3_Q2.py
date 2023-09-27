import streamlit as st

list1 = [10,20,30,40]
list2 = [100,200,300,400]
index = 0

list2.reverse()

#the first way:
st.write("First method:")
for x,y in zip(list1,list2):
    st.write(x,y)

#the second way:
st.write("Second method:")
for x in list1:
    #for y in list2:
        if index < len(list2):
            st.write(x,list2[index])
            index += 1
