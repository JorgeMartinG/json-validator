# Use Alpine Image (version 3.18.0)
FROM alpine:3.18.0

# Install requirements (python3, py3-pip) 
RUN apk add --no-cache python3 py3-pip

# Set Current Working Directory
WORKDIR /app

# Copy JSON file and python validator script
COPY json/ json/
COPY validation.py .

# Run Pyhton validator script
RUN python3 validation.py