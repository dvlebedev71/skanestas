# skanestas
тестовое задание для компании skanestas

1. Настроен docker compose для генерации логов в виде json файла и последующей загрузки в БД данных postgresql 
2. Commit производится после каждых 1000 (в целах сохранения быстродействия) строк загрузки (параметр задается в настройках .env), этот факт оповещается выводом на стандартый вывод.
3. Настроил "псевдомонитоинг" (прикрутить ELK или grafana+prometheus за такой короткий промежуток времени не получилось) в случае если значение полей ask_01+bid_01<105 - выводится оповещение на стандартный вывод 
4. добавленные строки в исходный файл 


        #import env
        import os
        from dotenv import load_dotenv

        #import lib for connect postgresql
        import psycopg2

        load_dotenv()

        #connect to DB
        db=os.getenv("database")
        username=os.getenv("username")
        passwd=os.getenv("passwd")
        post=os.getenv("port")
        commit=os.getenv("commit")   # count rows have to do commit
        host=os.getenv("DB_HOST")
        conn = psycopg2.connect(database=db, host=host, user=username, password=passwd, port=post)
        db=conn.cursor()


         # Insert a new row into the 'logs' table.
        def addrow(data):
            query_sql = """ insert into logs (id, stats) values (DEFAULT,'""" + data + """');"""
            db.execute( query_sql   )

         # select count row for commit
        def countrow():
            query="select * from logs;"
            db.execute(query)
            return db.rowcount

         # monitoring 
        def currentrowmonitor(data):
            y=json.loads(data)
            if y["ask_01"]+y["bid_01"]<105:
                return 1
            else:
                return 0

в конце скрипта 

        # add new message to DB
        addrow(f"{json.dumps(msg)}")
        # выполнение commit
        if countrow()%int(commit)==0:
            print("insert " + str(countrow()))
            conn.commit()
        # срабатываение мониторинга    
        if currentrowmonitor(f"{json.dumps(msg)}")==1:
            logger.info(f"{json.dumps(msg)}")


5. Запуск 
Склонируйте данный репозиторий git clone https://github.com/dvlebedev71/skanestas 
перейтите в каталог Skanestas и запустите docker compose up

