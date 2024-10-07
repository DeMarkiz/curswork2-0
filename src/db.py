import psycopg2


class DBManager:
    def __init__(self, dbname, user, password, host='127.0.0.1', port='5432'):
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port,
                options="-c client_encoding=UTF8"
            )
            self.cursor = self.conn.cursor()
            print("Подключение установлено!")
        except Exception as e:
            self.conn = None
            self.cursor = None
            print(f"Ошибка подключения: {e}")

    def create_tables(self):
        if self.cursor:
            try:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employers (
                    id SERIAL PRIMARY KEY,
                    naming VARCHAR(255) NOT NULL,
                    industry VARCHAR(255),
                    website VARCHAR(255),
                    location VARCHAR(255)
                );
                CREATE TABLE IF NOT EXISTS vacancies (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description TEXT,
                    salary INTEGER,
                    employers_id INTEGER REFERENCES employers(id) ON DELETE CASCADE,
                    data_posted DATE
                );
                """)
                self.conn.commit()
                print("Таблицы успешно созданы!")
            except Exception as e:
                print(f"Ошибка создания таблиц: {e}")
        else:
            print("Таблицы не созданы, так как соединение не установлено.")

    def add_employer(self, naming, industry, website, location):
        self.cursor.execute("""
           INSERT INTO employers (naming, industry, website, location) 
           VALUES (%s, %s, %s, %s) RETURNING id;
           """, (naming, industry, website, location))
        self.conn.commit()
        return self.cursor.fetchone()[0]  # Возвращаем ID нового работодателя

    def add_vacancy(self, title, description, salary, employers_id, data_posted):
        self.cursor.execute("""
           INSERT INTO vacancies (title, description, salary, employers_id, data_posted) 
           VALUES (%s, %s, %s, %s, %s);
           """, (title, description, salary, employers_id, data_posted))
        self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

