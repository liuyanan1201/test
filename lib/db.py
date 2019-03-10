import pymysql
from conf import config


def get_conn():
    conn = pymysql.connect(host = config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           password=config.db_password,
                           db=config.db,
                           charset='utf8')
    return conn

def db_query(sql):
    config.logging.debug(sql)
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    config.logging.debug(result)
    cur.close()
    conn.close()
    return result

def db_change(sql):
    config.logging.debug(sql)
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def check_user(name):
    result = db_query("select * from user where name = '%s'" % name)
    if result:
        return True
    else:
        return False

def del_user(name):
    db_change("delete from user where name = '{}'".format(name))

if __name__ == '__main__':
    print(check_user("liuliu2"))