



## 安装

python -m pip install grpcio grpcio-tools googleapis-common-protos


## 编译

python -m grpc_tools.protoc -I ./proto --python_out=. --grpc_python_out=. ./proto/order.proto