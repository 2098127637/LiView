class rescource:
    def initialization(self):
        try:
            import sqlite3
            self.conn = sqlite3.connect('I:\\amadeus\\LiView\\userData\\sql\\spider.db')
            self.c = self.conn.cursor()
            self.result=[]
            a=0
            for i in self.information[0]:
                exec("self.c.execute('SELECT %s FROM %s ')" % (i, self.information[1][a]))
                self.result.append(self.c.fetchone()[0])
                a=a+1
        except Exception as e:
            print(e)
    def close(self):
        self.c.close()
        self.conn.close()