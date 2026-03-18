FROM python:3.12-slim

WORKDIR /Tkachenko

COPY gtrans3.py /Tkachenko/
COPY my_trans_pack/ /Tkachenko/my_trans_pack/

RUN pip install googletrans==3.1.0a0

CMD ["python", "gtrans3.py"]
