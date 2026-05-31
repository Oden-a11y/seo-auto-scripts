import re
from collections import Counter

class ServerLogSEOAnalyzer:
    """
    基于底层服务器日志的技术型 SEO 诊断矩阵
    用于分析各大搜索引擎蜘蛛的抓取行为与站点健康度 (Crawl Budget)
    """
    def __init__(self, log_path: str):
        self.log_path = log_path
        # 定义需要监控的主流搜索引擎蜘蛛与 AI 爬虫
        self.target_spiders = {
            "Googlebot": r"Googlebot",
            "Bingbot": r"bingbot",
            "Bravebot": r"Brave",
            "GPTBot": r"GPTBot", # OpenAI 抓取爬虫
            "Perplexity": r"PerplexityBot"
        }
        self.status_codes = Counter()
        self.spider_activity = Counter()

    def parse_bt_panel_nginx_logs(self, mock_log_data: list = None):
        """解析宝塔(BT Panel)标准 Nginx 访问日志"""
        print(f"正在挂载并分析服务器日志卷: {self.log_path} ...\n")
        
        # 为了演示，如果未提供真实日志文件，则使用模拟的日志流
        logs_to_process = mock_log_data if mock_log_data else []
        
        for line in logs_to_process:
            # 提取 HTTP 状态码
            status_match = re.search(r'" (\d{3}) ', line)
            if status_match:
                self.status_codes[status_match.group(1)] += 1
                
            # 识别蜘蛛活动
            for bot_name, bot_regex in self.target_spiders.items():
                if re.search(bot_regex, line, re.IGNORECASE):
                    self.spider_activity[bot_name] += 1
                    break

    def generate_audit_report(self, target_brand: str):
        """生成类 Ahrefs 风格的站点技术健康审计报告"""
        print(f"======== 【{target_brand}】底层抓取预算(Crawl Budget)审计报告 ========")
        print("\n【1】AI 与搜索引擎爬虫活跃度矩阵:")
        for bot, count in self.spider_activity.most_common():
            print(f"  ➜ {bot.ljust(15)} : 拦截到 {count} 次有效抓取")
            
        print("\n【2】服务器 HTTP 状态码健康度 (Technical Health):")
        total_requests = sum(self.status_codes.values())
        for code, count in self.status_codes.most_common():
            percentage = (count / total_requests) * 100 if total_requests > 0 else 0
            alert = " [⚠️ 需检查路由配置]" if str(code).startswith('4') or str(code).startswith('5') else ""
            print(f"  ➜ 状态 {code} : {count} 次占比 {percentage:.1f}% {alert}")

if __name__ == "__main__":
    # 模拟宝塔 Nginx 的 access.log 格式
    mock_nginx_logs = [
        '192.168.1.1 - - [30/May/2026:10:00:01 +0000] "GET /about HTTP/1.1" 200 1024 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"',
        '10.0.0.2 - - [30/May/2026:10:05:12 +0000] "GET /api/v1/data HTTP/1.1" 404 512 "-" "Mozilla/5.0 (compatible; GPTBot/1.0; +https://openai.com/gptbot)"',
        '172.16.0.5 - - [30/May/2026:10:15:33 +0000] "GET /category/seo HTTP/1.1" 200 2048 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"',
        '192.168.1.1 - - [30/May/2026:10:20:00 +0000] "GET /old-url HTTP/1.1" 301 256 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"',
        '10.0.0.3 - - [30/May/2026:10:25:44 +0000] "GET / HTTP/1.1" 500 50 "-" "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai)"'
    ]
    
    analyzer = ServerLogSEOAnalyzer(log_path="/www/wwwlogs/seo_project.log")
    analyzer.parse_bt_panel_nginx_logs(mock_nginx_logs)
    analyzer.generate_audit_report(target_brand="核心品牌项目")
