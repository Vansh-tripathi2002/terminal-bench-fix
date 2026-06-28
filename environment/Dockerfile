FROM python:3.13-slim@sha256:f8db1fe0914241bb48c2ec09ba80490e5e5c52f08e3f57bff6f1e3fcfb0ec2b0

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log