FROM python:3.12-slim

RUN pip install uv

WORKDIR /app
COPY pyproject.toml .
RUN uv sync

COPY . .

CMD ["uv", "run", "python", "-m", "mice-to-meet-you"]
