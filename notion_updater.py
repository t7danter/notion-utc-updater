from notion_client import Client
from datetime import datetime, timezone  # 添加 timezone 导入
import os

# 从 GitHub Secret 中读取
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# 初始化 Notion 客户端
notion = Client(auth=NOTION_TOKEN)

# 获取当前 UTC 时间并包含时区信息
utc_now = datetime.now(timezone.utc).isoformat()

# 查询数据库中的所有页面
pages = notion.databases.query(database_id=DATABASE_ID)["results"]

# 更新每个页面的 "Now_UTC" 属性
for page in pages:
    page_id = page["id"]
    notion.pages.update(
        page_id=page_id,
        properties={
            "Now_UTC": {
                "date": {
                    "start": utc_now
                }
            }
        }
    )

print("✅ Updated Now_UTC to", utc_now)
