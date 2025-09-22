import streamlit as st
import requests
import re
import markdown2
import streamlit.components.v1 as components

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="NHAI Allocation Assistant", layout="wide")
st.title("🏗️ NHAI Allocation Assistant")
st.markdown("""
Minimal inputs, maximum insight - generate a comprehensive NHAI resource allocation report instantly.
""")

# ---------------------------
# Session state
# ---------------------------
if "allocation_report" not in st.session_state:
    st.session_state.allocation_report = None

# ---------------------------
# Utility functions
# ---------------------------
def fix_bullets(md_text):
    """Convert AI bullets (• or -) to proper Markdown list items."""
    md_text = re.sub(r'•\s*', '- ', md_text)
    md_text = re.sub(r'(\S)- ', r'\1\n- ', md_text)
    return md_text

def bold_in_tables(md_text):
    """
    Convert **text** inside table rows to HTML <b>text</b>.
    """
    lines = md_text.split("\n")
    new_lines = []

    for line in lines:
        if line.strip().startswith("|") and line.strip().endswith("|"):
            # Replace **text** with <b>text</b>
            line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
        new_lines.append(line)
    return "\n".join(new_lines)

def markdown_table_to_html(md_text):
    """
    Convert Markdown-style tables to proper HTML tables.
    """
    lines = md_text.split("\n")
    html_lines = []
    table_block = []

    for line in lines + [""]:
        if line.strip().startswith("|") and line.strip().endswith("|"):
            table_block.append(line.strip())
        else:
            if table_block:
                headers = [h.strip() for h in table_block[0].split("|")[1:-1]]
                html_table = "<table><thead><tr>"
                for h in headers:
                    html_table += f"<th>{h}</th>"
                html_table += "</tr></thead><tbody>"
                for row in table_block[2:]:
                    cells = [c.strip() for c in row.split("|")[1:-1]]
                    html_table += "<tr>" + "".join([f"<td>{c}</td>" for c in cells]) + "</tr>"
                html_table += "</tbody></table>"
                html_lines.append(html_table)
                table_block = []
            html_lines.append(line)
    return "\n".join(html_lines)

# ---------------------------
# Sidebar: Collapsible Inputs
# ---------------------------
with st.sidebar.expander("Project Inputs", expanded=True):
    project_name = st.text_input("Project Name", "Delhi-Mumbai Expressway")
    project_id = st.text_input("Project ID", "P001")
    location = st.text_input("Location", "Delhi to Mumbai via Ahemdabad")
    project_type = st.selectbox("Project Type", ["Highway", "Bridge", "Tunnel"])
    start_date = st.date_input("Start Date")
    duration_days = st.number_input("Duration (days)", min_value=1, value=200)

    if st.button("Generate Allocation Report"):
        request_data = {
            "project": {
                "project_name": project_name,
                "project_id": project_id,
                "location": location,
                "project_type": project_type,
                "start_date": str(start_date),
                "duration_days": duration_days
            }
        }

        with st.spinner("⏳ Generating allocation report..."):
            try:
                BACKEND_URL = "https://nhai-resource-allocation.onrender.com"

                response = requests.post(f"{BACKEND_URL}/allocate_resources", json=request_data)

                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        st.success("✅ Resources Allocated Successfully")
                        st.session_state.allocation_report = data["report"]
                    else:
                        st.error(f"❌ API Error: {data.get('error')}")
                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"❌ Request Failed: {e}")

# ---------------------------
# Display full-width report
# ---------------------------
if st.session_state.get("allocation_report"):
    # Prepare the report
    report_md = st.session_state.allocation_report
    report_md = fix_bullets(report_md)
    report_md = bold_in_tables(report_md)
    report_md = markdown_table_to_html(report_md)
    report_html = markdown2.markdown(report_md)

    # Build HTML with professional styling
    html_content = f"""
    <style>
        body {{
            margin:0;
            padding:0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height:1.6;
            color:#333;
        }}

        h1 {{
            font-size:26px;
            margin:12px 0 8px;
            color:#1F4E79;
            border-bottom:2px solid #E0E0E0;
            padding-bottom:4px;
        }}

        h2 {{
            font-size:22px;
            margin:10px 0 6px;
            color:#2F5597;
        }}

        h3 {{
            font-size:20px;
            margin:8px 0 4px;
            color:#3F62B1;
        }}

        p {{
            margin:6px 0;
        }}

        ul, ol {{
            margin:6px 0 10px 24px;
            padding-left:0;
        }}

        li {{
            margin-bottom:6px;
            /* Remove custom bullets to avoid double bullets */
        }}

        table {{
            width:100%;
            border-collapse: collapse;
            margin:10px 0;
            border-radius:6px;
            overflow:hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }}

        th {{
            background-color:#f0f4f8;
            color:#1F4E79;
            font-weight:600;
            padding:10px 8px;
            text-align:left;
        }}

        td {{
            padding:8px 6px;
            border-bottom:1px solid #e0e0e0;
        }}

        tr:nth-child(even) td {{
            background-color:#fafafa;
        }}

        b {{
            color:#1F4E79;
        }}
    </style>

    {report_html}
    """

    # Render in a scrollable HTML block
    components.html(html_content, height=1000, scrolling=True)

