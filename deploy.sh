cp -r /mnt/space/share/model ./model
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
apt-cache policy docker-ce
apt-get install -y docker-ce
systemctl status docker
docker build -t registry.jetbrains.team/ml-in-space/mnist-example:0.1.$JB_SPACE_EXECUTION_NUMBER .
docker login registry.jetbrains.team --username $JB_SPACE_CLIENT_ID --password $JB_SPACE_CLIENT_SECRET
docker push registry.jetbrains.team/ml-in-space/mnist-service:0.1.$JB_SPACE_EXECUTION_NUMBER
