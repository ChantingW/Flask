from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
task = Table('task', pre_meta,
    Column('task_id', INTEGER, primary_key=True, nullable=False),
    Column('task_name', VARCHAR(length=250)),
    Column('discription', VARCHAR(length=250)),
    Column('deadline', DATE),
    Column('status', VARCHAR(length=250)),
)

task = Table('task', post_meta,
    Column('task_id', Integer, primary_key=True, nullable=False),
    Column('task_name', String(length=250)),
    Column('description', String(length=250)),
    Column('deadline', Date),
    Column('state', String(length=250)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['task'].columns['discription'].drop()
    pre_meta.tables['task'].columns['status'].drop()
    post_meta.tables['task'].columns['description'].create()
    post_meta.tables['task'].columns['state'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['task'].columns['discription'].create()
    pre_meta.tables['task'].columns['status'].create()
    post_meta.tables['task'].columns['description'].drop()
    post_meta.tables['task'].columns['state'].drop()
