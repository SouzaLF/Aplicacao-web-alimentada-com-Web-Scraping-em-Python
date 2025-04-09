# agricultural-monitoring-dashboard/app.py

import streamlit as st
import json
import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import time
import datetime
import locale

# Page Configuration
st.set_page_config(
    page_title="Agricultural Monitoring Dashboard",
    page_icon="🌱",
    layout="wide"
)

# Constants
LOGO_PATH = "assets/logo.png"
API_CONFIG = {
    "url": "YOUR_API_URL",
    "credentials": {
        "cliente": "YOUR_CLIENT",
        "password": "YOUR_PASSWORD"
    }
}

# Helper Functions
def load_image(image_path):
    """Load and return an image"""
    return Image.open(image_path)

def initialize_session():
    """Initialize session state variables"""
    if 'data' not in st.session_state:
        st.session_state.data = None

# Data Loading Functions
def load_operations_data():
    """Load operations data from JSON files"""
    operations = {
        '105': 'ADUBAÇÃO/PREPARO DE SOLO',
        '106': 'APLIC. DE ADUBO A LANÇO',
        # ... rest of your operations data
    }
    return pd.DataFrame(list(operations.items()), columns=['CD_OPERACAO', 'Nome_Operação'])

def fetch_api_data(start_date, end_date):
    """Fetch data from the agricultural API"""
    try:
        # API authentication
        auth_response = requests.post(
            API_CONFIG['url'],
            data=json.dumps(API_CONFIG['credentials']),
            headers={'content-type': 'application/json'}
        )
        
        if auth_response.status_code != 200:
            st.error("Failed to authenticate with API")
            return None
            
        token = auth_response.json()['token']
        headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
        
        # Main data request
        payload = {
            "id": 22,
            "page": 0,
            "parameters": {
                "dataini": start_date,
                "datafim": end_date,
                # ... other parameters
            }
        }
        
        response = requests.post(
            'API_ENDPOINT',
            data=json.dumps(payload),
            headers=headers
        )
        
        return response.json()
        
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return None

# Visualization Functions
def create_horizontal_bar_chart(data, labels, title, color):
    """Create a horizontal bar chart"""
    fig = plt.figure(figsize=(10, 6))
    plt.style.use("ggplot")
    
    # Filter out zero values
    filtered_data = [x for x in data if x > 0]
    filtered_labels = [label for label, val in zip(labels, data) if val > 0]
    
    plt.barh(filtered_labels, filtered_data, alpha=0.8, color=color)
    plt.title(title, fontsize=14)
    plt.xlabel('Value', fontsize=12)
    plt.ylabel('Category', fontsize=12)
    
    for i, v in enumerate(filtered_data):
        plt.text(v + 0.1, i, f"{v:.2f}", color='black', va='center')
    
    plt.tight_layout()
    return fig

def create_pie_chart(values, labels, colors, title):
    """Create a pie chart"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%',
           startangle=90, wedgeprops={'alpha':0.8})
    ax.set_title(title, fontsize=14)
    ax.axis('equal')
    return fig

# Main App
def main():
    # Initialize session
    initialize_session()
    
    # Load static data
    operations_df = load_operations_data()
    
    # Header Section
    st.markdown("<h1 style='text-align: left; color: #033102;'>Indicadores Operacionais</h1>", 
                unsafe_allow_html=True)
    
    # Current date/time
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    st.text(time.strftime('%d %B %Y - %H:%M:%Sh', time.localtime()))
    
    # Logo
    logo = load_image(LOGO_PATH)
    st.image(logo, caption='Monitoramento de máquinas', use_column_width=True)
    
    # Date Selection
    today = datetime.date.today()
    date_range = st.date_input(
        'Informe o período para análise (Ano/mês/dia)',
        [today, today]
    )
    
    # Validate date range
    if len(date_range) == 2:
        start_date, end_date = date_range
        if start_date > today or end_date > today:
            st.error('Erro: Dados para datas futuras ainda serão gerados')
        elif (end_date - start_date).days > 7:
            st.error('Erro: Intervalo máximo permitido é de 7 dias')
        else:
            # Format dates for API
            formatted_start = start_date.strftime("%d/%m/%Y") + " 00:00:00"
            formatted_end = end_date.strftime("%d/%m/%Y") + " 23:59:59"
            
            st.success(f'Período selecionado: {formatted_start} a {formatted_end}')
            
            # Fetch data
            if st.button('Carregar Dados'):
                with st.spinner('Buscando dados...'):
                    api_data = fetch_api_data(formatted_start, formatted_end)
                    if api_data:
                        st.session_state.data = process_api_data(api_data, operations_df)
                        st.success('Dados carregados com sucesso!')
    
    # Display data if loaded
    if st.session_state.data is not None:
        display_dashboard(st.session_state.data)

if __name__ == "__main__":
    main()
