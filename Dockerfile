FROM python:3-alpine
WORKDIR /usr/src/app
COPY fizzbuzz.py .
CMD ["fizzbuzz.py"]
ENTRYPOINT ["python3"]
