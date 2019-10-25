# QUANTAXIS_PUB/SUB

![version](https://img.shields.io/pypi/v/quantaxis_pubsub.svg)

- 1.0 pub/sub模型
- 1.1 升级并完全更新至最新版本pika
- 1.2/1.3 重构
- 1.4 增加direct模型的支持, 增加routing的订阅/分发  
- 1.5 优化pubsub的模式, 规范env, 支持多机分布式/多docker container
- 1.6 增加debug tool[command line]
- 1.6.2 修改默认user为 'admin'
- 1.6.5 增加durable配置和vhost
- 1.7  优化topic 模式
- 1.8  优化 add_sub  增加多订阅!!!

## 安装

```
pip install quantaxis_pubsub
```

## 需要配置的4个 ENV 选项

- QAPUBSUB_IP 默认 'localhost'
- QAPUBSUB_PORT 默认 5672
- QAPUBSUB_USER 默认 'admin'
- QAPUBSUB_PWD  默认 'admin'

## DEBUG tool

```bash
qaps_pub --exchange {exchange} --model {direct/fanout} --routing_key {key} --content {content} --user {user} --password {password} --host {host}

qaps_sub --exchange {exchange} --model {direct/fanout} --routing_key {key} --user {user} --password {password} --host {host}
```