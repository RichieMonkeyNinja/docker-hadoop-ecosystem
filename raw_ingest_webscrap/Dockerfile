FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

# 1. Copy ONLY the dependency files first
COPY pyproject.toml uv.lock ./

# 2. Install dependencies (This layer is cached unless pyproject.toml changes)
RUN uv sync --frozen

# 3. NOW copy your script (This layer updates quickly when you change code)
COPY raw_data_ingestion.py ./

# No need for absolute paths in CMD since WORKDIR is /app
CMD ["uv", "run", "python", "raw_data_ingestion.py"]