# Project title
    🥤 Juice & Shake Recommendation System

## 📌 Project Description

The **Juice & Shake Recommendation System** is a lightweight Python-based web application that recommends juices and shakes based on **flavors** (e.g., *Chocolate, Mango, Strawberry*) and **drink type** (e.g., *Shake, Juice, Drink*).

It combines:

* **Supabase (Postgres)** for data storage
* **FastAPI** for the backend API
* **Streamlit** for the frontend UI

This project is ideal for learning **database integration, REST API design, and interactive frontend development** in Python.

---

## 🚀 Features

* Add and store drinks in **Supabase** database
* Search and filter drinks by **flavor** and/or **type**
* FastAPI-powered backend with interactive API docs
* Streamlit frontend with dropdowns and search bar
* Beginner-friendly modular code structure

---

## 📂 Project Structure

```
JuiceRecommendation/
│
|---src/                 # Core application logic
|     |---logic.py       # Business logic for recommendations
|     |__db.py           # Database operations (Supabase)
|
|---api/                 # Backend API
|     |__main.py         # FastAPI endpoints
|
|---frontend/            # Frontend application
|     |__app.py          # Streamlit UI
|
|___requirements.txt     # Python dependencies
|___README.md            # Project documentation
|___.env                 # Environment variables
```

---

## ⚡ Quick Start

### ✅ Prerequisites

* Python **3.8+**
* Supabase account
* Git installed

---

### 1️⃣ Clone the Project

```bash
git clone <repository-url>
cd JuiceRecommendation
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Supabase Database

1. Create a **Supabase project**
2. In the **SQL Editor**, run:

```sql
create table drinks (
    id bigserial primary key,
    name text not null,
    type text not null,          -- Shake, Juice, Drink
    flavors text[] not null      -- Array of flavors ['Chocolate','Sweet']
);
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in project root:

```env
SUPABASE_URL="https://<your-project>.supabase.co"
SUPABASE_KEY="<your-anon-key>"
```

---

### 5️⃣ Run the Application

#### 🔹 FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Visit → `http://127.0.0.1:8000/docs`

#### 🔹 Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

## 🛠 How to Use

1. Open the **Streamlit UI**
2. Enter a **flavor** (e.g., *Chocolate*)
3. Choose a **drink type** (Shake/Juice/Drink/Any)
4. Get recommendations like:

   * *Oreo Shake*
   * *Choco Chip Shake*
   * *Ferrero Rocher Thickshake*

---

## ⚙️ Technical Details

### 🏗 Technologies Used

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** Supabase (Postgres)
* **Language:** Python 3.8+

### 🔑 Key Components

* `src/db.py` → Handles Supabase database operations
* `src/logic.py` → Implements recommendation logic
* `api/main.py` → FastAPI endpoints for API access
* `frontend/app.py` → Streamlit interface for users

---

## 🐞 Troubleshooting

**Common Issues:**

1. `"Module not found"` → Run:

   ```bash
   pip install -r requirements.txt
   ```
2. API not working → Check your `.env` Supabase credentials
3. Port conflict → Change FastAPI port:

   ```bash
   uvicorn api.main:app --reload --port 8001
   ```

---

## 🔮 Future Enhancements

* Add **ingredient-based search** (e.g., suggest based on available fruits)
* Add **seasonal filters** (e.g., mango in summer)
* Add **ratings & popularity tracking**
* Expand dataset with 50+ juices & shakes
* Add **NLP-based flavor matching** (e.g., "something creamy and sweet")

---

## 📧 Support

For issues/questions:

* Email: **[hasinigurram2023@gmail.com](mailto:hasinigurram2023@gmail.com)**
* Contact: **+91 6304712142**

---
