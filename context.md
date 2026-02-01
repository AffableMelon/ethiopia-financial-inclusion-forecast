Overview
Business Need

You are a Data Scientist at Selam Analytics, a financial technology consulting firm specializing in emerging markets. Selam Analytics has been engaged by a consortium of stakeholders, including development finance institutions, mobile money operators, and the National Bank of Ethiopia, to develop a financial inclusion forecasting system.

Ethiopia is undergoing a rapid digital financial transformation. Telebirr has grown to over 54 million users since launching in 2021. M-Pesa entered the market in 2023 and now has over 10 million users. For the first time, interoperable P2P digital transfers have surpassed ATM cash withdrawals. Yet according to the 2024 Global Findex survey, only 49% of Ethiopian adults have a financial account; just 3 percentage points higher than in 2021.

The consortium wants to understand:

    What drives financial inclusion in Ethiopia?
    How do events like product launches, policy changes, and infrastructure investments affect inclusion outcomes?
    How did financial inclusion rates change in 2025 and how will it look like in the coming years - 2026 and 2027?

Your task is to build a forecasting system that predicts Ethiopia's progress on the two core dimensions of financial inclusion as defined by the World Bank's Global Findex:

    Access — Account Ownership Rate
    Usage — Digital Payment Adoption Rate

The Global Findex Framework

The Global Findex Database is the world's most comprehensive demand-side survey of financial inclusion, conducted every three years since 2011. Your models will forecast these Findex-defined indicators:
Access (Account Ownership)

“The share of adults (age 15+) who report having an account (by themselves or together with someone else) at a bank or another type of financial institution or report personally using a mobile money service in the past 12 months.”

Ethiopia's trajectory:
Year	Account Ownership	Change
2011	14%	—
2014	22%	+8pp
2017	35%	+13pp
2021	46%	+11pp
2024	49%	+3pp
Usage (Digital Payments)

“The share of adults who report using mobile money, a debit or credit card, or a mobile phone to make a payment from an account, or report using the internet to pay bills or to buy something online, in the past 12 months.”

Ethiopia's indicators (2024):

    Mobile money account ownership: 9.45%
    Made or received digital payment: ~35%
    Used account to receive wages: ~15%

Your Deliverables

Build a system that:

    Understands and enriches the provided financial inclusion dataset
    Analyzes patterns and relationships in Ethiopia's inclusion data
    Models how different type of national and regional level reports and events such as new policies, the launch of new products and services, etc. affect inclusion indicators
    Forecasts Access and Usage for 2025-2027
    Presents findings through an interactive dashboard

Data
Starter Dataset

You are provided with a structured dataset containing financial inclusion data for Ethiopia:

This dataset uses a unified schema where all records share the same structure. The record_type field indicates how to interpret each row:
record_type	Count	Description
observation	30	Measured values (Findex surveys, operator reports, infrastructure data)
event	10	Policies, product launches, market entries, milestones
impact_link	14	Modeled relationships between events and indicators
target	3	Official policy goals (e.g., NFIS-II targets)

Key design principle: Events are categorized by type (policy, product_launch, infrastructure, etc.) but are NOT pre-assigned to pillars. Their effects on specific indicators are captured through impact_link records. This keeps the data unbiased.

Supporting files:

    reference_codes — Valid values for all categorical fields
    README.md — Schema documentation

Supplementary Resource: Data Enrichment Guide

The following resource provides guidance on potential data sources and indicators for enrichment:

Additional Data Points Guide

This spreadsheet contains four sheets to help you identify useful data for your forecasting model:
Sheet	Description
A. Alternative Baselines	Additional data sources (IMF FAS, G20 indicators, GSMA, ITU, NBE, financial institution reports)
B. Direct Correlation	Indicators directly tied to inclusion: active accounts, agent density, POS terminals, QR merchants, transaction volumes, ATM density, bank branches
C. Indirect Correlation	Enabler/proxy variables: smartphone penetration, data affordability, gender gap, agent networks, urbanization, mobile internet, 4G coverage, literacy, electricity access, digital ID
D. Market Nuances	Ethiopia-specific context you should understand: P2P dominance (used for commerce, not just transfers), mobile money-only users are rare (~0.5%), bank accounts are easily accessible, very low credit penetration

Use this resource to:

    Identify additional observations to add in Task 1
    Understand which indicators matter most for forecasting
    Contextualize Ethiopia's unique market dynamics in your analysis

Tasks
Project Structure

ethiopia-fi-forecast/

├── .github/workflows/

│   └── unittests.yml

├── data/

│   ├── raw/                      # Starter dataset

│   │   ├── ethiopia_fi_unified_data.csv

│   │   └── reference_codes.csv

│   └── processed/                # Analysis-ready data

├── notebooks/

│   └── README.md

├── src/

│   ├── __init__.py

├── dashboard/

│   └── app.py

├── tests/

│   └── __init__.py

├── models/

├── reports/

│   └── figures/

├── requirements.txt

├── README.md

└── .gitignore
Task 1: Data Exploration and Enrichment

Objective: Understand the starter dataset and enrich it with additional data you find useful for the forecasting task.

Instructions:

    Understand the Schema
        Load and explore ethiopia_fi_unified_data.csv
        Examine the structure: all records share the same columns
        Sheet 1 (data): Contains observations, events, and targets
            observation: Actual measured values from surveys, reports, operators
            event: Policies, product launches, market entries, milestones
            target: Official policy goals
        Sheet 2 (impact_links): Contains modeled relationships between events and indicators
        Review reference_codes.csv for valid field values
        Understand the challenges associated to setting pillar values to events (e.g., policy, product_launch) 
        Understand how impact_link records connect events to indicators via parent_id
    Explore the Data
        Count records by record_type, pillar, source_type, and confidence
        Identify the temporal range of observations
        List all unique indicators (indicator_code) and their coverage
        Understand which events are cataloged and their dates
        Review the existing impact_links and what relationships they capture
    Enrich the Dataset - Add new data that you believe will be useful for forecasting Access and Usage. Consider: 
        Additional observations: Are there other data points about Ethiopia's financial inclusion that could help? (e.g., disaggregations by gender or region from Findex microdata, additional years of infrastructure data, other relevant metrics)
        Additional events: Are there policies, launches, or milestones that aren't captured but could affect inclusion? (e.g., regulatory changes, new partnerships, infrastructure investments)
        Additional impact_links: Can you identify other relationships between events and indicators that should be modeled?
    Follow the Schema
        For new observations: fill pillar, indicator, indicator_code, value_numeric, observation_date, source_name, source_url, confidence
        For new events: fill category (e.g., policy, product_launch, infrastructure) but leave pillar empty
        For new impact_links: fill parent_id (linking to the event), pillar, related_indicator, impact_direction, impact_magnitude, lag_months, evidence_basis
    Document Your Additions
        For each new record, document:

    source_url: Where you found the data
    original_text: The exact quote or figure from the source
    confidence: Your assessment (high/medium/low)
    collected_by: Your name
    collection_date: Date of collection
    notes: Why you think this data is useful

Minimum Essential To Do:

    Merge necessary branches into main using a Pull Request (PR)
    Create branch "task-1"
    Commit work with descriptive commit messages
    Load all three datasets successfully
    Updated dataset with your additions and corrections
    data_enrichment_log.md documenting changes

Task 2: Exploratory Data Analysis

Objective: Analyze the data to understand patterns and factors influencing financial inclusion in Ethiopia.

Instructions:

    Dataset Overview
        Summarize the dataset by record_type, pillar, and source_type
        Create a temporal coverage visualization: which years have data for which indicators?
        Assess data quality: distribution of confidence levels
        Identify gaps: which indicators have sparse coverage?
    Access Analysis
        Plot Ethiopia's account ownership trajectory (2011-2024)
        Calculate and visualize growth rates between survey years
        If disaggregated data available:
            Analyze the gender gap (male vs. female ownership)
            Compare urban vs. rural ownership
        Investigate the 2021-2024 slowdown:
            Account ownership grew only +3pp despite massive mobile money expansion
            What factors might explain this deceleration?
    Usage (Digital Payments) Analysis
        Analyze mobile money account penetration trend (2014-2024)
        Examine digital payment adoption patterns
        If data supports, explore:
            The "registered vs. active" gap (registered accounts vs. survey-reported usage)
            Payment use cases (P2P, merchant, bill pay, wages)
    Infrastructure and Enablers
        Analyze available infrastructure data (4G coverage, mobile penetration, ATM density)
        Examine relationships between infrastructure and inclusion outcomes
        Identify potential leading indicators that might predict Findex outcomes
    Event Timeline and Visual Analysis
        Create a timeline visualization showing all cataloged events
        Overlay events on indicator trend charts
        Visually identify apparent relationships:
            Did account ownership accelerate after Telebirr launch (May 2021)?
            Did mobile money accounts grow after M-Pesa entry (Aug 2023)?
            What happened around Safaricom's market entry (Aug 2022)?
    Correlation Analysis
        Examine correlations between different indicators
        Which factors appear most strongly associated with Access?
        Which factors appear most strongly associated with Usage?
        What insights emerge from the existing impact_link records?
    Document Key Insights Address questions such as:
        What factors appear to drive financial inclusion in Ethiopia?
        Why might account ownership have stagnated (only +3pp) despite 65M+ mobile money accounts being opened?
        What is the gender gap and how has it evolved?
        What data gaps most limit your analysis?
        What hypotheses emerge for testing in the impact modeling phase?

Note: Review Sheet D (Market Nuances) in the Additional Data Points Guide to understand Ethiopia-specific dynamics that may affect your interpretation.

Minimum Essential To Do:

    Merge branches from task-1 into main using PR
    Create branch "task-2"
    Commit work with descriptive commit messages
    EDA notebook with visualizations
    Summary of at least 5 key insights with supporting evidence
    Data quality assessment documenting limitations

Task 3: Event Impact Modeling

Objective: Model how events (policies, product launches, infrastructure investments) affect financial inclusion indicators.

Instructions:

    Understand the Impact Data
        Load the impact_links sheet from your enriched dataset
        Join with events from the data sheet using parent_id to get event details
        Create a summary showing: which events affect which indicators, and by how much.
    Build the Event-Indicator Matrix: Using the impact_link data:
        Each link specifies an event, the indicator it affects, the direction, magnitude, and lag
        Your task is to translate these relationships into a model that can predict how indicators change when events occur
        Consider:
            How do you represent an event's effect over time?
            Do effects happen immediately or build gradually?
            How do you combine effects from multiple events?
    Review Comparable Country Evidence: For events where Ethiopian pre/post data is insufficient, use documented impacts from similar contexts:
    Create the Association Matrix: Build a matrix that summarizes:
        Rows: Events
        Columns: Key indicators (ACC_OWNERSHIP, ACC_MM_ACCOUNT, USG_DIGITAL_PAYMENT, etc.)
        Values: The estimated effect of each event on each indicator
        This matrix captures "which events affect which indicators and by how much."
    Test Your Model Against Historical Data: Where possible, check if your impact model makes sense:
        Telebirr launched in May 2021; mobile money accounts went from 4.7% (2021) to 9.45% (2024)
        Does your model's estimated impact align with what actually happened?
        If not, what might explain the difference?
    Refine Your Estimates
        Based on what you observe in the data, refine your impact estimates
        Document your reasoning for any adjustments
        Note which estimates you're confident about vs. uncertain about
    Document Your Methodology
        Explain how you modeled event impacts
        What assumptions did you make?
        What are the limitations of your approach?

Minimum Essential To Do:

    Merge branches from task-2 into main using PR
    Create branch "task-3"
    Commit work with descriptive commit messages
    Impact modeling notebook
    Event-indicator association matrix (table or heatmap)
    Documentation of:
    Methodology and functional forms chosen
    Sources for all impact estimates
    Validation results comparing predicted vs. observed
    Key assumptions and uncertainties

Task 4: Forecasting Access and Usage

Objective: Forecast Account Ownership (Access) and Digital Payment Usage for 2025-2027.

Instructions:

    Define Targets
        Account Ownership Rate (Access): % of adults with account at financial institution or mobile money
        Digital Payment Usage: % of adults who made or received digital payment
    Select Approach Given sparse data (5 Findex points over 13 years), consider:
        Trend regression (linear or log)
        Event-augmented model (trend + event effects)
        Scenario analysis
    Generate Forecasts
        Baseline: Trend continuation
        With events: Incorporate expected developments
        Scenarios: Optimistic, base, pessimistic
    Quantify Uncertainty
        Confidence intervals
        Scenario ranges
        Explicit acknowledgment of limitations
    Interpret Results
        What does your model predict?
        What events have largest potential impact?
        What are the key uncertainties?

Minimum Essential To Do:

    Merge branches from task-3 into main using PR
    Create branch "task-4"
    Commit work with descriptive commit messages
    Forecasting notebook
    Forecast table with confidence intervals
    Scenario visualization
    Written interpretation

Task 5: Dashboard Development

Objective: Create an interactive dashboard that enables stakeholders to explore the data, understand event impacts, and view forecasts.

Instructions:

    Dashboard Setup
        Use Streamlit (recommended) or Dash
        Create dashboard/app.py
        Include clear instructions in README for running locally
    Dashboard Sections
        Overview Page:
            Key metrics summary cards (current values, trends)
            P2P/ATM Crossover Ratio indicator
            Growth rate highlights
        Trends Page:
            Interactive time series plots
            Date range selector
            Channel comparison view
        Forecasts Page:
            Forecast visualizations with confidence intervals
            Model selection option
            Key projected milestones
    Technical Requirements
        At least 4 interactive visualizations
        Clear labels and explanations
        Data download functionality
    Inclusion Projections Page:
        Financial inclusion rate projections
        Progress toward 60% target visualization
        Scenario selector (optimistic/base/pessimistic)
        Answers to consortium's key questions

Minimum Essential To Do:

    Merge branches from task-3 into main using PR
    Create branch "task-4"
    Commit work with descriptive commit messages
    Create working Streamlit application
    Include at least 4 interactive visualizations
    Display key metrics and forecasts
    Provide clear run instructions in README