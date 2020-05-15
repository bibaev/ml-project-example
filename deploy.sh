cp /mnt/space/share/model ./model
docker build -t registry.jetbrains.team/ml-in-space/mnist-example:0.0.2 .
docker login registry.jetbrains.team --username $JB_SPACE_CLIENT_ID --password $JB_SPACE_CLIENT_SECRET
docker push registry.jetbrains.team/ml-in-space/mnist-service:0.0.2
