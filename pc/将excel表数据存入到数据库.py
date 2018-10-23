import pymysql
import xlrd


class Mmp:

    def __init__(self):
        self.conn = pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = 'root123',
                db = 'tmall',
                port = 3306,
                charset = 'utf8'
            )
        self.cur = self.conn.cursor()

    def insert(self,item):
        keys,values = list(zip(*item.items()))
        keys = ','.join(list(keys))
        values = ','.join(['"%s"' % i for i in values])
        # print(keys,values)
        sql = 'insert into babycare_product({keys}) values ({values})'.format(keys=keys, values=values)
        print(sql)
        try:
            self.cur.execute(sql)
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print('error: %s' % e)
            print('log: %s' % sql)

    def excel_pul(self):
        shop = xlrd.open_workbook(r'/home/yuan/Desktop/tmall/goods_infor.xlsx')
        sheet = shop.sheets()[0]
        nrows = sheet.nrows
        ncols = sheet.ncols
        colnames = sheet.row_values(0)     
        for i in range(1,nrows):
            app = {}
            row = sheet.row_values(i)
            if row:
                for v,j in enumerate(colnames):
                    app[j] = str(row[v])
                    # print(v,j)
            self.insert(app)
mmp = Mmp()
mmp.excel_pul()      


