import streamlit as st
import pandas as pd

def main():
    st.title("Add Data")
    df = pd.read_csv("data.csv")
    st.header("The data")
    st.write(df)
    
    st.sidebar.header("Enter The Data")
    options_form = st.sidebar.form("options_form")
    user_name = options_form.text_input("Name")
    user_age = options_form.text_input("Age")
    add_data = options_form.form_submit_button(label = 'Add')
    
    if add_data:
        new_data = pd.DataFrame({"name": [user_name], "age": [int(user_age)]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv("data.csv", index = False)

    remove_form = st.sidebar.form("remove_form")
    Index = remove_form.text_input("Index")
    remove_data = remove_form.form_submit_button(label = 'Remove')
    if remove_data:
        df = df.drop(index=int(Index))
        df.to_csv("data.csv", index = False)
    
if __name__ == "__main__":
    main()
