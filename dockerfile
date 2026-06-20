FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app
COPY --chown=user . $HOME/app

EXPOSE 7860

CMD streamlit run app.py \
    --server.headless true \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --server.fileWatcherType none \
    --server.port 7860 \
    --server.address 0.0.0.0