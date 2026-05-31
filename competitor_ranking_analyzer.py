import json

def reverse_engineer_competitor_content(target_keyword, search_results_mock):
    """
    排名反推内容分析器：根据搜索引擎前排竞品，反推最佳内容框架
    支持扩展接入第三方搜索 API (SerpApi / Brave Search API)
    """
    print(f"正在分析关键词【{target_keyword}】排名前列的竞品网页结构...\n")
    
    content_brief_skeleton = {
        "Target_Keyword": target_keyword,
        "Common_Headings_Found": set(),
        "Structure_Strategy": []
    }
    
    for idx, competitor in enumerate(search_results_mock, 1):
        print(f"解析竞品 No.{idx}: {competitor['title']} (排名分数: {competitor['rank_score']})")
        # 提取核心大纲
        for heading in competitor["headings"]:
            content_brief_skeleton["Common_Headings_Found"].add(heading)
            
    # 根据反推数据制定内容策略
    content_brief_skeleton["Common_Headings_Found"] = list(content_brief_skeleton["Common_Headings_Found"])
    content_brief_skeleton["Structure_Strategy"] = [
        "1. 基础覆盖：必须包含以上竞品重合度最高的 H2 大纲结构。",
        "2. 差异化GEO优化：在前排竞品的基础上，额外增加一个【行业痛点与真实案例分析】章节，以迎合 AI 搜索的深度偏好。"
    ]
    
    return content_brief_skeleton

if __name__ == "__main__":
    # 模拟从搜索 API 获得的前排竞品数据
    mock_serp_data = [
        {
            "title": "2026最新自动化运营指南",
            "rank_score": 98,
            "headings": ["什么是自动化工作流", "常用自动化工具推荐", "如何搭建第一个脚本"]
        },
        {
            "title": "靠这套系统，我实现了全自动网站优化",
            "rank_score": 95,
            "headings": ["常用自动化工具推荐", "SEO技术指标详解", "常见错误规避"]
        }
    ]
    
    keyword = "自动化内容发布与优化"
    brief = reverse_engineer_competitor_content(keyword, mock_serp_data)
    
    print("\n====== 生成的反推内容大纲建议 ======")
    print(json.dumps(brief, ensure_ascii=False, indent=4))
