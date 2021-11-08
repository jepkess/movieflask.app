from app import create_app,db
from flask_script import Manager,Server #manager class that will initailize our extension and server thta will launch the application.
from app.models import User , Role,Review
from  flask_migrate import Migrate,MigrateCommand


# Creating app instance

app= create_app('production')
# app=create_app('test')
# app= create_app('production') # we pass in the production from the config options dictionary.
manager = Manager(app)
migrate = Migrate(app,db) #app instance from the app and db instance from the SQLAlchemy.
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )
if __name__ == '__main__':
    manager.run()   

#creating database
#d.b.create_all()@manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User, Role = Role )
# if __name__ == '__main__':
#     manager.run()
#User_james=User(username='james')
#User_vincent=User(username='vincent')
#db.session.add(user_james) - as storage location for the database.
#db.session.add(user_vincent)
#db.session.commit()-storing changes to the databases.

#deleting the data entries from the database steps.d
#single_user = User.query.filter_by(id = 1).first()
#single_user

#creating role and admin
#  role_admin = Role(name = 'Admin')
#  role_user = Role (name = 'User')
#  db.session.add_all([role_admin,role_user])
#  db.session.commit()

# creating users
# >>> user_james = User (username = "James Muriuki",role = role_admin)
# >>> user_christine = User(username = "Christine",role = role_user)
# >>> db.session.add_all([user_james,user_christine])
# >>> db.session.commit()
# Querying our data.
# >>> first_user = User.query.first()
# >>> first_user.role
# User Admin



