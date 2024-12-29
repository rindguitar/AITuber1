from src.api.openai_adapter import OpenAIAdapter

adapter = OpenAIAdapter()

with open("docs/diary_maker_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()
    
# ここをあとで一日生成機で作成する
user_prompt = """
家→ジム:冬の冷たい風に頬を撫でられながら、ジムへの道のりを辿り、それぞれの街の変化と時間の経過を思い出深く感じた。
ジム:とくになし
ジム→バー:とくになし
バー:とくになし
バー→家:冬の冷たい風が肌を突き刺した
家:窓から見える雪景色にしばし見とれた
"""

res = adapter.chat_completions([adapter.create_message(
    "system", system_prompt), adapter.create_message("user", user_prompt)])

print(res)