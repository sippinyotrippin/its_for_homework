CREATE TABLE IF NOT EXISTS orders(
id SMALLSERIAL PRIMARY KEY,
user_id SMALLINT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
data_create TIMESTAMP,
status_id SMALLINT NOT NULL,
FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE CASCADE,
invoice_id SMALLINT NOT NULL,
FOREIGN KEY (invoice_id) REFERENCES invoices(id) ON DELETE CASCADE,
);