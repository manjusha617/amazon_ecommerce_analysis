import streamlit as st
import pandas as pd
from utils import set_background

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Amazon E-Commerce Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ======================================
# BACKGROUND
# ======================================

set_background("images/background.jpg")

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

/* Main Title */
h1{
    color:#FF9900 !important;
    text-align:center;
    font-weight:800;
    font-size:3rem !important;
    text-shadow:0px 0px 15px rgba(255,153,0,0.8);
}

/* Headers */
h2,h3{
    color:#FFB84D !important;
    font-weight:bold !important;
}

/* KPI Cards */
div[data-testid="metric-container"]{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,153,0,0.3);
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(255,153,0,0.2);
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-5px);
    transition:0.3s;
}

/* Dataframe */
[data-testid="stDataFrame"]{
    border:2px solid #FF9900;
    border-radius:15px;
}

/* Success */
.stSuccess{
    border-left:6px solid #FF9900;
    border-radius:12px;
}

/* Info */
.stInfo{
    border-left:6px solid #FFB84D;
    border-radius:12px;
}

/* Footer */
.footer{
    text-align:center;
    padding:15px;
    border-top:1px solid #FF9900;
    margin-top:20px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# LOAD DATA
# ======================================

@st.cache_data
def load_data():
    return pd.read_csv("amazon_cleaned.csv")

df = load_data()

# ======================================
# SIDEBAR
# ======================================

st.sidebar.markdown("""
# 🛒 Amazon Dashboard

### E-Commerce Product Analytics
""")

st.sidebar.markdown("---")

st.sidebar.success("""
📊 Dataset Overview

📦 Product Analysis

💰 Price Analysis

⭐ Rating Analysis

🏷️ Discount Analysis

📂 Category Analysis

📈 Statistical Analysis

💡 Business Insights

👨‍💻 About Developer
""")

# ======================================
# TITLE
# ======================================

st.markdown("""
<h1>
🛒 Amazon E-Commerce Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

st.info("""
Analyze Amazon product pricing, discounts, ratings, category performance,
customer engagement, and business opportunities using data analytics and statistical analysis.
""")

st.markdown("""
### Amazon Product Performance & Pricing Analytics

This project explores Amazon product listings to understand:

✔ Product Performance

✔ Pricing Strategies

✔ Customer Ratings

✔ Discount Effectiveness

✔ Category Performance

✔ Statistical Relationships

✔ Business Recommendations
""")

st.divider()

# ======================================
# KPI CALCULATIONS
# ======================================

total_products = len(df)

total_categories = df["main_category"].nunique()

avg_price = df["actual_price"].mean()

avg_discount_price = df["discounted_price"].mean()

avg_rating = df["rating"].mean()

avg_discount = df["discount_percentage"].mean()

avg_savings = df["savings"].mean()

# ======================================
# KPI ROW 1
# ======================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Total Products",
        f"{total_products:,}"
    )

with col2:
    st.metric(
        "📂 Main Categories",
        total_categories
    )

with col3:
    st.metric(
        "⭐ Average Rating",
        round(avg_rating,2)
    )

with col4:
    st.metric(
        "🏷️ Average Discount",
        f"{avg_discount:.1f}%"
    )

st.divider()

# ======================================
# KPI ROW 2
# ======================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Avg Actual Price",
        f"₹{avg_price:,.0f}"
    )

with col2:
    st.metric(
        "🛒 Avg Selling Price",
        f"₹{avg_discount_price:,.0f}"
    )

with col3:
    st.metric(
        "💵 Avg Savings",
        f"₹{avg_savings:,.0f}"
    )

with col4:
    st.metric(
        "👤 Unique Users",
        df["user_id"].nunique()
    )

st.divider()

# ======================================
# KPI ROW 3
# ======================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "⭐ Highest Rating",
        round(df["rating"].max(),1)
    )

with col2:
    st.metric(
        "🔥 Highest Discount",
        f"{df['discount_percentage'].max():.0f}%"
    )

with col3:
    st.metric(
        "💸 Highest Savings",
        f"₹{df['savings'].max():,.0f}"
    )

with col4:
    st.metric(
        "💎 Highest Product Price",
        f"₹{df['actual_price'].max():,.0f}"
    )

st.divider()

# ======================================
# DATASET PREVIEW
# ======================================

st.subheader("📊 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True,
    height=350
)

st.divider()

# ======================================
# PROJECT HIGHLIGHTS
# ======================================

st.subheader("📌 Project Highlights")

st.success("""
✅ Dataset Overview

✅ Product Analysis

✅ Price Analysis

✅ Rating Analysis

✅ Discount Analysis

✅ Category Analysis

✅ Correlation Analysis

✅ Statistical Testing

✅ Regression Analysis

✅ Business Insights

✅ Interactive Streamlit Dashboard
""")

st.divider()

# ======================================
# BUSINESS QUESTIONS
# ======================================

st.subheader("📋 Business Questions")

st.info("""
• Which categories dominate Amazon product listings?

• Which products receive the highest customer ratings?

• How do prices vary across categories?

• Do discounts influence customer ratings?

• Which categories provide the highest customer value?

• What factors impact product performance?

• What relationships exist between price, savings, and ratings?

• Which categories offer the strongest business opportunities?
""")

st.divider()

# ======================================
# DASHBOARD PAGES
# ======================================

st.subheader("🧭 Dashboard Pages")

st.info("""
📊 Dataset Overview

📦 Product Analysis

💰 Price Analysis

⭐ Rating Analysis

🏷️ Discount Analysis

📂 Category Analysis

📈 Statistical Analysis

💡 Business Insights & Recommendations

👨‍💻 About Developer
""")

st.divider()

# ======================================
# PROJECT OBJECTIVE
# ======================================

st.subheader("🎯 Project Objective")

st.write("""
This project aims to analyze Amazon product data to identify patterns in pricing,
discount strategies, customer ratings, and category performance.

The insights generated help businesses improve pricing decisions,
optimize promotional strategies, enhance customer satisfaction,
and maximize sales opportunities.
""")

st.divider()

# ======================================
# FOOTER
# ======================================

st.markdown("""
<div class="footer">
Developed by <b>Vempa Bhargav Naidu</b> |
Amazon E-Commerce Analytics Dashboard
</div>
""", unsafe_allow_html=True)