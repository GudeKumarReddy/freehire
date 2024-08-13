FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /DOC_HOME

#copying requirements
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/DOC_HOME/entrypoint.sh"]

CMD ["python", "manage.py",  "runserver", "0.0.0.0:8001"]