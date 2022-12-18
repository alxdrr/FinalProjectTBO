import streamlit as st

def pattern(results):
    if "XO" in results:
        st.write("### Pola Kalimat :blue[S P O]")
    elif "XKet" in results:     
        st.write("### Pola Kalimat :blue[S P Ket]")
    elif "XPel" in results:
        st.write("### Pola Kalimat :blue[S P Pel]")  
    elif "XX" in results:    
        st.write("### Pola Kalimat :blue[S P Pel Ket]")
    elif "XY" in results:    
        st.write("### Pola Kalimat :blue[S P O Ket]") 
    elif "XZ" in results:    
        st.write("### Pola Kalimat :blue[S P O Pel]")              
    elif "SP" in results:    
        st.write("### Pola Kalimat :blue[S P]")          
    elif "QKet" in results:    
        st.write("### Pola Kalimat :blue[S P O Pel Ket]")               