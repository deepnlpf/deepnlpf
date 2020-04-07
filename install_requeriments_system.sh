#!/bin/bash

# Maintainer: RodriguesFAS <franciscosouzaacer@gmail.com>
# Description: DeepNLPF
# Date: 16/01/2019

option=2

echo "=======================================================
🐙 Install Requeriments System in Ubuntu 19.04 from DeepNLPF.
Author: RodriguesFAS
Email: franciscosouzaacer@gmail.com
Page oficial: https://deepnlpf.github.io/site
Select option:
    y - Install (Java 8, Python 3.7, Pip and MongoDB)
    n - Exit.
"

read option

case $option in

    y)
        echo "🐙 >> Update package.."
        sudo apt update

        echo "🐙 >> Installing Java 8.."
        sudo apt install openjdk-8-jdk openjdk-8-jre
        java -version
        
        echo "🐙 >> Installing Python 3.7.."
        sudo apt install software-properties-common
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt install python3.7
        sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
        python --version
        
        echo "🐙 >> Installing Pip .."
        sudo apt install python-pip
        pip --version

        sudo apt install python3-pip
        pip3 --version
        
        echo "🐙 >> Installing MongoDB.."
        sudo apt install -y mongodb

        echo "🐙 Installation completed successfully."
        ;;

    *)
        echo "🐙 Option err!"
        ;;

    esac