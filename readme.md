# QUANTAXIS_PUB/SUB

![version](https://img.shields.io/pypi/v/quantaxis_pubsub.svg)

- 1.0 pub/sub模型
- 1.1 升级并完全更新至最新版本pika
- 1.2/1.3 重构
- 1.4 增加direct模型的支持, 增加routing的订阅/分发  
- 1.5 优化pubsub的模式, 规范env, 支持多机分布式/多docker container


## 安装

```
pip install quantaxis_pubsub
```

## 需要配置的4个 ENV 选项

- QAPUBSUB_IP 默认 'localhost'
- QAPUBSUB_PORT 默认 5672
- QAPUBSUB_USER 默认 'guest'
- QAPUBSUB_PWD  默认 'guest'