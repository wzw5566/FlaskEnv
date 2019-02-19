from flask import Flask

from app.apis import init_home_blue
from app.ext import init_ext

from app.settings import envs


def create_app():

    app = Flask(__name__)
    #配置使用开发环境
    app.config.from_object(envs.get('develop'))


    #初始化蓝图-路由
    init_home_blue(app)

    #初始化ext第三方类库
    init_ext(app)

    return app