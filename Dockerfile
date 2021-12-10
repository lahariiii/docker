# init a base image
FROM alpine: latest 
RUN apk update
RUN apk add python3 
RUN apk add py-pip
# copying the contents
COPY. /app 
# defining the working directory
WORKDIR /app
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
EXPOSE 5000
# command to run the program
CMD ["python3", "app.py"]

