"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from asyncio import tasks
from unicodedata import category
from psycopg2 import sql, connect, ProgrammingError
import flaskdb.var as v
from flaskdb.models import Item, Task

class DataAccess:

    # Constractor called when this class is used. 
    # It is set for hostname, port, dbname, useranme and password as parameters.
    def __init__(self, hostname, port, dbname, username, password):
        self.dburl = "host=" + hostname + " port=" + str(port) + \
                     " dbname=" + dbname + " user=" + username + \
                     " password=" + password

    # This method is used to actually issue query sql to database. 
    def execute(self, query, autocommit=True):
        with connect(self.dburl) as conn:
            if v.SHOW_SQL:
                print(query.as_string(conn))
            conn.autocommit = autocommit
            with conn.cursor() as cur:
                cur.execute(query)
                if not autocommit:
                    conn.commit()
                try:
                    return cur.fetchall()
                except ProgrammingError as e:
                    return None

    # For mainly debug, This method is used to show sql to be issued to database. 
    def show_sql(self, query):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))

    # search item data
    def search_items(self):
        query = sql.SQL("""
            SELECT * FROM \"items\"
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.user_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list
    
    def search_tasks(self):
        query = sql.SQL("""
            SELECT * FROM \"tasks\"
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        task_list = []
        for r in results:
            item = Task()
            item.id = r[0]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            task_list.append(item)
        return task_list

    # search item data by itemname
    def search_items_by_itemname(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE itemname LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.user_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list

    #カテゴリー検索
    def search_items_by_category(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE category LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Task()
            item.id = r[0]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list
    
    #タスク検索
    def search_items_by_task(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE task LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Task()
            item.id = r[0]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list
    
    #役割検索
    def search_items_by_role(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE role LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Task()
            item.id = r[0]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list
    
    #開始日付検索
    def search_items_by_start_date(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE start_date LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Task()
            item.id = r[0]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list
    
    #締切日付検索
    def search_items_by_final_date(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE final_date LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Task()
            item.id = r[0]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list




    def add_item(self, item):
        query = sql.SQL("""
            INSERT INTO \"items\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("items"),
            fields = sql.SQL(", ").join([
                sql.Identifier("itemname"),
                sql.Identifier("price")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(item.itemname),
                sql.Literal(item.price)
            ])
        )
        self.execute(query, autocommit=True)
        
    def add_task(self, task):#編集途中
        query = sql.SQL("""
            INSERT INTO \"tasks\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("tasks"),
            fields = sql.SQL(", ").join([
                sql.Identifier("category"),
                sql.Identifier("role"),
                sql.Identifier("task"),
                sql.Identifier("start_date"),
                sql.Identifier("final_date")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(task.category),
                sql.Literal(task.role),
                sql.Literal(task.task),
                sql.Literal(task.start_date),
                sql.Literal(task.final_date)
            ])
        )
        self.execute(query, autocommit=True)
