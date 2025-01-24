# 使用 Python 基礎 Image
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 複製專案環境與相關檔案
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 啟動 Django 開發伺服器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
