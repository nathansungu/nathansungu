import pymysql


class query_values:
    def sum_Distance(self):
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()

        cursor.execute(f"SELECT SUM(Distance_KM) FROM orders")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
            total_sum = 0
        cursor.close()
        conn.close()
        return total_sum

    def cost_km(self):
       # Connect to the SQl database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()

        # Retrieve the sum of values in the specified column
        cursor.execute(f"SELECT Cost_perkm FROM `management`")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
             total_sum = 0

        cursor.close()
        conn.close()
        return total_sum

    def get_passord(self):
       # Connect to the SQl database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()

        # Retrieve the sum of values in the specified column
        cursor.execute(f"SELECT Password FROM `management`")
        Password = cursor.fetchone()[0]
        if Password is None:
             Password = 0

        cursor.close()
        conn.close()
        return Password

    def totalservice_cost(self):
        # Connect to the SQl database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()

        # Retrieve the sum of values in the specified column
        cursor.execute(f"SELECT SUM(subquery.Service_cost) AS total FROM (SELECT `vehicle expense`.`Service_cost`FROM `vehicle expense`"
                            f"LEFT JOIN `vehicle` ON `vehicle`.`Category` = `vehicle expense`.`Category`) AS subquery")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
             total_sum = 0
        cursor.close()
        conn.close()
        return total_sum
    def tires_cost(self):
        # Connect to the SQl database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()

        # Retrieve the sum of values in the specified column
        cursor.execute(f"SELECT SUM(subquery.Tires_cost) AS total FROM (SELECT `vehicle expense`.`Tires_cost`FROM `vehicle expense`"
                            f"LEFT JOIN `vehicle` ON `vehicle`.`Category` = `vehicle expense`.`Category`) AS subquery")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
             total_sum = 0
        cursor.close()
        conn.close()
        return total_sum
    def staff_totalpay(self):
        # Connect to  SQL database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        cursor.execute(f"SELECT SUM(subquery.Amount) AS total FROM (SELECT `workers pay`.`Amount`FROM `office staff`"
                           f"LEFT JOIN `workers pay` ON `office staff`.`Category` = `workers pay`.`Category`) AS subquery")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
            total_sum = 0

        cursor.close()
        conn.close()

        return total_sum

    def loaders_totalpay(self):
        # Connect to the SQL database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        cursor.execute(f"SELECT SUM(subquery.Amount) AS total FROM (SELECT `workers pay`.`Amount`FROM `loaders`"
                       f"LEFT JOIN `workers pay` ON `loaders`.`Category` = `workers pay`.`Category`) AS subquery")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
            total_sum = 0

        cursor.close()
        conn.close()
        return total_sum

    def drivers_totalpay(self):
        # Connect to the SQL database
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        cursor.execute(f"SELECT SUM(subquery.Amount) AS total FROM (SELECT `workers pay`.`Amount`FROM `drivers`"
                       f"LEFT JOIN `workers pay` ON `drivers`.`Category` = `workers pay`.`Category`) AS subquery")
        total_sum = cursor.fetchone()[0]
        if total_sum is None:
            total_sum = 0

        cursor.close()
        conn.close()
        return total_sum