# Simple REST API with Flask 🚀

This is a basic REST API built using Flask and deployed on Render.

## Endpoints

- `GET /` → Welcome message
- `GET /todos` → Get all todos
- `POST /todos` → Add new todo (JSON body)
- `PUT /todos/<id>` → Update a todo
- `DELETE /todos/<id>` → Delete a todo

## Deployment on Render
1. Push this repo to GitHub
2. Go to [Render](https://render.com/)
3. Create a new **Web Service**
4. Build command:
   ```bash
   pip install -r requirements.txt
