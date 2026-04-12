from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

engine = create_engine(
    'sqlite:///:memory:',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
    echo=True,
)
