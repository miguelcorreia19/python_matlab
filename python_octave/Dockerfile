FROM python:3
WORKDIR /code
COPY requirements.txt /code
RUN apt-get update && \
    apt-get install -y gnuplot octave && \
    apt-get clean && \
    pip install -r requirements.txt
CMD ["api.py"]
ENTRYPOINT ["python3"]