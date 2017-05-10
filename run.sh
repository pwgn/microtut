#!/bin/sh

source env/bin/activate

tmux new-session -d

tmux split-window -d -t 0 -h
tmux split-window -d -t 0 -v
tmux split-window -d -t 0 -v
tmux split-window -d -t 3 -v
tmux split-window -d -t 4 -v

tmux send-keys -t 0 'python discoveryservice/discoveryservice.py' enter
tmux send-keys -t 2 'python apigateway/apigateway.py' enter

sleep 1

tmux send-keys -t 5 'python authservice/authservice.py' enter
tmux send-keys -t 4 'python articleservice/articleservice.py' enter
tmux send-keys -t 1 'python commentservice/commentservice.py' enter

tmux send-keys -t 3 'cd frontend; python -m http.server 8000' enter

tmux attach
