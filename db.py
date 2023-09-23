import pymysql

context_theme_1 = []
context_theme_2 = []
context_theme_3 = []
context_theme_4 = []
context_theme_5 = []

question_theme_1 = []
question_theme_2 = []
question_theme_3 = []
question_theme_4 = []
question_theme_5 = []

try:
    connection = pymysql.connect(
        host="138.103.55.186",
        port=3306,
        user="root",
        password="AKdj286669721389134230650+-",
        database="dtPytonXDBOT",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
    with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `qtheme`"
            
            
            cursor.execute(select_all_rows)
            
           
            # cursor.execute("SELECT * FROM `users`")
            
            rows = cursor.fetchall()
            print(rows)
            
            print(type(rows[1].get("Themes")))
            print("#" * 20)
    with connection.cursor() as cursor:
         select_all_context_theme_1 = "SELECT * FROM `questions`"
         cursor.execute(select_all_context_theme_1)
         rows2 = cursor.fetchall()
    for row in rows2:
         if row.get('Q_ID') == 1000:
              context_theme_1.append(row.get("ANSWERS")) 
              question_theme_1.append(row.get("QUESTIONS"))
         if row.get('Q_ID') == 1001:
              context_theme_2.append(row.get("ANSWERS"))
              question_theme_2.append(row.get("QUESTIONS"))
         if row.get('Q_ID') == 1002:
              context_theme_3.append(row.get("ANSWERS"))
              question_theme_3.append(row.get("QUESTIONS"))
         if row.get('Q_ID') == 1003:
              context_theme_4.append(row.get("ANSWERS"))
              question_theme_4.append(row.get("QUESTIONS"))
         if row.get('Q_ID') == 1004:
              context_theme_5.append(row.get("ANSWERS"))
              question_theme_5.append(row.get("QUESTIONS"))
    
    
    
                
         
         
            







except Exception as ex:
    print("Connection refused...")
    print(ex)
