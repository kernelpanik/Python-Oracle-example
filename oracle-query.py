import cx_Oracle
con = cx_Oracle.connect('NICOLA/popolo@pitonedb.aosp.bo.it:1521/TESTDB')

cur = con.cursor()


results = []

cur.execute('select * from SYS.UTENTE')

for row in cur.fetchall():
    results.append(row)

# print the entire list
print(results)
