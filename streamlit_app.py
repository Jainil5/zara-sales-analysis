import streamlit as st
from sales_analysis import df, sales_by_gender, sales_by_category, product_categories, highest_income, top_sellers, least_sellers, top_revenue,highest_income_item,highest_sold_item,total_items,total_revenue,total_sales, least_sold_item

st.set_page_config(page_title="Sales Data Dashboard", layout="wide")
st.markdown('<p style="color:red; font-weight:bold;font-size:50px;">ZARA COLTHING SALES ANALYSIS DASHBOARD FOR 2024</p>', unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Increase font size of tab labels */
        div[role="tablist"] > div {
            font-size: 20px; /* Adjust the font size */
        }
    </style>
""", unsafe_allow_html=True)
tab1,tab2 = st.tabs(["### Key Metrics","### Visualizations"],)

with tab1:
    col1, col2, col3 = st.columns(3, gap="medium")
    with col2:
        st.markdown('<p style="color:red; font-weight:bold;font-size:50px;text-align:center;">KEY METRICS</p>', unsafe_allow_html=True) 
    st.container(height=20,border=False)
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    with col1:
        st.success(f"### TOTAL REVENUE GENERATED : \n ### ${total_revenue:,.2f}")
    with col2:
        st.success(f"### ITEMS SOLD THIS YEAR: \n ### {total_sales:,} items")
    with col3:
        st.success(f"### TOP SELLING CATEGORY : \n ### {highest_sold_item.upper()}")
    with col4:
        st.success(f"### LEAST SELLING CATEGORY : \n ### {least_sold_item.upper()}")
    
    st.warning("")
    col1, col2,col3 = st.columns(3, gap="medium")
    with col1:
        st.info("### TOP REVENUES")
        st.dataframe(top_revenue, use_container_width=True)
    with col2:
        st.info("### TOP SELLERS")
        st.dataframe(top_sellers, use_container_width=True)
    with col3:
        st.info("### LEAST SELLERS")
        st.dataframe(least_sellers, use_container_width=True)
    
        
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.info("### REVENUE BY CATEGORY")
        st.dataframe(highest_income, use_container_width=True)    
    with col2:
        st.info("### SALES BY CATEGORY")
        st.dataframe(sales_by_category, use_container_width=True)
    with col3:
        st.info("### SALES BY GENDER")
        st.dataframe(sales_by_gender, use_container_width=True)
    
    
    
    
with tab2:
    col1, col2, col3 = st.columns(3, gap="medium")
    with col2:
        st.markdown('<p style="color:red; font-weight:bold;font-size:50px;text-align:center;">VISUALIZATIONS</p>', unsafe_allow_html=True) 
    

    c1, c2 = st.columns(2,gap="medium")
    with c1:
        st.markdown('<p style="color:blue; font-weight:bold;font-size:20px;text-align:center;">SALES BY GENDER</p>', unsafe_allow_html=True) 
        st.bar_chart(sales_by_gender,y_label="ITEMS SOLD",x_label="GENDER",width=400, height=400)
    with c2:
        st.markdown('<p style="color:blue; font-weight:bold;font-size:20px;text-align:center;">SALES BY CATEGORY</p>', unsafe_allow_html=True) 
        st.bar_chart(sales_by_category,y_label="ITEMS SOLD",x_label="CATEGORY",width=400, height=400)
    
    c1, c2 = st.columns(2,gap="medium")
    with c1:
        st.markdown('<p style="color:blue; font-weight:bold;font-size:20px;text-align:center;">VARIETY OF PRODUCTS IN EACH CATEGORY</p>', unsafe_allow_html=True) 
        st.bar_chart(product_categories,x_label="CATEGORIES",y_label="NO. OF VARIETY IN CATEGORY",width=400, height=400)
    with c2:
        st.markdown('<p style="color:blue; font-weight:bold;font-size:20px;text-align:center;">REVENUE GENERATED BY EACH CATEGORY</p>', unsafe_allow_html=True) 
        st.bar_chart(highest_income,y_label="REVENUE",x_label="Category",width=400, height=400)
    
    
