#!/bin/sh
gunicorn entry_point:app --bind=0.0.0.0:5000