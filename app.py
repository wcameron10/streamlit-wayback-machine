# app.py
import streamlit as st
from waybackpy import WaybackMachineCDXServerAPI

def get_snapshots(url, from_date, to_date):
    user_agent = "my new app's user agent"
    cdx_api = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=from_date, end_timestamp=to_date)
    website_snapshots = cdx_api.snapshots()
    return website_snapshots
    #for item in cdx_api.snapshots():
        #print(item.archive_url)

def main():
    st.title("The Wayback Machine Snapshot Viewer")
    st.write("Enter a URL to view its historical snapshots.")

    # Get user input
    url = st.text_input("Enter a URL:", "https://www.example.com")
    from_date = st.date_input("Select From Date:")
    to_date = st.date_input("Select To Date:")
    
    if st.button("View Snapshots"):
        snapshots = get_snapshots(url, from_date, to_date)

        if not snapshots:
            st.info("No snapshots found for the given URL.")
        else:
            st.write("Snapshots Timeline:")
            for snapshot in snapshots:
                st.write(f"- {snapshot.timestamp} - {snapshot.archive_url} - {snapshot.original}")

if __name__ == "__main__":
    main()

