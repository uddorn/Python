FROM python:3.11-slim

WORKDIR /tkachenko

COPY 1_tkachenko.py .
COPY 17_tkachenko.py .

CMD ["/bin/bash"]