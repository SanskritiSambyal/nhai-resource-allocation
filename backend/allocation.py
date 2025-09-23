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

Style Guidelines:
- Use bullet points with **1 full sentence each** (not just short phrases).
- Where necessary, use **short paragraphs** (3–4 sentences) to explain important context, policies, or sustainability practices.
- After every table (cost, manpower, machinery, materials), add a **1-2 sentence narrative** explaining the numbers.
- Keep the structure clear and professional. Avoid overly long paragraphs.
- Ensure no single section exceeds 250 words.

Include (in this exact order):
1. Executive Summary
2. Site Assessment (terrain, soil, climate)
3. Estimated Project Cost and Budget
   - Fetch latest cost benchmarks from **authentic web sources** such as MoRTH circulars, CAG reports, NHAI updates, or recent expressway/highway project announcements.
   - Provide a detailed table with cost heads (land acquisition, materials, machinery, labor, safety, contingency).
   - Ensure the cost values are **realistic and consistent with project type and scale**.
   - Always provide a short explanation of how the estimates were derived with reference to the chosen benchmarks.
4. Manpower Plan (technical, skilled, unskilled) in a table + explanation
5. Machinery Plan in a table + explanation
6. Material Requirements in a table + explanation
7. Risks and Potential Delays (weather, terrain, logistics)
8. Mitigation Strategies
9. Expected Completion Date considering weather and terrain
10. New Reforms & Policy Updates
    - Summarize latest government notifications, MoRTH guidelines, NHAI circulars
    - Include relevant policy references (e.g., https://morth.gov.in/en/New-Material-Technology-on-NH, Indian Infrastructure Highway Reforms)
11. Sustainable & Cost-Efficient Practices
    - Explain methods/resources (e.g., recycled aggregates, fly ash, cold mix, green concrete)
    - Include cost-cutting measures while ensuring compliance and quality
12. MoRTH & Statutory Compliance
    - Highlight rules/acts/standards applicable
    - Reference MoRTH updates, IRC codes, and environmental clearances
13. Recent Completed Projects & Research Learnings
    - Case studies or schemes by NHAI/MoRTH
    - Innovations and lessons to adopt
14. Road Safety Integration
    - Safety policies, lane safety, crash barriers, lighting, and smart monitoring
15. Traffic Diversion & Route Management
    - Diversion plans for ongoing traffic
    - Temporary signage, communication strategy, and public safety measures
16. **Final Summary (MANDATORY)**
    - Provide a 1-2 paragraph summary
    - Recap budget feasibility, manpower readiness, compliance alignment, risks and mitigations
    - End with a clear project readiness statement (e.g., "Project feasible within allocated budget and expected to be completed within timeframe").

Constraints:
- Avoid overly small bullet points; use 1 sentence minimum.
- Allow short paragraphs if needed for explanation.
- Ensure the **Final Summary** is always included.
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
        report_text = call_claude(prompt, max_tokens=7000)
        return {"success": True, "report": report_text}
    except Exception as e:
        return {"success": False, "error": str(e)}
