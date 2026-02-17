from sqlalchemy import create_engine, Column, String, Integer, Numeric, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

class Portfolio(Base):
    __tablename__ = "portfolios"
    portfolio_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'))
    portfolio_name = Column(String(200))
    total_value = Column(Numeric(15, 2), default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Holding(Base):
    __tablename__ = "holdings"
    holding_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    portfolio_id = Column(UUID(as_uuid=True), ForeignKey('portfolios.portfolio_id'))
    ticker = Column(String(20), nullable=False)
    quantity = Column(Numeric(15, 6))
    average_cost = Column(Numeric(15, 6))
    created_at = Column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    portfolio_id = Column(UUID(as_uuid=True), ForeignKey('portfolios.portfolio_id'))
    ticker = Column(String(20), nullable=False)
    transaction_type = Column(String(10))
    quantity = Column(Numeric(15, 6))
    price = Column(Numeric(15, 6))
    transaction_date = Column(DateTime, default=datetime.utcnow)

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(engine)
    print("✅ Database tables created successfully!")
