# Usa una imagen ligera y moderna de Python
FROM python:3.11-slim

# Establece variables para evitar errores en compilación
ENV CFLAGS="-std=c99"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece la carpeta de trabajo
WORKDIR /app

# Copia todos los archivos del proyecto
COPY . .

# Instala dependencias del sistema necesarias para 'unstructured'
RUN apt-get update && apt-get install -y \
    libmagic1 \
    build-essential \
    poppler-utils \
    tesseract-ocr \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Actualiza pip
RUN pip install --upgrade pip

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Expone el puerto del API
EXPOSE 8000

# Comando para levantar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
