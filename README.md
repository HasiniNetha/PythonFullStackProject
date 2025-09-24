# Project Title: 
     Micro Diary API

# Project Description:
Micro Diary API is a simple and lightweight journaling service that allows users to create daily journal entries via API calls. Each entry supports text content with optional tagging (e.g., #happy, #work), making it easy to categorize and filter entries by date or tags. The API supports efficient filtering and pagination, making it perfect for practicing backend development skills like RESTful API design, database relationships, and query optimization.

## Project Features:

Create, edit, and delete daily journal entries with tags.
Filter entries by date or tags with pagination.
Full-text search using Python or PostgreSQL features.
Automatic tag suggestions via Python NLP (e.g., spaCy).
Mood tracking on entries.
Export entries as JSON or CSV.
User authentication and rate limiting.
Daily reminders via email or webhook.
Multi-user support with private/public entries.
Tag popularity stats.
Support for image/audio attachments.

Ideal for developers looking to build practical experience with APIs, data filtering, and pagination.



## Project Structure

MicroDiary/
|
|---src/                 #core application logic
|     |---logic.py       #Business logic and task
operations
|     |__db.py           #database operations
|
|---api/                 #Backend api
|     |__main.py         #FastAPI endpoints
|
|---frontend/            #frontend application
|     |__app.py          #streamlit application
|
|___requirements.txt     #Python Dependencies
|
|___README.md            #Project documentation
|
|___.env                 #Python Variables 


## Quick Start

### Prerequisites

- Python 3.8 or higher
- A-Supabasee account
- Git(Push,cloning)

### 1.Clone or Download the Project 
# Option 1:Clone with Git
git clone <repository-url>
# Option 2:Download and extract the ZIP file
### 2.Install all required python packages
pip install -r requirements.txt

### 3.Set Up Supabase Database

1.Create a Supabase project:

2.Create  the tasks table:

- Go to the SQL Editor in your Supabase dashboard
- Run this SQL command:
```sql

-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Entries table (includes mood, media URLs, privacy)
CREATE TABLE entries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  text TEXT NOT NULL,
  mood VARCHAR(20),
  is_private BOOLEAN DEFAULT TRUE,
  media_urls TEXT[] DEFAULT '{}',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  tags TEXT[] DEFAULT '{}' -- store tags as an array of strings
);

-- Reminders table for daily reminders
CREATE TABLE reminders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  reminder_time TIME NOT NULL,
  channel VARCHAR(50) NOT NULL, -- 'email' or 'webhook'
  target VARCHAR(255) NOT NULL,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Full-text search index on entries.text
CREATE INDEX entries_text_search_idx ON entries USING gin(to_tsvector('english', text));


```
** Get your Credentials:

### 4. Configure Environment Variables

1. create a `.env` file in the project root

2. Add your supabase credentials to `.env`:
SUPABASE_URL="https://kxfcjceuqdiggdncwvly.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdjbmx6Ynptc3hyd29ydGh0anhuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI1ODYsImV4cCI6MjA3MzY1ODU4Nn0.IKZOBmQo22TCSFHHnrzgGiGczu9kx04gmHc9fSPcoqM"

### 5. Run the Appilication

### Streamlit Frontend
streamlit run fornend/app.py


### FastAPI Backend

cd api
python main.py


## How to Use

## Technical Details

## Technologies used

   **Frontend**: Streamlit(Python web framework)
   **Backend** :  fastAPI (Python REST API framework)
   **Database**: Supabase (PostgresSQL-based backend-as-a-service)
   **Language**: Python 3.8+

### key Components
1. ** `src/db.py`**: Database operations
      - Handles all CRUD operations with Supabase
2. ** `src/logic.py`**: Business logic 
      - task Validation an processing

## TroubleShooting

   ##  Common Issues

      1. **"Module not found" errors**
         - Make sure you've installed all dependencies: `pip install -r requirements.txt`
         - Check that you're running commands from the correct directory


## Futeure Enhancements

   Ideas for extending this project

   # Key Extension Ideas:
    Sentiment analysis to auto-detect mood from entries
    Entry versioning to track edits over time
    Social sharing for collaborative journaling
    Rich media support (images/audio) in entries
    Customizable reminders to encourage daily journaling
    Export/import entries for backup and portability
    Analytics dashboard showing mood and tag trends


## Support 

If you encounter any issues or have questions:
      emailID:hasinigurram2023@gmail.com
      Ph No:6304712142

