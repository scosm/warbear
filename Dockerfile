
# The root folder of the entire project on the local (dev) machine.
ARG context=workboard_web

###########################################################
# BACKEND
# Stage 1: Build the backend image.
###########################################################

# v3.13.3 avoids security vulnerabilities of 3.11.2.
FROM python:3.13.3-slim AS backend

#######################################
# Copy straggler files that will still be left in the root folder, not taken care of in Stages 1 and 2.
# Source location is the root folder (determined by the build context, the command line).
# Destination location is the working folder, determined above by WORKDIR /${context} .
RUN rm -rf /workboard_web && mkdir -p /workboard_web
COPY README.md /workboard_web/

# Install poetry (not using pip).
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && mv /root/.local/bin/poetry /usr/local/bin/poetry

#######################################
# VARIABLES (build and run)
# Define BUILD VARIABLES here (image).
ARG context
ARG back_port=8000
ARG front_port=3000

# Define RUN-TIME VARIABLES here (container).
ENV context=${context}
#ENV REDIS_HOST=redis
ENV back_port=8000
ENV front_port=3000

#######################################

# Guarantee that the root folder exists.
#RUN if [ ! -d "/${context}/app/backend" ]; then mkdir -p /${context}/app/backend; fi
#RUN if not exist ${context} mkdir ${context}
RUN mkdir -p /${context}

WORKDIR /${context}  # Root of backend and frontend code on the dev machine.

# Copy pyproject.toml and poetry.lock files (for package management).
COPY pyproject.toml poetry.lock /

# Later, we might create a "dev" group and distinguish dependencies that are just for development: RUN poetry install --without dev
RUN poetry install

# Copy backend source tree.
COPY app/backend/ ${context}


###########################################################
# FRONTEND
# Stage 2: Build the frontend.
###########################################################

FROM node:23-slim AS frontend

ARG context
ARG back_port
ARG front_port

# Create the frontend folder explicitly.
#   RUN mkdir -p /frontend
RUN mkdir -p /workboard_web/frontend

# Copy essential files into the frontend directory.
# These "package" files are in (only) the frontend, as they are created by npm, which the backend does not use.
#COPY frontend/package.json frontend/package-lock.json /frontend/
# Copy all frontend files into workboard_web/frontend (and NOT /frontend/). This will also grab the "package" files.
COPY frontend/ /${context}/frontend/

WORKDIR /${context}/frontend

# Install dependencies
RUN npm install
#RUN npm ci

# Build the frontend!
RUN npm run build


###########################################################
# COMBINED IMAGE
# Stage 3: Combined image.
###########################################################

FROM python:3.13.3-slim AS final

#######################################
# VARIABLES (build and run)
# Define BUILD VARIABLES here (image).
ARG context 
ARG back_port
ARG front_port

WORKDIR /${context}

# Copy backend from backend stage.
COPY --from=backend /${context}/app/backend app/backend

# Copy frontend from frontend stage.
COPY --from=frontend /${context}/frontend frontend

# Run both backend and frontend.
CMD ["sh", "-c", "python /${context}/app/backend/main.py & npx serve -s /${context}/frontend -l ${front_port}"]

# Expose thhe ports for the backend API and the frontend UI.
EXPOSE ${back_port} ${front_port}
