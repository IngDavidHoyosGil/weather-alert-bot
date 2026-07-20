#!/bin/bash

echo "========== $(date) =========="

cd /home/ubuntu/weather-alert-bot || exit 1

source .venv/bin/activate

python -m src.main