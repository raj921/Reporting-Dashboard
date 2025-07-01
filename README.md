# 🏥 Therapy Session Dashboard

A clean, interactive dashboard for analyzing therapy session data built with Python and Streamlit.

## 🚀 Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate sample data**
   ```bash
   python data_generator.py
   ```

3. **Run the dashboard**
   ```bash
   streamlit run dashboard.py
   ```

4. **Open in browser**
   - Visit: `http://localhost:8501`

## ✨ Key Features

- **Interactive Visualizations**
  - Session distribution by therapist
  - No-show and cancellation rates
  - Revenue trends over time

- **Powerful Filtering**
  - Filter by date range, therapist, session type, and status
  - Real-time updates

- **Export Options**
  - Download data as CSV, Excel, or PDF
  - Custom report generation

## 📁 Project Structure

```
reporting-dashboard/
├── dashboard.py         # Main dashboard application
├── data_generator.py    # Sample data generator
├── requirements.txt     # Python dependencies
├── setup.py            # One-click setup
└── README.md           # This file
```

## 🔧 Customization

### Using Your Own Data
1. Replace `therapy_sessions.csv` with your data
2. Or modify `load_data()` in `dashboard.py` for database connections

### Development
- Built with Streamlit and Plotly
- Easily extendable and customizable

## 📄 License
MIT License - feel free to use and modify!

