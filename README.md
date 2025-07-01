# 🏥 Therapy Session Reporting Dashboard

A comprehensive, interactive dashboard for managing and analyzing therapy session data, built with Python and Streamlit.

## ✨ Features

### 📊 Core Visualizations
- **Total Sessions per Therapist** - Bar chart showing session distribution
- **No-shows & Cancellations** - Pie chart of session status breakdown  
- **Revenue Over Time** - Interactive line chart with daily/weekly/monthly views

### 🔧 Advanced Features
- **Interactive Filtering** - Filter by date range, therapist, session type, and status
- **Export Options** - Download data as CSV, Excel, or PDF reports
- **Real-time Metrics** - Key performance indicators displayed prominently
- **Responsive Design** - Works on desktop and mobile devices

### 📈 Analytics Included
- Session completion rates
- No-show tracking and rates
- Revenue analysis and trends
- Therapist performance metrics
- Session type distribution

## 🚀 Quick Start

### 1. Install Dependencies & Generate Sample Data
```bash
python setup.py
```

### 2. Run the Dashboard
```bash
streamlit run dashboard.py
```

The dashboard will automatically open in your web browser at `http://localhost:8501`

## 📁 Project Structure

```
reporting dashboard/
├── dashboard.py          # Main Streamlit dashboard application
├── data_generator.py     # Generates realistic sample data
├── setup.py             # One-click setup script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── therapy_sessions.csv # Generated sample data (CSV)
└── therapy_sessions.json # Generated sample data (JSON)
```

## 🎯 Usage Guide

### Dashboard Navigation
1. **Sidebar Filters** - Use to filter data by date, therapist, session type, or status
2. **Key Metrics** - Top row shows total sessions, completion rate, revenue, and no-show rate
3. **Visualizations** - Interactive charts for different data perspectives
4. **Export Section** - Download filtered data in various formats

### Filtering Options
- **Date Range** - Select start and end dates
- **Therapists** - Multi-select from available therapists
- **Session Types** - Choose from Individual, Couples, Family, Group, or Initial Consultation
- **Status** - Filter by Completed, Cancelled, No-Show, or Rescheduled

### Export Formats
- **CSV** - Raw data for spreadsheet analysis
- **Excel** - Formatted workbook with multiple sheets
- **PDF** - Professional report with summary statistics

## 📊 Sample Data Schema

The generated sample data includes:

| Field | Type | Description |
|-------|------|-------------|
| session_id | String | Unique session identifier |
| therapist_id | String | Therapist identifier (T001, T002, etc.) |
| therapist_name | String | Full therapist name |
| client_id | String | Client identifier |
| session_date | Date | Date of session (YYYY-MM-DD) |
| session_time | Time | Time of session (HH:MM) |
| session_type | String | Type of therapy session |
| duration_minutes | Integer | Session duration |
| status | String | Session status |
| amount | Float | Session fee/revenue |
| notes | String | Session notes |

## 🔧 Customization

### Adding Your Own Data
Replace the sample data by:

1. **CSV Format** - Replace `therapy_sessions.csv` with your data file
2. **Database Connection** - Modify the `load_data()` function in `dashboard.py`
3. **API Integration** - Add API calls to fetch live data

### Modifying Visualizations
- Charts are built with Plotly - easily customizable
- Add new charts by creating additional Plotly figures
- Modify colors, themes, and layouts in the chart configuration

### Adding New Features
- **Authentication** - Add user login functionality
- **Real-time Updates** - Connect to live data sources  
- **Advanced Analytics** - Machine learning predictions
- **Mobile App** - Convert to mobile-first design

## 🛠️ Technical Details

### Dependencies
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **FPDF2** - PDF report generation
- **OpenPyXL** - Excel file handling

### Performance Features
- **Data Caching** - Streamlit caching for faster load times
- **Efficient Filtering** - Optimized pandas operations
- **Responsive Design** - Mobile-friendly layout

## 🔒 Security & Privacy

- All data processing happens locally
- No data is sent to external servers
- Generated sample data is completely fictional
- Follow HIPAA compliance guidelines when using with real patient data

## 🆘 Troubleshooting

### Common Issues

**Dashboard won't start:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Generate fresh sample data  
python data_generator.py
```

**Charts not displaying:**
- Check your internet connection (Plotly needs CDN access)
- Clear browser cache
- Try a different browser

**Export not working:**
- Ensure all dependencies are installed
- Check file permissions in the project directory

### Getting Help
- Check the Streamlit documentation for deployment options
- Review Plotly docs for chart customization
- Use GitHub issues for bug reports and feature requests

## 🚀 Deployment Options

### Local Development
```bash
streamlit run dashboard.py
```

### Cloud Deployment
- **Streamlit Cloud** - Free hosting for public repos
- **Heroku** - Easy deployment with Procfile
- **AWS/GCP/Azure** - Enterprise deployment options

### Docker Deployment
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "dashboard.py"]
```

## 📈 Future Enhancements

- [ ] Real-time data synchronization
- [ ] Mobile application version
- [ ] Advanced predictive analytics
- [ ] Integration with popular EHR systems
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] Email report scheduling
- [ ] Role-based access control

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for healthcare professionals**

*Need help or have questions? Feel free to reach out!*# 🏥 Therapy Session Reporting Dashboard

A comprehensive, interactive dashboard for managing and analyzing therapy session data, built with Python and Streamlit.

## ✨ Features

### 📊 Core Visualizations
- **Total Sessions per Therapist** - Bar chart showing session distribution
- **No-shows & Cancellations** - Pie chart of session status breakdown  
- **Revenue Over Time** - Interactive line chart with daily/weekly/monthly views

### 🔧 Advanced Features
- **Interactive Filtering** - Filter by date range, therapist, session type, and status
- **Export Options** - Download data as CSV, Excel, or PDF reports
- **Real-time Metrics** - Key performance indicators displayed prominently
- **Responsive Design** - Works on desktop and mobile devices

### 📈 Analytics Included
- Session completion rates
- No-show tracking and rates
- Revenue analysis and trends
- Therapist performance metrics
- Session type distribution

## 🚀 Quick Start

### 1. Install Dependencies & Generate Sample Data
```bash
python setup.py
```

### 2. Run the Dashboard
```bash
streamlit run dashboard.py
```

The dashboard will automatically open in your web browser at `http://localhost:8501`

## 📁 Project Structure

```
reporting dashboard/
├── dashboard.py          # Main Streamlit dashboard application
├── data_generator.py     # Generates realistic sample data
├── setup.py             # One-click setup script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── therapy_sessions.csv # Generated sample data (CSV)
└── therapy_sessions.json # Generated sample data (JSON)
```

## 🎯 Usage Guide

### Dashboard Navigation
1. **Sidebar Filters** - Use to filter data by date, therapist, session type, or status
2. **Key Metrics** - Top row shows total sessions, completion rate, revenue, and no-show rate
3. **Visualizations** - Interactive charts for different data perspectives
4. **Export Section** - Download filtered data in various formats

### Filtering Options
- **Date Range** - Select start and end dates
- **Therapists** - Multi-select from available therapists
- **Session Types** - Choose from Individual, Couples, Family, Group, or Initial Consultation
- **Status** - Filter by Completed, Cancelled, No-Show, or Rescheduled

### Export Formats
- **CSV** - Raw data for spreadsheet analysis
- **Excel** - Formatted workbook with multiple sheets
- **PDF** - Professional report with summary statistics

## 📊 Sample Data Schema

The generated sample data includes:

| Field | Type | Description |
|-------|------|-------------|
| session_id | String | Unique session identifier |
| therapist_id | String | Therapist identifier (T001, T002, etc.) |
| therapist_name | String | Full therapist name |
| client_id | String | Client identifier |
| session_date | Date | Date of session (YYYY-MM-DD) |
| session_time | Time | Time of session (HH:MM) |
| session_type | String | Type of therapy session |
| duration_minutes | Integer | Session duration |
| status | String | Session status |
| amount | Float | Session fee/revenue |
| notes | String | Session notes |

## 🔧 Customization

### Adding Your Own Data
Replace the sample data by:

1. **CSV Format** - Replace `therapy_sessions.csv` with your data file
2. **Database Connection** - Modify the `load_data()` function in `dashboard.py`
3. **API Integration** - Add API calls to fetch live data

### Modifying Visualizations
- Charts are built with Plotly - easily customizable
- Add new charts by creating additional Plotly figures
- Modify colors, themes, and layouts in the chart configuration

### Adding New Features
- **Authentication** - Add user login functionality
- **Real-time Updates** - Connect to live data sources  
- **Advanced Analytics** - Machine learning predictions
- **Mobile App** - Convert to mobile-first design

## 🛠️ Technical Details

### Dependencies
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **FPDF2** - PDF report generation
- **OpenPyXL** - Excel file handling

### Performance Features
- **Data Caching** - Streamlit caching for faster load times
- **Efficient Filtering** - Optimized pandas operations
- **Responsive Design** - Mobile-friendly layout

## 🔒 Security & Privacy

- All data processing happens locally
- No data is sent to external servers
- Generated sample data is completely fictional
- Follow HIPAA compliance guidelines when using with real patient data

## 🆘 Troubleshooting

### Common Issues

**Dashboard won't start:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Generate fresh sample data  
python data_generator.py
```

**Charts not displaying:**
- Check your internet connection (Plotly needs CDN access)
- Clear browser cache
- Try a different browser

**Export not working:**
- Ensure all dependencies are installed
- Check file permissions in the project directory

### Getting Help
- Check the Streamlit documentation for deployment options
- Review Plotly docs for chart customization
- Use GitHub issues for bug reports and feature requests

## 🚀 Deployment Options

### Local Development
```bash
streamlit run dashboard.py
```

### Cloud Deployment
- **Streamlit Cloud** - Free hosting for public repos
- **Heroku** - Easy deployment with Procfile
- **AWS/GCP/Azure** - Enterprise deployment options

### Docker Deployment
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "dashboard.py"]
```

## 📈 Future Enhancements

- [ ] Real-time data synchronization
- [ ] Mobile application version
- [ ] Advanced predictive analytics
- [ ] Integration with popular EHR systems
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] Email report scheduling
- [ ] Role-based access control

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for healthcare professionals**

*Need help or have questions? Feel free to reach out!*