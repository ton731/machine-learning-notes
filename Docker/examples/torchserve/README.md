# TorchServe

### Start conatiner
```bash
docker run --rm -it -p 8080:8080 -p 8081:8081 -p 8082:8082 -p 7070:7070 -p 7071:7071 pytorch/torchserve:latest
```

### Create model archiver from container
```bash
# 1. run the container
docker run --rm -it -p 8080:8080 -p 8081:8081 --name test-nn -v $(pwd)/model-store:/home/model-server/model-store -v $(pwd)/test-nn:/home/model-server/test-nn pytorch/torchserve:latest

# 2. create another entry point to get in the container env
# (test-nn is the container name)
docker exec -it test-nn /bin/bash

# 3. execute torch-model-archiver command
torch-model-archiver --model-name test-nn --version 1.0 --model-file /home/model-server/test-nn/model.py --serialized-file /home/model-server/test-nn/test_model.pt --export-path /home/model-server/model-store --extra-files /home/model-server/test-nn/my_utils.py --handler /home/model-server/test-nn/test_handler.py

# 4. register the model
curl -X POST "http://localhost:8081/models?url=/home/model-server/model-store/test-nn.mar&initial_workers=1"         
```