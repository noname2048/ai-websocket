from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB url 주소의 형식은 다음과 같다.
# postgresql//[user]:[password]@[host](:[port])/[dbname]
SQLALCHEMY_DATABASE_URL = "postgresql://localhost:example@postgres:15001/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL) # 선언만, 연결은 첫 실행때 연결된다고 한다.

# engine 객체를 이용하여 세션형태로 연결한다.
# 세션을 통해 명령을 내린후, commit 까지 하면 데이터베이스에서 동작한다. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() # meta 데이터를 지닌 클래스
