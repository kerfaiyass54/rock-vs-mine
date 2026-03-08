FROM Python

WORKDIR /app

COPY requirements.txt

RUN pip install -r requirements.txt

COPY /config .

COPY /data .

COPY /entrypoint .

COPY /pipeline

VOLUME /rockMine

EXPOSE 80

CMD ["mkdir","models"]

CMD ["python3","/entrypoint/train.py"]

CMD ["python3","/entrypoint/inference.py"]