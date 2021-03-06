from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('develop')

# 通过程序实例实例化管理器对象
manage = Manager(app)

# 使用迁移框架
Migrate(app, db)
# 使用ｍａｎａｇｅ管理器通过迁移命令来管理数据库
manage.add_command('db', MigrateCommand)
from app import models # 一定要将模型导入关联程序


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()