FROM python:3.13-slim-trixie

# uv from official binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

ENV UV_COMPILE_BYTECODE=1   \
    UV_LINK_MODE=copy       \
    PYTHONUNBUFFERED=1      \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY pyproject.toml uv.lock* ./ 

RUN uv sync --no-install-project --no-dev
    

COPY . .
RUN uv sync --no-dev 

COPY scripts/entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh 

ENTRYPOINT ["/entrypoint.sh"]
CMD ["uv", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
