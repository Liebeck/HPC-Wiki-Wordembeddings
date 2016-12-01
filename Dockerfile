FROM liebeck/miniconder3

RUN apt-get update && \
	apt-get install -y build-essential libxml2-dev libxslt-dev libsm6 libxrender1 libfontconfig1 libicu-dev python-dev && \
	apt-get clean

# install packages with conda
RUN conda install -y \
  pip \
  numpy

RUN pip install gensim

RUN sudo echo "Europe/Berlin " > /etc/timezone
RUN sudo dpkg-reconfigure -f noninteractive tzdata

WORKDIR /var/www
ADD . .
RUN pip install -e .

