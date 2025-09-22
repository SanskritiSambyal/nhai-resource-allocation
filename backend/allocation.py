from utils import call_claude

def allocate_resources_claude(request_data: dict) -> dict:
    """
    Generates a technical NHAI allocation report using Claude.
    Minimal input is required; Claude fills in the rest.
    """
    project_info = request_data.get("project", {})
    project_name = project_info.get("project_name", "Unknown Project")
    project_id = project_info.get("project_id", "PXXX")
    location = project_info.get("location", "Unknown")
    project_type = project_info.get("project_type", "Highway")
    start_date = project_info.get("start_date", "2025-01-01")
    duration_days = project_info.get("duration_days", 100)

    prompt = f"""
You are an expert NHAI project planner. Generate a **technical resource allocation report** in **structured markdown**.

Use:
- Bullet points for descriptive text
- Tables for numeric data such as manpower, machinery, and materials
- Include:
  - Executive summary
  - Site assessment (terrain, soil, climate)
  - Estimated project cost and budget
  - Manpower (technical, skilled, unskilled) in a table
  - Machinery plan in a table
  - Material requirements in a table
  - Risks and potential delays (weather, terrain, logistics)
  - Mitigation strategies
  - Expected completion date considering weather and terrain
- Avoid overly large paragraphs; break into bullet points and short sections
- **Do not include any footer or signature lines**, such as "Report Prepared By", "Date", or "Next Review".

Minimal project info:
Project Name: {project_name}
Project ID: {project_id}
Location: {location}
Project Type: {project_type}
Start Date: {start_date}
Duration: {duration_days} days

"""
    try:
        report_text = call_claude(prompt, max_tokens=4000)
        return {"success": True, "report": report_text}
    except Exception as e:
        return {"success": False, "error": str(e)}
