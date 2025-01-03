# Florida Business Search Microservice

A microservice application to scrape business data from the Florida Sunbiz website and display it via a frontend interface. The application includes a backend (FastAPI) and a frontend (React), with a database integration (Supabase).

---

## Features

- Scrapes business data using Playwright.
- Stores scraped data in Supabase.
- Provides RESTful APIs for data retrieval.
- Beautiful frontend built with React and Tailwind CSS.

---

## Prerequisites

Ensure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.10 or higher)
- **Supabase** project with proper database setup
- **Docker** (if using the Docker setup)
- **Playwright dependencies** (installed automatically via Playwright)

---

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/florida-business-search.git
cd florida-business-search
```

### 2. Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file in the backend directory and add the following:

   ```bash
   SUPABASE_URL=<your-supabase-url>
   SUPABASE_KEY=<your-supabase-key>
   ```

4. Run the backend server:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

   The backend will be available at http://localhost:8000.

---

### 3. Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Install the required dependencies:

   ```bash
   npm i
   ```

3. Start the frontend development server:

   ```bash
   npm start
   ```

   The frontend will be available at http://localhost:3000.

---

## Docker Setup (Optional)

### 1. Build and Run the Application

1. Ensure Docker is installed and running.

2. Build and start the application using Docker Compose:

   ```bash
    docker-compose build
    docker-compose up
   ```

3. The services will be available at:
   - Backend: http://localhost:8000
   - Frontend: http://localhost:3000

---

PS: Change the Table Name in database.py
