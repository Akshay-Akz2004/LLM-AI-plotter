import streamlit as st
import plotly.express as px
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Custom Graphs", page_icon=":bar_chart:", layout="wide")

st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding-top: 1rem;
    }
    header {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(":bar_chart: Custom Graphs from CSV")

fl = st.file_uploader(":file_folder: Upload a CSV file", type=["csv"])
if fl is not None:
    try:
        df = pd.read_csv(fl, encoding="ISO-8859-1")
        st.write("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading the file: {e}")
else:
    st.info("Please upload a CSV file to proceed.")

if fl is not None:
    st.sidebar.header("Select your axes for the graph:")
    
    numeric_columns = df.select_dtypes(['float', 'int']).columns.tolist()
    string_columns = df.select_dtypes(['object']).columns.tolist()

    x_axis = st.sidebar.selectbox("X-Axis", options=numeric_columns + string_columns)
    y_axis = st.sidebar.selectbox("Y-Axis", options=numeric_columns + string_columns)

    if x_axis and y_axis:
        st.subheader("Dashboard of All Possible Graphs")
        
        # Bar Chart
        st.write("### Bar Chart")
        fig_bar = px.bar(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Line Chart
        st.write("### Line Chart")
        fig_line = px.line(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig_line, use_container_width=True)
        
        # Scatter Plot
        st.write("### Scatter Plot")
        fig_scatter = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Pie Chart
        if df[x_axis].nunique() < 20: 
            st.write("### Pie Chart")
            fig_pie = px.pie(df, names=x_axis, values=y_axis)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        # Histogram
        st.write("### Histogram")
        fig_hist = px.histogram(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig_hist, use_container_width=True)
        
        # Box Plot
        st.write("### Box Plot")
        fig_box = px.box(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig_box, use_container_width=True)
        
        # Area Chart
        st.write("### Area Chart")
        fig_area = px.area(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig_area, use_container_width=True)

        # Treemap
        st.write("### Treemap")
        fig_treemap = px.treemap(df, path=[x_axis], values=y_axis)
        st.plotly_chart(fig_treemap, use_container_width=True)
        
        st.write("### Additional Graphs")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Histogram")
            fig_hist = px.histogram(df, x=x_axis)
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            st.write("Box Plot")
            fig_box = px.box(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig_box, use_container_width=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.write("Scatter Plot")
            fig_scatter = px.scatter(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col4:
            st.write("Area Chart")
            fig_area = px.area(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig_area, use_container_width=True)

else:
    st.info("Please upload a CSV file to proceed.")
