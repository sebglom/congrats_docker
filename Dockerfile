# Leichtes Python-Image
FROM python:3.12-alpine

WORKDIR /app
COPY run.py ascii.txt ./

# Saubere UTF-8-Ausgabe + keine Pufferung
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

CMD ["python", "/app/run.py"]
