import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

from sklearn.linear_model import LinearRegression

#Importing the Salary datafile
data=pd.read_csv("Salary_Data.csv")
#Using Linear regression model to fit the data
x=np.array(data["YearsExperience"]).reshape(-1,1)
lr=LinearRegression()
lr.fit(x,np.array(data["Salary"]))

#Salary Predictor Home page
st.title("Salary predictor")
nav=st.sidebar.radio("Navigation",["Home","Prediction","Contribution"])
if nav=="Home":
    
    st.write("Home page")
    st.image("Salary_man.jpg")
    if st.checkbox("Show Table"):
         st.table(data)

    #Slider for Years of  Experience 
    val = st.slider("Filter data using years",0,20)
    data = data.loc[data["YearsExperience"]>= val]
    
    #FOr interactive or Non interactive graph
    graph=st.selectbox("What kind of Graph ?",["Non interactive","Interactive"])
    if graph=="Non interactive":
         plt.scatter(data["YearsExperience"],data["Salary"])
         plt.xlabel("Years of experience")
         plt.ylabel("Salary")
         st.pyplot()
    if graph=="Interactive":
         df=pd.DataFrame(data)
         chart=alt.Chart(df).mark_circle().encode(
              x="YearsExperience",y="Salary",
         ).interactive()
         st.altair_chart(chart)

#For prediction of Salary using Years of Experience
if nav == "Prediction":
    st.write("Prediction")
    val=st.number_input("Enter your experience",0.00,20.00)
    val=np.array(val).reshape(-1,1)
    pred=lr.predict(val)[0]
    if st.button("Predict"):
          st.write("Expected salry",pred)


#FOr the contribution to the data(if a person has worked for some years(YearsExperinece) with their salary)
if nav=="Contribution":
        st.write("Contribution")
        ex=st.number_input("Enter your experience",0.00,20.00)
        sal=st.number_input("Enter your salary",0.00,1000000.00,step=1000.0)
        if st.button("Submit"):
             to_add={"YearsExperience":[ex],"Salary":[sal]}
             to_add=pd.DataFrame(to_add)
             to_add.to_csv("Salary_Data.csv",mode='a',header=False,index=False)
             st.success("Submitted")
