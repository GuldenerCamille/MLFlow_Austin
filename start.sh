#!/bin/bash

gunicorn -b 0.0.0.0:5000 run_mlflow:app