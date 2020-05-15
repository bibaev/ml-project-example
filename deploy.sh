cp /mnt/space/share/model ./model
docker build -t registry.jetbrains.team/ml-in-space/mnist-example:0.1.$JB_SPACE_EXECUTION_NUMBER .
docker login registry.jetbrains.team --username $JB_SPACE_CLIENT_ID --password $JB_SPACE_CLIENT_SECRET
docker push registry.jetbrains.team/ml-in-space/mnist-service:0.1.$JB_SPACE_EXECUTION_NUMBER
