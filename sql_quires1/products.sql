CREATE TABLE IF NOT EXISTS products(
id SMALLSERIAL PRIMARY KEY,
category_id SMALLINT NOT NULL,
FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE,
price FLOAT,
media TEXT,
total INT,
is_published boolean default(false), name VARCHAR(20) UNIQUE NOT NULL);