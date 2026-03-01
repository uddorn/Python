FROM python:3.11-slim
RUN mkdir /Tkachenko
WORKDIR /Tkachenko
COPY lab2IsHere.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "lab2IsHere.py"]
