# Use an official Miniconda runtime as a parent image
FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel

# Set the working directory in the container
WORKDIR /app

# Install system packages
ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt upgrade -y --fix-missing
RUN apt install -y curl
RUN apt install -y wget
RUN apt install -y systemd
RUN apt install -y git
RUN apt install -y p7zip-full
RUN apt install -y ffmpeg
RUN apt install -y freeglut3-dev

# Clean up to reduce image size
RUN apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/lib/dri/
RUN ln -s /usr/lib/x86_64-linux-gnu/dri/*.so /usr/lib/dri/

# Setting up Git
RUN git config --global --add safe.directory /workspaces/iSDF
RUN git config --global --add safe.directory /workspaces/iSDF/ORB_SLAM3_ros
RUN git config --global user.name zivmax
RUN git config --global user.email zivmax@foxmail.com

# Install dependent packages
RUN conda update -n base conda
COPY ./environment.yml ./env.yml
RUN conda env create -f env.yml
RUN conda init
RUN rm ./env.yml

# Make port 80 available to the world outside this container
EXPOSE 80

WORKDIR /workspaces/iSDF

ENTRYPOINT conda run -n isdf /bin/bash -c 'pip install -e .' && bash
 