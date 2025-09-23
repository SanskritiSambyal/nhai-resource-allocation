## 🏗️ NHAI Resource Allocation Assistant

An AI-powered tool that generates **NHAI-specific resource allocation reports** for highway, bridge, and tunnel projects across India.
It combines a **FastAPI backend** (Claude-powered AI logic) and a **Streamlit frontend** (user interface).

### ⚙️ Tech Stack

* **Backend**: FastAPI, Uvicorn, Anthropic Claude API
* **Frontend**: Streamlit, Markdown2
* **Deployment**:

  * Backend → Render
  * Frontend → Streamlit Cloud

### 🚀 Getting Started

#### 1️⃣ Clone Repository

git clone https://github.com/your-username/nhai-resource-allocation.git

cd nhai-resource-allocation


#### 2️⃣ Backend Setup (FastAPI)

##### Install dependencies

cd backend

pip install -r requirements.txt

##### Add `.env`

Create a `.env` file inside `backend/`:

ANTHROPIC_API_KEY=your_api_key_here

##### Run locally

uvicorn main:app --reload


#### 3️⃣ Frontend Setup (Streamlit)

##### Install dependencies
cd frontend

pip install -r requirements.txt

##### Run locally
streamlit run app.py

Make sure backend is also running.


### 🌍 Deployment

#### Backend (Render)

1. Push repo to GitHub.
2. Create new **Web Service** on [Render](https://render.com).
3. Select `backend/` as the root.
4. Set **Start Command**:
   uvicorn main:app --host 0.0.0.0 --port $PORT
5. Add environment variable in Render dashboard:
   ANTHROPIC_API_KEY=your_api_key_here

Backend will be deployed at:
👉 `https://your-backend-service.onrender.com`


#### Frontend (Streamlit Cloud)

1. Go to [Streamlit Cloud](https://streamlit.io/cloud).
2. Connect GitHub repo.
3. Select `frontend/app.py` as the entrypoint.
4. In "Advanced Settings", set Python version to **3.11**.
5. Streamlit will auto-install from `frontend/requirements.txt`.

Update backend URL in `app.py`:

## Replace localhost with Render backend URL
response = requests.post("https://your-backend-service.onrender.com/allocate_resources", json=request_data)

Frontend will be deployed at:
👉 `https://your-streamlit-app.streamlit.app`


### 🧪 Sample Input

You can test with real NHAI-style project data:

{

  "project": {
  
    "project_name": "Delhi-Mumbai Expressway Section",
    
    "project_id": "P001",
    
    "location": "Delhi to Mumbai via Ahemdabad",
    
    "project_type": "Highway",
    
    "start_date": "2025-05-01",
    
    "duration_days": 180
    
  }
  
}


### ✅ Features

* AI-generated **technical allocation reports**
* NHAI-specific terminology and structure
* Covers manpower, machinery, materials, risk factors
* Interactive, collapsible frontend UI
* Ready for cloud deployment

