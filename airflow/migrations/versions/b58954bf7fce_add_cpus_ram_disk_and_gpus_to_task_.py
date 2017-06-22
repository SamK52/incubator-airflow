#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""add cpus, ram, disk and gpus to task_instance

Revision ID: b58954bf7fce
Revises: 127d2bf2dfa7
Create Date: 2017-06-22 10:32:08.747633

"""

# revision identifiers, used by Alembic.
revision = 'b58954bf7fce'
down_revision = '127d2bf2dfa7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('task_instance', sa.Column('cpus', sa.Float(), nullable=True))
    op.add_column('task_instance', sa.Column('disk', sa.Float(), nullable=True))
    op.add_column('task_instance', sa.Column('gpus', sa.Float(), nullable=True))
    op.add_column('task_instance', sa.Column('ram', sa.Float(), nullable=True))


def downgrade():
    op.drop_column('task_instance', 'ram')
    op.drop_column('task_instance', 'gpus')
    op.drop_column('task_instance', 'disk')
    op.drop_column('task_instance', 'cpus')
    # ### end Alembic commands ###
