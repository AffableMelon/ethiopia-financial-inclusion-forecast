import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page config
st.set_page_config(page_title="Ethiopia Financial Inclusion Forecast", layout="wide", page_icon="🇪🇹")

# -----------------------------------------------------------------------------
# Data Loading
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    # Helper to get absolute path relative to this script
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data', 'processed')
    
    unified_path = os.path.join(data_dir, 'ethiopia_fi_unified_data.csv')
    forecast_path = os.path.join(data_dir, 'forecast_results_2025_2027.csv')
    impacts_path = os.path.join(data_dir, 'modeled_event_impacts.csv')
    
    try:
        df = pd.read_csv(unified_path)
        df['observation_date'] = pd.to_datetime(df['observation_date'])
        df['year'] = df['observation_date'].dt.year
    except FileNotFoundError:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    try:
        fc_df = pd.read_csv(forecast_path)
    except FileNotFoundError:
        fc_df = pd.DataFrame()

    try:
        imp_df = pd.read_csv(impacts_path)
        if 'observation_date' in imp_df.columns:
            imp_df['observation_date'] = pd.to_datetime(imp_df['observation_date'])
            imp_df['year'] = imp_df['observation_date'].dt.year
    except FileNotFoundError:
        imp_df = pd.DataFrame()
        
    return df, fc_df, imp_df

df_main, df_forecast, df_impacts = load_data()

# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
st.sidebar.title("Selam Analytics")
st.sidebar.info("Ethiopia Financial Inclusion Forecasting System")

page = st.sidebar.radio("Navigation", [
    "Overview", 
    "Trends Analysis", 
    "Forecasts (2025-2027)", 
    "Event Impacts",
    "Inclusion Projections"
])

# -----------------------------------------------------------------------------
# 1. Overview Page
# -----------------------------------------------------------------------------
if page == "Overview":
    st.title("🇪🇹 Financial Inclusion Overview")
    st.markdown("### Key Metrics Snapshot (2024)")
    
    if df_main.empty:
        st.error("Data not loaded. Please ensure data processing steps are complete.")
    else:
        # Extract latest values
        latest_year = 2024
        
        # Access
        access_row = df_main[(df_main['indicator_code'] == 'ACC_OWNERSHIP') & (df_main['year'] == latest_year)]
        access_val = access_row['value_numeric'].values[0] if not access_row.empty else "N/A"
        
        # Usage (Digital Payment)
        usage_row = df_main[(df_main['indicator_code'] == 'USG_DIGITAL_PAYMENT') & (df_main['year'] == latest_year)]
        usage_val = usage_row['value_numeric'].values[0] if not usage_row.empty else "N/A"
        
        # Mobile Money
        mm_row = df_main[(df_main['indicator_code'] == 'ACC_MM_ACCOUNT') & (df_main['year'] == latest_year)]
        if mm_row.empty: 
            # Fallback to nearest date if 2024 exact match missing in yearly filter
            mm_row = df_main[df_main['indicator_code'] == 'ACC_MM_ACCOUNT'].sort_values('observation_date').tail(1)
        mm_val = mm_row['value_numeric'].values[0] if not mm_row.empty else "N/A"

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Account Ownership (Access)", f"{access_val}%", delta="3pp vs 2021")
        with col2:
            st.metric("Digital Payment Usage", f"{usage_val}%", delta="High Growth")
        with col3:
            st.metric("Mobile Money Accounts", f"{mm_val}%", delta="Doubled since '21")
            
        st.markdown("---")
        st.subheader("P2P vs ATM Crossover")
        st.write("In a historic shift, interoperable P2P digital transfers have surpassed ATM cash withdrawals in value/volume, signaling a transition to digital-first habits.")
        
        # Create simple P2P vs ATM chart if data exists (simulated for overview if specific rows missing)
        # Using specific indicator codes if available
        p2p_data = df_main[df_main['indicator_code'] == 'USG_P2P_COUNT']
        if not p2p_data.empty:
            fig_p2p = px.bar(p2p_data, x='year', y='value_numeric', title="P2P Transaction Growth")
            st.plotly_chart(fig_p2p)

# -----------------------------------------------------------------------------
# 2. Trends Page
# -----------------------------------------------------------------------------
elif page == "Trends Analysis":
    st.title("Historical Trends (2011-2024)")
    
    if df_main.empty:
        st.error("No data available.")
    else:
        indicators = df_main[df_main['record_type']=='observation']['indicator_code'].unique()
        selected_ind = st.multiselect("Select Indicators to Compare", indicators, default=['ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT'])
        
        if selected_ind:
            trend_data = df_main[df_main['indicator_code'].isin(selected_ind)].sort_values('observation_date')
            fig = px.line(trend_data, x='observation_date', y='value_numeric', color='indicator_code',
                          markers=True, title="Indicator Trends Over Time",
                          labels={'value_numeric': 'Value (%)', 'observation_date': 'Date', 'indicator_code': 'Indicator'})
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Key Observations")
        st.markdown("- **2021-2024 Slowdown:** Account ownership grew only +3pp despite massive mobile money expansion.")
        st.markdown("- **Registered vs Active Gap:** While 65M+ accounts are registered, Findex usage data shows lower active engagement.")

# -----------------------------------------------------------------------------
# 3. Forecasts Page
# -----------------------------------------------------------------------------
elif page == "Forecasts (2025-2027)":
    st.title("🔮 Forecasts: Access & Usage")
    
    if df_forecast.empty:
        st.warning("Forecast data not generated yet (Task 4).")
    else:
        metric = st.selectbox("Select Metric to Forecast", df_forecast['Indicator'].unique())
        
        # Filter data
        fc_subset = df_forecast[df_forecast['Indicator'] == metric]
        
        # Get historical for context
        hist_code = 'ACC_OWNERSHIP' if 'Access' in metric else 'USG_DIGITAL_PAYMENT'
        hist_data = df_main[(df_main['indicator_code'] == hist_code) & (df_main['record_type']=='observation')][['year', 'value_numeric']]
        hist_data['Scenario'] = 'Historical'
        hist_data.rename(columns={'value_numeric': 'Value', 'year': 'Year'}, inplace=True)
        
        # Combine
        plot_df = pd.concat([
            hist_data,
            fc_subset[['Year', 'Value', 'Scenario']]
        ])
        
        fig = px.line(plot_df, x='Year', y='Value', color='Scenario',
                      markers=True, title=f"{metric}: 2025-2027 Projections",
                      color_discrete_map={'Historical': 'black', 'Base Case': 'blue', 'Optimistic': 'green', 'Pessimistic': 'red'})
        
        # Add event markers if available
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Scenario Definitions")
        st.markdown("""
        - **Base Case:** Trend continuation + confirmed policy impacts.
        - **Optimistic:** Accelerated policy adoption (e.g., successful digital ID rollout).
        - **Pessimistic:** Implementation delays or macro headwinds.
        """)
        
        st.subheader("Forecast Data")
        st.dataframe(fc_subset.pivot(index='Year', columns='Scenario', values='Value'))

# -----------------------------------------------------------------------------
# 4. Event Impacts
# -----------------------------------------------------------------------------
elif page == "Event Impacts":
    st.title("💥 Event Impact Modeling")
    
    if df_impacts.empty:
        st.warning("Impact modeling data not found.")
    else:
        st.markdown("This section quantifies how specific events (Policies, Launches) affect inclusion metrics.")
        
        # Display the Matrix
        matrix_view = df_impacts[['category', 'observation_date', 'original_text', 'related_indicator', 'estimated_impact']]
        matrix_view['Impact %'] = matrix_view['estimated_impact'] * 100
        
        st.dataframe(matrix_view.sort_values('observation_date', ascending=False))
        
        # Visualization of cumulative impacts
        st.subheader("Projected Impact Magnitude")
        fig = px.bar(matrix_view, x='related_indicator', y='Impact %', color='category',
                     hover_data=['original_text'],
                     title="Estimated Percentage Point Impact by Indicator & Event Type")
        st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# 5. Inclusion Projections
# -----------------------------------------------------------------------------
elif page == "Inclusion Projections":
    st.title("🎯 Strategy & Targets")
    
    target_val = 60
    st.markdown(f"### Progress Toward National Target ({target_val}%)")
    
    # Get base case 2027 forecast
    if not df_forecast.empty:
        base_2027 = df_forecast[
            (df_forecast['Indicator'].str.contains('Access')) & 
            (df_forecast['Year'] == 2027) & 
            (df_forecast['Scenario'] == 'Base Case')
        ]['Value'].values[0]
        
        opt_2027 = df_forecast[
            (df_forecast['Indicator'].str.contains('Access')) & 
            (df_forecast['Year'] == 2027) & 
            (df_forecast['Scenario'] == 'Optimistic')
        ]['Value'].values[0]
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("2027 Base Forecast", f"{base_2027:.1f}%")
        with col2:
            st.metric("Gap to Target", f"{target_val - base_2027:.1f}pp")
            
        fig = go.Figure()
        
        fig.add_trace(go.Indicator(
            mode = "gauge+number",
            value = base_2027,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "2027 Access Rate (Base Case)"},
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 49], 'color': "lightgray"},
                    {'range': [49, opt_2027], 'color': "lightblue"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': target_val
                }
            }
        ))
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### Strategic Recommendations")
        st.markdown("To close the gap to 60%, the consortium should focus on:")
        st.markdown("1. **Digital ID Integration:** Accelerate biometric verification to lower onboarding friction.")
        st.markdown("2. **Merchant Acceptance:** Expand P2P usage into P2B (Person to Business) for daily commerce.")
        st.markdown("3. **Rural Agent Networks:** Incentivize expansion beyond Addis to reach the underserved.")
