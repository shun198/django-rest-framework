FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# COPY requirements.dev.txt /code/
ARG DEV=false
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
    # && \
    # if [ $DEV="true" ]; \
    #     then pip install -r requirements.dev.txt; \
    # fi
COPY . /code/
