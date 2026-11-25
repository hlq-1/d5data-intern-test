# D5Data Intern Test

Frontend Engineer Intern Test.

- `frontend/`: resume upload page (drag & click upload, responsive layout, button hover/active states)
- `fastapi-stream/`: FastAPI SSE-style streaming response demo

## Frontend

Open `frontend/upload.html` directly in a browser.

Features:
- Drag-and-drop upload and click-to-select upload
- Display selected file name
- Button hover / active interaction states
- Responsive layout: side-by-side on desktop, stacked vertically on narrow screens (<768px)

## FastAPI Streaming Demo

```bash
cd fastapi-stream
pip install -r requirements.txt
python main.py
```

- Stream endpoint: http://127.0.0.1:8000/stream
- API docs (Swagger): http://127.0.0.1:8000/docs

> （注：部分内容由豆包 AI 生成）