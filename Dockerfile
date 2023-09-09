FROM python
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY *.py ./
RUN rm requirements.txt
CMD ["python", "main.py"]