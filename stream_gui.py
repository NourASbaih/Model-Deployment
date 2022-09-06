#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st


# In[4]:


def main():
    st.title("Hi")
    st.subheader("Hello")
    
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu" , menu)
    
    if choice == "Home":
        st.subheader("Home")
    else: 
        st.subheader("About")
        
if __name__ == '__main__':
    main()


# In[ ]:




