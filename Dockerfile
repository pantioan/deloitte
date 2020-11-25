# Create layer form the python:3-alpine image
FROM python:3-alpine

# Copy files to code folder
COPY . /code
 
# Make code folder our work directory
WORKDIR /code
 
# Install all packages included in requirement file
RUN pip install -r requirements.txt
 
# Run the Flask application
CMD [ "python", "main.py" ]