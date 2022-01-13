FROM python:3

WORKDIR /usr/src/app

#copy only requirement files over
COPY requirements.txt ./
COPY LICENSE.md ./
COPY logger.conf ./
COPY data.json ./
COPY env.py ./
COPY start.py ./

#ENV TERM=xterm

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./start.py" ]
#CMD ["/bin/bash"]