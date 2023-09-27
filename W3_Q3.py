import streamlit as st

sampleDict = {
    "class":{
        "student":{
            "name": "Mike", "marks" :{
                "physics" : 70,"history":80
            }
        }
    }
}

historyScore = sampleDict["class"]["student"]["marks"]["history"]
physicsScore = sampleDict["class"]["student"]["marks"]["physics"]
st.write(f"Mike's history mark is {historyScore}")
st.write(f"Mike's physics mark is {physicsScore}")