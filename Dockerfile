FROM kalilinux/kali-rolling
RUN apt-get update && apt upgrade -y

RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    axel \
    openssl \
    pv \
    jq \
    wget \
    python3-dev \
    libreadline-dev \
    openjdk-13-jdk \
    zipalign \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    chromium \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev \
    sudo \
    chromium \
    chromium-chromedriver

RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip install wheel 
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache

RUN git clone https://github.com/amitsharma123234/Plus /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
CMD ["python3","-m","userbot"]
