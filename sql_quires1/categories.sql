CREATE TABLE IF NOT EXISTS categories(
id SMALLSERIAL PRIMARY KEY,
is_published boolean default(false),
parent_id SMALLINT,
name VARCHAR(20) UNIQUE NOT NULL,
FOREIGN KEY (parent_id) REFERENCES categories(id) ON DELETE CASCADE);