---

# ✍️ Blog API (FastAPI + SQLite + Pydantic)

A simple and professional **Blog API** built with **FastAPI**, **SQLite**, and **Pydantic**.
This project demonstrates how to create, list, and delete blog posts while applying **data validation**, **path & query parameters**, and **database persistence**.

---

## 🚀 Features

* 📝 **Create Blog Post** – Add new posts with title & content
* 📖 **List Blog Posts** – Fetch all posts with pagination (query params)
* ❌ **Delete Blog Post** – Remove a post by its ID
* ⚡ **FastAPI** for modern, high-performance APIs
* ✅ **Pydantic Models** for request & response validation
* 🗄️ **SQLite** database for data persistence

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI** – Web framework
* **SQLite** – Database
* **SQLAlchemy** – ORM
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server

---

## 📂 Project Structure

```
blog_api/
│── main.py          # Entry point of the API
│── database.py      # DB connection setup
│── models.py        # SQLAlchemy models
│── schemas.py       # Pydantic models
│── crud.py          # Database operations (create, read, delete)
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/blog-api.git
   cd blog-api
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API**

   ```bash
   uvicorn blog_api.main:app --reload
   ```

---

## 🔗 API Endpoints

### ➕ Create Blog Post

**POST** `/blogs/`
Request body:

```json
{
  "title": "My First Blog",
  "content": "Hello, this is my first post!"
}
```

---

### 📖 List All Blog Posts

**GET** `/blogs/?skip=0&limit=10`

* `skip` → number of records to skip (default: 0)
* `limit` → number of records to return (default: 10)

Response:

```json
[
  {
    "id": 1,
    "title": "My First Blog",
    "content": "Hello, this is my first post!"
  }
]
```

---

### ❌ Delete Blog Post

**DELETE** `/blogs/{blog_id}`
Example:

```bash
DELETE /blogs/1
```

Response:

```json
{
  "message": "Blog 1 deleted successfully"
}
```

---

## 📸 API Documentation

Once the server is running, you can explore the interactive docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Future Improvements

* 🔒 Add authentication & authorization (JWT)
* 📝 Update blog posts (PUT/PATCH)
* 🔍 Search & filter blogs
* 📊 Add tags & categories

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

Would you like me to also generate a **`requirements.txt`** file so that this README setup works immediately when someone clones your repo?
