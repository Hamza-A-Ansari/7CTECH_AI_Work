# Use Python base image
FROM python:3.12-slim

# Install necessary packages for git and cron
RUN apt-get update && apt-get install -y cron

# Set the working directory
WORKDIR /fp_gen_tags

# Copy the necessary files
COPY Code /fp_gen_tags/

# Install Python dependencies directly without creating a virtual environment
RUN pip install --upgrade pip && pip install -r requirements.txt

# Create a cron job file
RUN echo "0 23 * * * /usr/local/bin/python3 /fp_gen_tags/main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/fp_gen_tags_cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/fp_gen_tags_cron

# Apply cron job
RUN crontab /etc/cron.d/fp_gen_tags_cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Echo message during build
RUN echo "Docker image for fp_gen_tags is being built."

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log