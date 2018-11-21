from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.topic import Topic
from utils import log


main = Blueprint('topic', __name__)


@main.route("/")
def index():
    ms = Topic.all()
    return render_template("topic/index.html", ms=ms)


@main.route('/<int:id>')
def detail(id):
    m = Topic.get(id)
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    log('前端传过来的form包括user_id吗:', form)
    u = current_user()
    log('does u exist?', u)
    m = Topic.new(form, user_id=u.id)
    log('id error', u)
    return redirect(url_for('.detail', id=m.id))


@main.route("/new")
def new():
    return render_template("topic/new.html")
