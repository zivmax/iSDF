docker run --gpus all --rm \
    -v /home/zivmax/sist/research/iSDF/:/workspaces/iSDF \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $HOME/.Xauthority:/home/hakon/.Xauthority \
    -e DISPLAY=unix$DISPLAY \
    -h $HOSTNAME \
    -it isdf bash
