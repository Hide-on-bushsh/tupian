export PYTHONPATH=/data/x30060150/sgl-project/sglang/python:$PYTHONPATH
ASCEND_RT_VISIBLE_DEVICES=4 python3 -m sglang.launch_server   --model-path /data/ascend-ci-share-pkking-sglang/modelscope/hub/models/BAAI/bge-m3   --host 127.0.0.1   --disable-radix-cache   --chunked-prefill-size -1   --attention-backend ascend   --is-embedding   --port 30000
