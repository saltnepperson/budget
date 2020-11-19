# Base image to pull from
FROM python:3.9

# Get that credit
LABEL AUTHOR="Tyler Epperson"
LABEL EMAIL="tepperson22@gmail.com"

# Change where we're working
WORKDIR /budget

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
COPY docker.env .env

# Download requirements
RUN pip3 install -r requirements.txt

# Copy over the application
COPY . .

RUN pip3 install .

# Serve it up
CMD ["gunicorn", "--config", "config/gunicorn-config.py", "budget.manage:app"]