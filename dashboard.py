

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import io
from fpdf import FPDF
import base64


st.set_page_config(
    page_title="Therapy Session Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    """Load session data with caching for better performance"""
    try:
        df = pd.read_csv("/Users/rajkumar/reporting dashboard/therapy_sessions.csv")
        df['session_date'] = pd.to_datetime(df['session_date'])
        df['session_datetime'] = pd.to_datetime(df['session_date'].astype(str) + ' ' + df['session_time'])
        df['month_year'] = df['session_date'].dt.to_period('M')
        df['week_year'] = df['session_date'].dt.to_period('W')
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please run data_generator.py first to create sample data.")
        return pd.DataFrame()

def create_pdf_report(filtered_data, therapist_summary, revenue_summary):
   
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    
  
    pdf.cell(200, 10, txt="Therapy Session Report", ln=1, align='C')
    pdf.ln(10)
    
   
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Report Period: {filtered_data['session_date'].min().strftime('%Y-%m-%d')} to {filtered_data['session_date'].max().strftime('%Y-%m-%d')}", ln=1)
    pdf.cell(200, 10, txt=f"Total Sessions: {len(filtered_data)}", ln=1)
    pdf.cell(200, 10, txt=f"Total Revenue: ${filtered_data[filtered_data['status'] == 'Completed']['amount'].sum():,.2f}", ln=1)
    pdf.ln(5)
    
    # Therapist summary
    pdf.cell(200, 10, txt="Sessions by Therapist:", ln=1)
    for _, row in therapist_summary.iterrows():
        pdf.cell(200, 8, txt=f"  {row['therapist_name']}: {row['total_sessions']} sessions", ln=1)
    
    return pdf

def main():
    # Title and description
    st.title("🏥 Therapy Session Reporting Dashboard")
    st.markdown("### Comprehensive analytics for therapy practice management")
    
    # Load data
    df = load_data()
    
    if df.empty:
        st.stop()
    
    # Sidebar filters
    st.sidebar.header("📋 Filters")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['session_date'].min().date(), df['session_date'].max().date()),
        min_value=df['session_date'].min().date(),
        max_value=df['session_date'].max().date()
    )
    
    # Therapist filter
    therapists = st.sidebar.multiselect(
        "Select Therapists",
        options=df['therapist_name'].unique(),
        default=df['therapist_name'].unique()
    )
    
    # Session type filter
    session_types = st.sidebar.multiselect(
        "Select Session Types",
        options=df['session_type'].unique(),
        default=df['session_type'].unique()
    )
    
    # Status filter
    statuses = st.sidebar.multiselect(
        "Select Session Status",
        options=df['status'].unique(),
        default=df['status'].unique()
    )
    
    # Apply filters
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = df[
            (df['session_date'].dt.date >= start_date) &
            (df['session_date'].dt.date <= end_date) &
            (df['therapist_name'].isin(therapists)) &
            (df['session_type'].isin(session_types)) &
            (df['status'].isin(statuses))
        ]
    else:
        filtered_df = df[
            (df['therapist_name'].isin(therapists)) &
            (df['session_type'].isin(session_types)) &
            (df['status'].isin(statuses))
        ]
    
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sessions = len(filtered_df)
        st.metric("Total Sessions", total_sessions)
    
    with col2:
        completed_sessions = len(filtered_df[filtered_df['status'] == 'Completed'])
        completion_rate = (completed_sessions / total_sessions * 100) if total_sessions > 0 else 0
        st.metric("Completion Rate", f"{completion_rate:.1f}%")
    
    with col3:
        total_revenue = filtered_df[filtered_df['status'] == 'Completed']['amount'].sum()
        st.metric("Total Revenue", f"${total_revenue:,.2f}")
    
    with col4:
        no_shows = len(filtered_df[filtered_df['status'] == 'No-Show'])
        no_show_rate = (no_shows / total_sessions * 100) if total_sessions > 0 else 0
        st.metric("No-Show Rate", f"{no_show_rate:.1f}%")
    
    st.divider()
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Sessions by Therapist")
        therapist_summary = filtered_df.groupby('therapist_name').agg({
            'session_id': 'count',
            'amount': 'sum'
        }).rename(columns={'session_id': 'total_sessions', 'amount': 'total_revenue'}).reset_index()
        
        fig_therapist = px.bar(
            therapist_summary, 
            x='therapist_name', 
            y='total_sessions',
            title="Total Sessions per Therapist",
            color='total_sessions',
            color_continuous_scale='Blues'
        )
        fig_therapist.update_xaxes(tickangle=45)
        st.plotly_chart(fig_therapist, use_container_width=True)
    
    with col2:
        st.subheader("❌ Session Status Distribution")
        status_counts = filtered_df['status'].value_counts()
        fig_status = px.pie(
            values=status_counts.values, 
            names=status_counts.index,
            title="Session Status Breakdown",
            color_discrete_sequence=['#28a745', '#ffc107', '#dc3545', '#6c757d']
        )
        st.plotly_chart(fig_status, use_container_width=True)
    
   
    st.subheader("💰 Revenue Over Time")
    
    
    time_period = st.selectbox("Select Time Period", ["Daily", "Weekly", "Monthly"])
    
    if time_period == "Daily":
        revenue_data = filtered_df[filtered_df['status'] == 'Completed'].groupby('session_date')['amount'].sum().reset_index()
        x_col, title = 'session_date', 'Daily Revenue'
    elif time_period == "Weekly":
        revenue_data = filtered_df[filtered_df['status'] == 'Completed'].groupby('week_year')['amount'].sum().reset_index()
        revenue_data['week_year'] = revenue_data['week_year'].astype(str)
        x_col, title = 'week_year', 'Weekly Revenue'
    else:  # Monthly
        revenue_data = filtered_df[filtered_df['status'] == 'Completed'].groupby('month_year')['amount'].sum().reset_index()
        revenue_data['month_year'] = revenue_data['month_year'].astype(str)
        x_col, title = 'month_year', 'Monthly Revenue'
    
    fig_revenue = px.line(
        revenue_data, 
        x=x_col, 
        y='amount',
        title=title,
        markers=True
    )
    fig_revenue.update_layout(xaxis_title="Time Period", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_revenue, use_container_width=True)
    
   
    st.subheader("📊 Detailed Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Session Types Distribution**")
        session_type_data = filtered_df.groupby(['session_type', 'status']).size().unstack(fill_value=0)
        st.dataframe(session_type_data)
    
    with col2:
        st.write("**Revenue by Therapist**")
        revenue_by_therapist = filtered_df[filtered_df['status'] == 'Completed'].groupby('therapist_name')['amount'].sum().sort_values(ascending=False)
        st.dataframe(revenue_by_therapist.to_frame('Revenue ($)'))
    
   
    st.subheader("📤 Export Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # CSV Export
        csv_buffer = io.StringIO()
        filtered_df.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()
        
        st.download_button(
            label="📄 Download CSV",
            data=csv_data,
            file_name=f"therapy_sessions_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    with col2:
        # Excel Export
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            filtered_df.to_excel(writer, sheet_name='Sessions', index=False)
            therapist_summary.to_excel(writer, sheet_name='Therapist Summary', index=False)
        
        st.download_button(
            label="📊 Download Excel",
            data=excel_buffer.getvalue(),
            file_name=f"therapy_sessions_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    with col3:
        # PDF Report
        if st.button("📋 Generate PDF Report"):
            pdf = create_pdf_report(filtered_df, therapist_summary, revenue_data)
            pdf_output = io.BytesIO()
            pdf_string = pdf.output(dest='S')
            pdf_output.write(pdf_string)
            
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_output.getvalue(),
                file_name=f"therapy_report_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime="application/pdf"
            )
    
   
    with st.expander("🔍 View Raw Data"):
        st.dataframe(filtered_df, use_container_width=True)
    
    
    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit | Therapy Session Dashboard v1.0")

if __name__ == "__main__":
    main()