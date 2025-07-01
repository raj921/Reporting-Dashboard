#!/bin/bash

# Therapy Session Dashboard Startup Script
echo "🏥 Starting Therapy Session Dashboard..."

# Navigate to the project directory
cd "/Users/rajkumar/reporting dashboard"

# Activate virtual environment
source dashboard_env/bin/activate

# Run the dashboard
echo "Dashboard will open in your browser at http://localhost:8501"
streamlit run dashboard.py