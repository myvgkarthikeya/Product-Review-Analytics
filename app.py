import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Product Review Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fc;
    color: #1e293b;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #102b50, #071a33);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(255,255,255,0.06);
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 8px;
}

/* Main header */

.main-header {
    background: linear-gradient(120deg, #123b70, #1769aa, #2589d8);
    padding: 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(20,70,130,0.18);
}

.main-header h1 {
    color: white;
    font-size: 32px;
    margin-bottom: 8px;
}

.main-header p {
    color: #dcecff;
    font-size: 15px;
    margin-bottom: 0;
}

/* KPI cards */

.metric-card {
    background: white;
    padding: 23px;
    border-radius: 13px;
    border: 1px solid #e3eaf4;
    border-left: 5px solid #2678c8;
    box-shadow: 0 4px 15px rgba(30,60,100,0.05);
    min-height: 125px;
}

.metric-label {
    color: #64748b;
    font-size: 14px;
    font-weight: 600;
}

.metric-value {
    color: #123b70;
    font-size: 29px;
    font-weight: 750;
    margin-top: 9px;
}

.metric-icon {
    font-size: 23px;
    float: right;
}

/* Section headings */

.section-title {
    color: #123b70;
    font-size: 22px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
}

.subtext {
    color: #64748b;
    font-size: 13px;
}

/* Tables */

div[data-testid="stDataFrame"] {
    background: white;
    border-radius: 10px;
}

/* Footer */

.footer {
    text-align: center;
    color: #8493a8;
    font-size: 12px;
    padding: 25px;
    border-top: 1px solid #dce5f0;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# DATA
# =====================================================

total_reviews = 3572784
total_products = 1244476
average_rating = 4.41

rating_data = pd.DataFrame({
    "Rating": ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"],
    "Reviews": [130760, 133700, 286559, 598837, 2422924]
})

verified_data = pd.DataFrame({
    "Purchase Type": ["Verified", "Not Verified"],
    "Reviews": [2640434, 932350]
})

top_products = pd.DataFrame({
    "Product ASIN": [
        "B06Y1264PX", "0679805273", "1782490671",
        "0920668372", "B00L9B7IKE", "B006LSZECO",
        "0803736800", "1442450703", "1338099132",
        "B00JO8PEN2"
    ],
    "Review Count": [
        4789, 4534, 4198, 3887, 3628,
        2781, 2641, 2369, 2206, 2055
    ],
    "Average Rating": [
        4.46, 4.85, 4.65, 4.66, 4.09,
        3.96, 4.33, 4.75, 3.83, 4.79
    ]
})

cluster_data = pd.DataFrame({
    "Cluster": ["VL-741794", "VL-859165", "VL-639676"],
    "Products": [200835, 226932, 816709],
    "Percentage": [16.14, 18.24, 65.63],
    "Interpretation": [
        "Lower-rated products",
        "Strong 4-star rating tendency",
        "Strong 5-star rating tendency"
    ]
})


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 📊 PR ANALYTICS")
    st.markdown("### Product Intelligence")
    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Rating Analytics",
            "Product Analytics",
            "Mahout Clustering"
        ]
    )

    st.markdown("---")

    st.markdown("### TECHNOLOGY STACK")
    st.markdown("🔹 Hadoop MapReduce")
    st.markdown("🔹 Apache Hive")
    st.markdown("🔹 Apache Mahout")
    st.markdown("🔹 Python & Streamlit")

    st.markdown("---")
    st.caption("Amazon Books Reviews Dataset")
    st.caption("Academic Analytics Project")


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="main-header">
    <h1>Product Review Analytics</h1>
    <p>Large-Scale E-Commerce Review Analysis & Product Intelligence</p>
    <p>Hadoop MapReduce &nbsp; | &nbsp; Apache Hive &nbsp; | &nbsp; Apache Mahout</p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# REUSABLE KPI CARD
# =====================================================

def metric_card(title, value, icon):
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-icon">{icon}</span>
        <div class="metric-label">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# OVERVIEW PAGE
# =====================================================

if page == "Overview":

    st.markdown(
        '<div class="section-title">Platform Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        metric_card("Total Reviews", "3.57 Million", "📝")

    with c2:
        metric_card("Unique Products", "1.24 Million", "📦")

    with c3:
        metric_card("Average Rating", "4.41 / 5", "⭐")

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Customer Rating Distribution</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([1, 1.5])

    with c1:
        st.dataframe(
            rating_data,
            hide_index=True,
            width="stretch"
        )

    with c2:
        fig, ax = plt.subplots(figsize=(8, 4))

        bars = ax.bar(
            rating_data["Rating"],
            rating_data["Reviews"],
            color=["#9fc5e8", "#75a9dc", "#4d8fce",
                   "#2678c8", "#12529a"],
            width=0.6
        )

        ax.set_title("Review Rating Distribution",
                     fontsize=14, fontweight="bold")
        ax.set_ylabel("Number of Reviews")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.2)

        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Product Performance</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        top_products.head(5),
        hide_index=True,
        width="stretch"
    )


# =====================================================
# RATING ANALYTICS PAGE
# =====================================================

elif page == "Rating Analytics":

    st.markdown(
        '<div class="section-title">Customer Rating Analytics</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Explore the distribution of customer ratings "
        "across the Amazon Books review dataset."
    )

    c1, c2 = st.columns(2)

    with c1:
        metric_card("Average Rating", "4.41 / 5", "⭐")

    with c2:
        metric_card("Total Reviews", "3,572,784", "📝")

    st.markdown("---")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        rating_data["Rating"],
        rating_data["Reviews"],
        color=["#9fc5e8", "#75a9dc", "#4d8fce",
               "#2678c8", "#12529a"]
    )

    ax.set_title("Customer Rating Distribution",
                 fontsize=15, fontweight="bold")
    ax.set_xlabel("Customer Rating")
    ax.set_ylabel("Number of Reviews")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.2)

    st.pyplot(fig)
    plt.close(fig)

    st.dataframe(
        rating_data,
        hide_index=True,
        width="stretch"
    )

    st.markdown("---")

    st.markdown("### Verified Purchase Analysis")

    c1, c2 = st.columns(2)

    with c1:
        st.dataframe(
            verified_data,
            hide_index=True,
            width="stretch"
        )

    with c2:
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.pie(
            verified_data["Reviews"],
            labels=verified_data["Purchase Type"],
            autopct="%1.1f%%",
            colors=["#1769aa", "#a9cbea"],
            startangle=90,
            wedgeprops={"edgecolor": "white"}
        )

        ax.set_title("Purchase Verification")
        st.pyplot(fig)
        plt.close(fig)


# =====================================================
# PRODUCT ANALYTICS PAGE
# =====================================================

elif page == "Product Analytics":

    st.markdown(
        '<div class="section-title">Product Performance Analytics</div>',
        unsafe_allow_html=True
    )

    metric_card("Unique Products", "1,244,476", "📦")

    st.markdown("---")

    st.markdown("### Top 10 Most Reviewed Products")

    st.dataframe(
        top_products,
        hide_index=True,
        width="stretch"
    )

    fig, ax = plt.subplots(figsize=(11, 5))

    ax.barh(
        top_products["Product ASIN"],
        top_products["Review Count"],
        color="#2678c8"
    )

    ax.invert_yaxis()
    ax.set_xlabel("Number of Reviews")
    ax.set_title("Top 10 Products by Review Count",
                 fontsize=15, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", alpha=0.2)

    st.pyplot(fig)
    plt.close(fig)


# =====================================================
# MAHOUT CLUSTERING PAGE
# =====================================================

elif page == "Mahout Clustering":

    st.markdown(
        '<div class="section-title">Apache Mahout - K-Means Clustering</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Products were grouped using K-Means clustering "
        "based on seven normalized product-rating features."
    )

    st.markdown("### Clustering Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        metric_card("Total Products", "1,244,476", "📦")

    with c2:
        metric_card("Number of Clusters", "3", "🔵")

    with c3:
        metric_card("Algorithm", "K-Means", "🤖")

    st.markdown("---")

    c1, c2 = st.columns([1, 1.3])

    with c1:
        st.markdown("### Cluster Details")

        st.dataframe(
            cluster_data,
            hide_index=True,
            width="stretch"
        )

    with c2:
        fig, ax = plt.subplots(figsize=(7, 5))

        ax.pie(
            cluster_data["Products"],
            labels=cluster_data["Cluster"],
            autopct="%1.1f%%",
            colors=["#9fc5e8", "#4388ca", "#123b70"],
            startangle=90,
            wedgeprops={"edgecolor": "white", "linewidth": 2}
        )

        ax.set_title("Product Cluster Distribution",
                     fontsize=14, fontweight="bold")

        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")

    st.markdown("### Cluster Interpretation")

    for _, row in cluster_data.iterrows():

        st.markdown(f"""
        <div class="metric-card" style="margin-bottom:15px;">
            <div class="metric-label">{row['Cluster']}</div>
            <div class="metric-value">
                {row['Products']:,} Products
            </div>
            <p style="color:#64748b;">
                {row['Percentage']}% of all products
                <br>
                {row['Interpretation']}
            </p>
        </div>
        """, unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    PRODUCT REVIEW ANALYTICS DASHBOARD<br><br>
    Powered by Hadoop 3.3.6 | Hive 3.1.3 |
    Apache Mahout 0.13.0 | Python & Streamlit
</div>
""", unsafe_allow_html=True)
