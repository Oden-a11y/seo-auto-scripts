import json
import re

def analyze_page_framework(html_content):
    """
    高级网页 SEO/GEO 框架自动诊断系统
    检查传统搜索引擎优化与生成式引擎优化（GEO）的核心指标
    """
    report = {
        "Technical_SEO": {},
        "GEO_Readiness": {},
        "Suggestions": []
    }
    
    # 1. 模拟传统 SEO 检查
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    title = title_match.group(1) if title_match else ""
    report["Technical_SEO"]["Title"] = title
    if len(title) < 10:
        report["Suggestions"].append("【传统SEO】页面标题过短，建议增加核心关键词以提升搜索权重。")
        
    h1_count = len(re.findall(r'<h1', html_content, re.IGNORECASE))
    report["Technical_SEO"]["H1_Count"] = h1_count
    if h1_count != 1:
        report["Suggestions"].append(f"【传统SEO】检测到 {h1_count} 个 H1 标签。标准框架规范要求有且仅有 1 个 H1 标签。")

    # 2. 模拟 GEO（生成式引擎优化）检查
    has_json_ld = "application/ld+json" in html_content
    report["GEO_Readiness"]["Structured_Data_JSONLD"] = has_json_ld
    if not has_json_ld:
        report["Suggestions"].append("【GEO优化】缺失 JSON-LD 结构化数据，AI 搜索引擎（如 ChatGPT/Perplexity）将难以精准提取实体信息。")
        
    # 检查是否包含高度概括的引言段落（便于LLM总结）
    has_abstract = "abstract" in html_content.lower() or "summary" in html_content.lower()
    report["GEO_Readiness"]["LLM_Summary_Friendly"] = has_abstract
    if not has_abstract:
        report["Suggestions"].append("【GEO优化】内容缺乏核心摘要段落，建议在正文前部增加结构化摘要，提升 AI 引用率。")

    return report

if __name__ == "__main__":
    # 模拟一段待诊断的网页源码
    mock_html = """
    <html>
    <head><title>基础测试页面</title></head>
    <body>
        <h1>主标题一</h1>
        <h1>错误的多重主标题</h1>
        <p>这是一篇关于自动化运营的文章，但没有结构化数据，也没有摘要。</p>
    </body>
    </html>
    """
    
    print("====== 正在启动高级 SEO/GEO 框架自动诊断系统 ======")
    diagnostic_result = analyze_page_framework(mock_html)
    print(json.dumps(diagnostic_result, ensure_ascii=False, indent=4))
