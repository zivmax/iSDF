# Use an official Miniconda runtime as a parent image
FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel

# Set the working directory in the container
WORKDIR /app

# Install system packages
ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y curl 
RUN apt install -y wget 
RUN apt install -y systemd 
RUN apt install -y git 
RUN apt install -y p7zip-full
RUN apt install -y libxext6 
RUN apt install -y libsm6 
RUN apt install -y ffmpeg 

# Clean up to reduce image size
RUN apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install dependent packages
COPY env.yml ./
RUN conda env create -f env.yml
RUN rm ./env.yml

# Setting up Git
RUN git config --global --add safe.directory /workspaces/iSDF
RUN git config --global --add safe.directory /workspaces/iSDF/ORB_SLAM3_ros
RUN git config --global user.name zivmax 
RUN git config --global user.email zivmax@foxmail.com 

# Make port 80 available to the world outside this container
EXPOSE 80
