# Deploy DeepNLPF in AWS EC2 or Azure

# Install Enginx

    sudo apt install enginx

# Config
[Tutorial base](https://www.youtube.com/watch?v=tW6jtOOGVJI&list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP&index=4).
    
    $ cd /etc/nginx/sites-available
    $ sudo nano deepnlpf_api

    server {
        listen 80;
        server_name http://192.168.1.5/;

        location / {
            proxy_pass http://127.0.0.1:5000;
        }
    }

    $ sudo service nginx restart

# Execute deepnlpf api task backgroud server terminal

    nohup deepnlpf --api start