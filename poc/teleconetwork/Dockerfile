FROM python:3.8

COPY ./basicoperator.py /

RUN pip install --upgrade pip

RUN pip install kopf && \
pip install kubernetes


CMD kopf run ./basicoperator.py --verbose