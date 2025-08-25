# congrats_docker

A small docker container shipping a small terminal application :-=

## Requirements

- **Docker** (recommended)
  - Alternatively: **Podman** as a drop-in replacement.
- Internet access to pull the base image `python:3.12-alpine` on first build.

## Quick Start

```bash
# 1) Build the image (from the project folder)
docker build -t doktorhut-animated .

# 2) Run the application in the terminal (-it allocates a TTY)
docker run --rm -it doktorhut-animated
```

## Web Demo

Try the ASCII art in your browser via Streamlit:

[View the app](https://llm-congrats.streamlit.app)
