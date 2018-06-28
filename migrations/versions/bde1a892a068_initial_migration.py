"""initial migration

Revision ID: bde1a892a068
Revises: 
Create Date: 2018-06-28 15:54:07.548220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bde1a892a068'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_free_category',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_thinking_category',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=32), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('signature', sa.String(length=512), nullable=True),
    sa.Column('avatar_url', sa.String(length=256), nullable=True),
    sa.Column('gender', sa.Enum('MAN', 'WOMAN'), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('tb_work_category',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_free_article',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('source', sa.String(length=64), nullable=True),
    sa.Column('digest', sa.String(length=512), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('reason', sa.String(length=256), nullable=True),
    sa.Column('free_category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['free_category_id'], ['tb_free_category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_thinking_article',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('source', sa.String(length=64), nullable=True),
    sa.Column('digest', sa.String(length=512), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('reason', sa.String(length=256), nullable=True),
    sa.Column('thinking_category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['thinking_category_id'], ['tb_thinking_category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_work_article',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('source', sa.String(length=64), nullable=True),
    sa.Column('digest', sa.String(length=512), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('reason', sa.String(length=256), nullable=True),
    sa.Column('work_category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.ForeignKeyConstraint(['work_category_id'], ['tb_work_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_free_comment',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('free_article_id', sa.Integer(), nullable=False),
    sa.Column('free_parent_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['free_article_id'], ['tb_free_article.id'], ),
    sa.ForeignKeyConstraint(['free_parent_id'], ['tb_free_comment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_thinking_comment',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('thinking_article_id', sa.Integer(), nullable=False),
    sa.Column('thinking_parent_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['thinking_article_id'], ['tb_thinking_article.id'], ),
    sa.ForeignKeyConstraint(['thinking_parent_id'], ['tb_thinking_comment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user_collection',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('free_article_id', sa.Integer(), nullable=False),
    sa.Column('work_article_id', sa.Integer(), nullable=False),
    sa.Column('thinking_article_id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['free_article_id'], ['tb_free_article.id'], ),
    sa.ForeignKeyConstraint(['thinking_article_id'], ['tb_thinking_article.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.ForeignKeyConstraint(['work_article_id'], ['tb_work_article.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'free_article_id', 'work_article_id', 'thinking_article_id')
    )
    op.create_table('tb_work_comment',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('work_article_id', sa.Integer(), nullable=False),
    sa.Column('work_parent_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.ForeignKeyConstraint(['work_article_id'], ['tb_work_article.id'], ),
    sa.ForeignKeyConstraint(['work_parent_id'], ['tb_work_comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_free_comment_like',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('free_comment_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['free_comment_id'], ['tb_free_comment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('free_comment_id', 'user_id')
    )
    op.create_table('thinking__comment_like',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('thinking_comment_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['thinking_comment_id'], ['tb_thinking_comment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('thinking_comment_id', 'user_id')
    )
    op.create_table('work__comment_like',
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('work_comment_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.ForeignKeyConstraint(['work_comment_id'], ['tb_work_comment.id'], ),
    sa.PrimaryKeyConstraint('work_comment_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work__comment_like')
    op.drop_table('thinking__comment_like')
    op.drop_table('tb_free_comment_like')
    op.drop_table('tb_work_comment')
    op.drop_table('tb_user_collection')
    op.drop_table('tb_thinking_comment')
    op.drop_table('tb_free_comment')
    op.drop_table('tb_work_article')
    op.drop_table('tb_thinking_article')
    op.drop_table('tb_free_article')
    op.drop_table('tb_work_category')
    op.drop_table('tb_user')
    op.drop_table('tb_thinking_category')
    op.drop_table('tb_free_category')
    # ### end Alembic commands ###