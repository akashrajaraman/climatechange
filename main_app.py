import schedule
import time
from datetime import datetime
import pandas as pd
from company_analyzer import CompanyAnalyzer
from financial_analyzer import FinancialAnalyzer
from ai_recommendation import AIRecommendationEngine
from sebi_compliance import SEBIChecker
import streamlit as st

def main():
    st.title("📈 Real-Time Equity AI Analyst")
    
    # Auto-refresh every 15 minutes
    st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Ticker input
    ticker = st.selectbox(
        "Select stock:",
        ["TCS.NS", "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "BHARTIARTL.NS"],
        index=0
    )
    
    if st.button("Analyze") or True:  # Auto-analyze on load
        with st.spinner("Running real-time analysis..."):
            ai = AIRecommendationEngine()
            rec, score = ai.generate_realtime_recommendation(ticker)
            
            # Show recommendation
            if "BUY" in rec:
                st.success(f"AI Recommendation: {rec} (Score: {score}/100)")
            else:
                st.error(f"AI Recommendation: {rec} (Score: {score}/100)")
            
            # Show metrics
            analysis = ai.get_realtime_analysis(ticker)
            st.subheader("Live Metrics")
            
            cols = st.columns(4)
            cols[0].metric("Price", f"₹{analysis['price']:,.2f}")
            cols[1].metric("P/E", f"{analysis['pe_ratio']:.1f}")
            cols[2].metric("RSI", f"{analysis['rsi']:.1f}")
            cols[3].metric("50-Day SMA", f"₹{analysis['sma_50']:,.2f}")

if __name__ == "__main__":
    # Auto-refresh logic
    while True:
        main()
        time.sleep(900)  # Refresh every 15 minutes
        st.experimental_rerun()

if __name__ == "__main__":
    main()