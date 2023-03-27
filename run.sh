#!/bin/sh

# Install required packages
apk add --no-cache python3-dev py3-pip
# pip install tensorflow
python3 -m pip install tensorflow


# Run the factorial.py script with a sample input
python /app/repo/train.py

# Create output directory if it doesn't exist
mkdir -p /app/repo/output

# Move the model to the output directory
mv /app/repo/model.h5 /app/repo/output/model.h5
