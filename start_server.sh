#!/usr/bin/env bash
uvicorn App.server:app --host 0.0.0.0 --port 5000 --workers 4
