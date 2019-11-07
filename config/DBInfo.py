# coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dbhost = "127.0.0.1"
port = '3306'
db = 'workcity'
pwd = 'root'
user = 'root'

# 数据库设置
engine = create_engine(
    "mysql+pymysql://" + user + ":" + pwd + "@" + dbhost + ":" + port + "/" + db + "?charset=utf8",
    max_overflow=20,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

SessionFactory = sessionmaker(bind=engine)
