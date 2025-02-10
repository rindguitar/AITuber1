# 発言内容を生成するためのTalkerクラスを定義するプログラムです。このプログラムを編集することで、コメントがない場面での話す内容が増えます。

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
from api.openai_adapter import OpenAIAdapter
from utils.blog_utils import BlogUtils


class Talker:
    def __init__(self):
        self.talk_history: list[dict[str, str]] = []
        with open("docs/aituber_system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def chat(self, message):
        adapter = OpenAIAdapter()
        self.talk_history.append({"role": "user", "content": message})
        # 過去3やり取りまで参照する
        if len(self.talk_history) > 3:
            talk_history = self.talk_history[-3:]
        else:
            talk_history = self.talk_history
        res = adapter.chat_completions([adapter.create_message(
            "system", self.system_prompt), *talk_history])
        self.talk_history.append({"role": "assistant", "content": res})
        return res
    
    def _generate_story_elements(self):
        themes = ["冒険", "友情", "成長", "愛", "勇気", "知恵"]
        characters = ["少年", "少女", "動物", "魔法使い", "王子", "姫", "妖精"]
        settings = ["森", "城", "村", "山", "海", "空"]
        plot_elements = ["魔法のアイテム", "試練", "助けてくれる仲間", "悪役",
                         "大きな決断", "予想外の展開", "裏切り", "悲しみ", "バッドエンド"]
        
        return {
            "theme": random.choice(themes),
            "main_character": random.choice(characters),
            "setting": random.choice(settings),
            "plot_elements": random.sample(plot_elements, 3)
        }
    
    def generate_fairy_tale(self) -> str:
        elements = self._generate_story_elements()
        prompt = f"""
            以下の要素を使って、短い童話を作ってください:
            テーマ: {elements['theme']}
            主人公: {elements['main_character']}
            舞台設定: {elements['setting']}
            プロット要素: {','.join(elements['plot_elements'])}
            
            童話は300文字程度で、キャラクターの個性を反映させてください。
            """
        response = self.chat(prompt)
        print(response)
        return response
    
    def generate_about_diary(self) -> str:
        read_diary = BlogUtils()
        latest_diary = read_diary.read_latest_blog()
        prompt = f"""
            あなたは以下の日記の筆者です。
            以下の日記内の出来事について、何があったのか、どういう思いだったのか短い文を作ってください:
            日記: {latest_diary}
            
            文は200文字程度で、キャラクターの個性を反映させてください。
            """
        response = self.chat(prompt)
        print(response)
        return response

if __name__ == "__main__":
    talker = Talker()
    print(talker.generate_fairy_tale())
    print(talker.chat("さっきの童話面白かったな、君があの童話で好きなところある？"))
    print(talker.generate_about_diary())