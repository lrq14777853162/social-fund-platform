# 全国公积金 / 社保缴费基数智能采集平台

全 Python 骨架版 · 微服务架构 · FastAPI + PostgreSQL + Redis + MinIO

---

## 项目简介

本项目是**全国公积金 / 社保缴费基数智能采集平台**的骨架版实现。  
目标是为各城市公积金与社保缴费基数数据的自动采集、解析、AI 抽取和发布提供一套清晰可扩展的工程基础。

当前版本以**工程结构和基础接口**为主，各服务均可本地运行，抽取逻辑使用 mock 数据，便于后续替换为真实实现。

---

## 目录结构

```text
social-fund-platform/
├── README.md
├── infrastructure/
│   ├── docker-compose.yml          # PostgreSQL + Redis + MinIO + 四个服务
│   └── sql/
│       └── init.sql                # 建表 + 初始数据
├── shared/                         # 公共 Python 模块
│   ├── __init__.py
│   ├── events.py                   # 事件常量
│   ├── middleware.py               # TraceID 中间件
│   ├── response.py                 # 统一响应结构
│   └── schemas.py                  # 公共 Pydantic Schema
└── services/
    ├── policy-admin-service/       # 地区 & 政策版本管理（端口 8001）
    ├── collector-service/          # 来源发现 & 文档抓取（端口 8002）
    ├── document-parser-service/    # 文档解析（端口 8003）
    └── ai-extract-service/         # AI 字段抽取（端口 8004）
```

---

## 服务列表与端口

| 服务 | 端口 | 主要接口 |
|------|------|----------|
| policy-admin-service | 8001 | `GET /health` · `GET /ready` · `GET /api/v1/regions` · `GET /api/v1/policies/current` |
| collector-service | 8002 | `GET /health` · `GET /ready` · `POST /api/v1/discovery/run` |
| document-parser-service | 8003 | `GET /health` · `GET /ready` · `POST /api/v1/parse/document` |
| ai-extract-service | 8004 | `GET /health` · `GET /ready` · `POST /api/v1/extract/fields` |

---

## 本地启动方式

### 前置条件

- Python 3.11+
- pip

### 1. 设置 PYTHONPATH

因为各服务依赖根目录下的 `shared/` 模块，需要将仓库根目录加入 `PYTHONPATH`：

```bash
# 在仓库根目录执行
export PYTHONPATH=$(pwd)
```

### 2. 安装依赖并启动各服务

每个服务独立安装依赖，以 **policy-admin-service** 为例：

```bash
cd services/policy-admin-service
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

其他服务依此类推（8002 / 8003 / 8004）。

### 3. 使用 Docker Compose 一键启动所有服务

```bash
cd infrastructure
docker compose up -d
```

启动后可访问：
- policy-admin-service：<http://localhost:8001/docs>
- collector-service：<http://localhost:8002/docs>
- document-parser-service：<http://localhost:8003/docs>
- ai-extract-service：<http://localhost:8004/docs>
- PostgreSQL：`localhost:5432`（用户 `sfp`，密码 `sfp_secret`，数据库 `social_fund_platform`）
- Redis：`localhost:6379`
- MinIO Console：<http://localhost:9001>（用户 `minio_admin`，密码 `minio_secret`）

---

## 初始化数据库

Docker Compose 启动时会自动执行 `infrastructure/sql/init.sql`，创建以下表并插入示例数据：

- `regions`：地区维度表（北京、上海、深圳）
- `source_documents`：原始来源文档表
- `policy_versions`：政策版本表

手动执行（如需）：

```bash
psql -h localhost -U sfp -d social_fund_platform -f infrastructure/sql/init.sql
```

---

## API 文档

各服务启动后访问 Swagger UI：

- policy-admin-service：<http://localhost:8001/docs>
- collector-service：<http://localhost:8002/docs>
- document-parser-service：<http://localhost:8003/docs>
- ai-extract-service：<http://localhost:8004/docs>

---

## 后续扩展建议

| 方向 | 建议 |
|------|------|
| 真实采集 | 在 `collector-service/crawler/adapters/` 下按城市实现 Adapter，使用 Playwright / httpx |
| 文档解析 | 在 `document-parser-service/parsers/` 子目录实现 HTML、PDF、Excel、图片解析器 |
| AI 抽取 | 在 `ai-extract-service/pipelines/` 实现规则 + LLM 混合抽取流水线 |
| 置信度评分 | 在 `ai-extract-service/scorers/` 实现字段级置信度模型 |
| 消息队列 | 引入 Kafka / RabbitMQ，服务间通过事件（见 `shared/events.py`）解耦 |
| 调度编排 | 接入 Airflow 或 Celery Beat 实现定时采集 |
| 全文检索 | 接入 Elasticsearch / OpenSearch 支持政策内容搜索 |
| 审核发布 | 增加人工审核队列与发布审批流程 |
| 监控告警 | 接入 Prometheus + Grafana + Loki |
