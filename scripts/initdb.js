var dbadmin = db.getSiblingDB('peace_db');
dbadmin.createUser(
  {
    user: "peace_user",
    pwd: "peace#secret123",
    roles: [ { role: "readWrite", db: "peace_db" }]
  }
);
