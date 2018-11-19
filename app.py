from flask import Flask

import config


# web framework
# web application
# __main__
app = Flask(__name__)
#加盐
app.secret_key = config.secret_key


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
app.register_blueprint(index_routes)
app.register_blueprint(topic_routes, url_prefix='/topic')
app.register_blueprint(reply_routes, url_prefix='/reply')


# 运行代码
if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
