FROM python:3.7.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN echo 'deb http://ftp.de.debian.org/debian buster main contrib' > /etc/apt/sources.list.d/fonts.list
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libhunspell-dev hunspell-en-us poppler-utils libdb++-dev
# TODO: get ttf-mscorefonts-installer
RUN fc-cache
RUN python3 -m pip install gutenberg
COPY update_cache.py update_cache.py
RUN python3 update_cache.py
COPY requirements.txt /usr/src/app/
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt --src /usr/local/src
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
RUN python3 -m spacy download en_core_web_sm
RUN python3 -m nltk.downloader averaged_perceptron_tagger

ENTRYPOINT python3 server.py