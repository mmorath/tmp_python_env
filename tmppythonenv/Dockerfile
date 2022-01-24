FROM python:3

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

#run pip install and get all upgrades...
RUN pip install --upgrade pip

#RUN adduser worker
RUN useradd -ms /bin/bash worker
#change user to worker
USER worker
#change to home directory of worker
WORKDIR /home/worker/

#install pipenv to local directory of user ...currently active "worker"
RUN pip install --user -U --no-warn-script-location pipenv  

#copy only requirement files over, for simplicity ..
COPY --chown=worker:worker requirements.txt ./
COPY --chown=worker:worker LICENSE.md ./
COPY --chown=worker:worker logger.conf ./
COPY --chown=worker:worker data.json ./
COPY --chown=worker:worker env.py ./
COPY --chown=worker:worker start.py ./

#install with the user the requirements
RUN pip install --user -r requirements.txt

#add the workder home directory to the path variable, is required because of the command from above..which notifies 
#about this therefore "--no-warn-script-location pipenv " was added...
ENV PATH="/home/worker/.local/bin:${PATH}"

#change the owner to worker:worker
COPY --chown=worker:worker . .

#add a label 
LABEL maintainer="matthias.morath@liebherr.com" \
      version="1.0.0"

#finally call python and start the script start.py
CMD [ "python", "./start.py" ]