
FROM python:3.9-slim

WORKDIR /app

COPY shivashakti_core.py .
COPY web_app.html .
COPY admin_interface.html .

RUN pip install flask

EXPOSE 8000

CMD ["python", "shivashakti_core.py"]
