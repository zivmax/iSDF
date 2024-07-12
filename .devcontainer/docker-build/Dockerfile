# Use an official Miniconda runtime as a parent image
FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel

# Set the working directory in the container
WORKDIR /workspace

ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i -e 's|http://archive.ubuntu.com/ubuntu|https://mirrors.shanghaitech.edu.cn/ubuntu|g'  \
	-i -e 's|http://security.ubuntu.com/ubuntu|https://mirrors.shanghaitech.edu.cn/ubuntu|g' \
	/etc/apt/sources.list

RUN apt update
RUN apt upgrade -y --fix-missing
RUN apt install -y curl 
RUN apt install -y wget 
RUN apt install -y systemd 
RUN apt install -y git 
RUN apt install -y p7zip-full

# Clean up to reduce image size
RUN apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install any dependent packages
RUN pip config set global.index-url https://mirrors.shanghaitech.edu.cn/pypi/web/simple
COPY environment.yml ./
RUN conda env create -f environment.yml

# Make port 80 available to the world outside this container
EXPOSE 80

RUN rm ./environment.yml


