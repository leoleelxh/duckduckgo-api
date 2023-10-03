from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
from itertools import islice

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    # 从JSON请求体中获取搜索关键词
    data = request.get_json()
    search_key = data.get('searchKey')
    max_results = int(data.get('max_results', 3))
    results = []

    with DDGS() as ddgs:
        # 使用DuckDuckGo搜索关键词
        ddgs_gen = ddgs.text(search_key, safesearch='Off', timelimit='y', backend="lite")
        # 从搜索结果中获取最大结果数
        for r in islice(ddgs_gen, max_results):
            results.append(r['body'])  # 提取结果中的body字段

    # 返回一个json响应，包含仅包含body字段的搜索结果
    return jsonify({'prompt': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0')



#源代码

# from flask import Flask, request
# from duckduckgo_search import DDGS
# from itertools import islice

# app = Flask(__name__)

# @app.route('/search')
# def search():
#     # 从请求参数中获取关键词
#     keywords = request.args.get('q')
#     # 从请求参数中获取最大结果数，如果未指定，则默认为10
#     max_results = int(request.args.get('max_results', 10))
#     results = []

#     with DDGS() as ddgs:
#         # 使用DuckDuckGo搜索关键词
#         ddgs_gen = ddgs.text(keywords, safesearch='Off', timelimit='y', backend="lite")
#         # 从搜索结果中获取最大结果数
#         for r in islice(ddgs_gen, max_results):
#             results.append(r)

#     # 返回一个json响应，包含搜索结果
#     return {'results': results}

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

