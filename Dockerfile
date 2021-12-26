FROM nikolaik/python-nodejs:python3.9-nodejs16

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

RUN cd /
RUN git clone https://github.com/LEGEND-OS/MUSIC-VC
RUN cd MUSIC-VC
WORKDIR /MUSIC-VC

RUN pip3 install --upgrade pip

CMD python3 main.py

#Repo Clonning ⚡♥️
RUN git clone https://github.com/The-LegendBot/LEGENDUSERBOT.git /root/userbot

#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
