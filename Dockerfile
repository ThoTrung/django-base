FROM python:3.9-alpine3.13
LABEL maintainer="londonappdeveloper.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
# For production only after
# COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps

RUN adduser \
        --disabled-password \
        --no-create-home \
        www-data
ARG USER_ID
ARG GROUP_ID
RUN apk add --no-cache shadow
RUN groupmod --gid ${GROUP_ID} www-data && \
    usermod -u ${USER_ID} www-data
RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R www-data:www-data . && \
    chown -R www-data:www-data /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER www-data

CMD ["run.sh"]
