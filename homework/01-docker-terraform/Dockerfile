FROM python:3.9
RUN pip install pandas sqlalchemy psycopg2
WORKDIR /app
COPY data_ingest_pipeline.py data_ingest_pipeline.py
ENTRYPOINT [ "python", "data_ingest_pipeline.py" ]