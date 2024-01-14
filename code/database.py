import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    # текущая волна
    def get_wave(self):
        self.cur.execute("select wave from current_stats")
        return self.cur.fetchall()[0][0]

    # первоначальное заполнение таблицы
    def fill_data(self, hero_name, hero_wave, hero_weapons, hero_money):
        self.cur.execute("delete from current_stats")
        self.cur.execute("""
        insert into current_stats values (?, ?, ?, ?)
        """, (hero_name, hero_wave, hero_weapons, hero_money))
        self.conn.commit()

    # обновление данных по мере игры
    def update_data(self, hero_name, hero_wave, hero_weapons, hero_money):
        self.cur.execute("""
        update current_stats set wave = ?, weapons = ?, money = ? where hero = ?
        """, (hero_wave, hero_weapons, hero_money, hero_name))
        self.conn.commit()

    # получение всех данных из таблицы
    def get_data(self):
        self.cur.execute("select * from current_stats")
        return self.cur.fetchall()[0]

    # получение врагов из таблицы с волнами
    def get_waves(self):
        self.cur.execute("select * from waves_stats")
        return self.cur.fetchall()
