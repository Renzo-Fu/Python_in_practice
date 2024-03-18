# Use an official LaTeX Docker image as a base
FROM blang/latex:ubuntu

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python code and data into the container
COPY . .

# Install any necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y ghostscript

# Install required Python packages
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Generate the .tex file
RUN python3 create_table_tex.py

# Compile the .tex file into PDF
RUN pdflatex example_document.tex

# Cleanup unnecessary files
RUN rm *.log *.aux

# Expose the port
# EXPOSE 8080

# Command to run the application
# CMD ["python3", "app.py"]
