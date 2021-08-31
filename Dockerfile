FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --ignore-installed -r requirements.txt
RUN pip install --ignore-installed -r req2.txt
RUN pip3 uninstall numpy
RUN pip3 uninstall numpy
RUN pip install numpy
CMD python flask_api.py