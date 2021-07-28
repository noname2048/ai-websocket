# database (연결) > models (orm 준비) > schema (CRUD 방식, pydantic validation) > 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB url 주소의 형식은 다음과 같다.
# postgresql//[user]:[password]@[host](:[port])/[dbname]
SQLALCHEMY_DATABASE_URL = "postgresql://localhost:example@postgres:15001/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL) # 선언만, 연결은 첫 실행때 연결된다고 한다.

# engine 객체를 이용하여 세션형태로 연결한다.
# 아직은 클래스일뿐, 인스턴스 생성전까지는 실제 세션이 만들어 지지 않는다.
# 이 클래스를 사용하면, 실제 세션이 열린다. 영속성을 위해 commit도 해야한다.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() # meta 데이터를 지닌 클래스, ORM Class에서 사용해야한다.
