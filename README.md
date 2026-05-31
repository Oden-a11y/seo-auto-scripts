# seo-auto-scripts
A collection of useful scripts for web optimization and automation.
# AI-Powered SEO & Automation Workflows

这是一个面向自媒体运营者与独立开发者的 AI 自动化与 SEO/GEO（生成式引擎优化）工具箱。本项目旨在通过简单的自动化脚本与精炼的 AI 提示词（Prompts），帮助用户提升内容在主流搜索引擎及 AI 搜索（如 ChatGPT, Perplexity）中的可见度。

## 🌟 核心引擎与功能特点 (Core Engines)

本项目包含多个专为企业级环境与高级独立开发者设计的核心模块：

- ⚙️ **AI 智能体本地发布调度引擎 (`agent_workflow_dispatcher.py`)**:
  构建本地化的 AI 代理流水线。模拟将依赖第三方云端（如 Coze）的自动化工作流无缝迁移至本地（如 OpenClaw），实现高并发的内容处理、GEO 提示词注入与自建 CMS 的全自动分发调度。
- 📊 **服务器底层 SEO 蜘蛛日志分析器 (`bt_nginx_spider_analyzer.py`)**:
  突破传统 SEO 软件的限制，直接解析底层 Nginx 日志（兼容宝塔 BT Panel 格式）。精准监控 Googlebot, Bingbot 以及最新 AI 爬虫（GPTBot, Perplexity）的抓取轨迹，自动计算 Crawl Budget 消耗并诊断 404/500 路由异常。
- 🔍 **SEO/GEO 框架自动诊断系统 (`seo_framework_diagnoser.py`)**: 
  自动化解析网页源码，评估技术 SEO 指标与 AI 搜索引擎（GEO）的友好度。
- 🧠 **竞品排名反推内容分析器 (`competitor_ranking_analyzer.py`)**: 
  抓取高排名竞品大纲结构，利用内容缺口反推最优文章框架。

  - 🦞 **Lobster 多模态全链路生产引擎 (`lobster_omni_content_engine.py`)**:
  本项目中最具工程价值的调度中枢。采用 Python `asyncio` 异步高并发架构，实现五大链路一键打通：
  1. 实时抓取高排名的 SERP 受欢迎内容结构。
  2. 对接 **SEMrush API** 清洗搜索意图与关键词难度（KD）。
  3. 基于大语言模型（LLM）矩阵，根据意图自动生成【小白/专家/决策者】三维用户视角的高价值二次创作。
  4. 自动降维转换，生成高完播率的短视频分镜剧本（支持 TikTok/Reels）。
  5. 内容反编译，将文章拆解为可交互的微型工具（如 ROI 计算器、检查表）。
  *附带企业级日志监控与 Slack 工作区实时 Webhook 推送。*

## 📅 开源工程进度 (Roadmap)
- [x] 初始化项目基础设施与 MIT 许可
- [x] 上线网页 SEO/GEO 框架诊断系统与 SERP 内容反推模块
- [x] **[重大更新]** 上线本地化 AI Agent 调度中枢
- [x] **[重大更新]** 上线 Nginx 服务器底层日志抓取与 Crawl Budget 分析器
- [ ] 开发 GUI 界面，实现服务器运行状态的可视化大屏
📄 开源协议
本项目基于 MIT License 协议开源，欢迎所有人提交 Issue 或 Pull Request 参与维护！

