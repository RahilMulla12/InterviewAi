# Interview AI Frontend

A modern React application that allows users to upload resumes, generate AI-powered interview questions, take mock interviews, receive AI feedback, and monitor their interview performance through analytics.

## Features

* User Authentication
* Dashboard
* Resume Upload
* Automatic Skill Detection
* Interview Setup
* AI Question Generation
* Answer Submission
* AI Evaluation & Feedback
* Analytics Dashboard
* User Profile Management
* Responsive Bootstrap UI

---

## Tech Stack

* React
* Vite
* React Router
* Bootstrap 5
* React Hot Toast
* Fetch API
* JWT Authentication
* Vercel

---

## Project Structure

```text
src/
│── components/
│── Context/
│── layouts/
│── pages/
│── Service/
│── utils/
│── App.jsx
│── main.jsx
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Frontend
```

Install dependencies:

```bash
npm install
```

---

## Environment Variables

Create a `.env` file for local development:

```env
VITE_API_URL=http://127.0.0.1:8000/api/
```

For production:

```env
VITE_API_URL=https://your-backend.onrender.com/api/
```

---

## Run Development Server

```bash
npm run dev
```

Frontend will be available at:

```
http://localhost:5173
```

---

## Build Production Version

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

---

## Pages

* Login
* Register
* Dashboard
* Resume Upload
* Interview Setup
* Interview Session
* Analytics
* Profile

---

## Deployment

Frontend is deployed on Vercel.

Production stack:

* React
* Vite
* Bootstrap
* Vercel

---

## Backend Connection

The frontend communicates with the Django REST API through the environment variable:

```env
VITE_API_URL=https://your-backend.onrender.com/api/
```

---

## Author

**Rahil Mulla**
# InterviewAi
