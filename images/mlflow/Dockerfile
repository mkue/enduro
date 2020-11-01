FROM python:3.8

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD mlflow server \
     --backend-store-uri ${BACKEND_STORE_URI} \
     --default-artifact-root ${DEFAULT_ARTIFACT_ROOT} \
     --expose-prometheus /tmp/metrics \
     --host 0.0.0.0 \
     --port ${PORT}
