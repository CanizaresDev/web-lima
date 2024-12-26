FROM python:3.11

WORKDIR /app
COPY requirements.txt .

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["reflex", "run", "--env", "prod", "--backend-only"]