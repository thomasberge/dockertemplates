FROM python:3.7-stretch
RUN mkdir /code
RUN mkdir /code/logs
WORKDIR /code
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD /code .
CMD ["gunicorn", "-b 0.0.0.0:5010", "-w 1", "-t 1", "app:app"]
