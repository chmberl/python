# coding:utf-8

import xml.etree.cElementTree as ET
import psycopg2

xml_file_path = '/Users/exit0/Downloads/addresslist.xml'


def parser_xml(xml_file_path, db):
    tree = ET.ElementTree(file=xml_file_path)
    states = tree.findall('CountryRegion/State')
    cursor = db.get_cursor()
    cursor.execute('select coalesce(max(id), 0) + 1 from address_province;')
    i = cursor.fetchone()[0]
    cursor.execute('select coalesce(max(id), 0) + 1 from address_city;')
    j = cursor.fetchone()[0]
    cursor.execute('select coalesce(max(id), 0) + 1 from address_district;')
    k = cursor.fetchone()[0]
    for state in states:
        name = state.attrib.get('Name')
        sql = "insert into address_province values(%s, '%s');" % (i, name)
        cursor.execute(sql)
        cities = state.findall('City')
        for c in cities:
            cname = c.attrib.get('Name')
            csql = "insert into address_city values(%s, '%s', %s);" % (
                j, cname, i)
            cursor.execute(csql)
            for r in c.findall('Region'):
                rname = r.attrib.get('Name')
                rsql = "insert into address_district values(%s, '%s', %s);" % (
                    k, rname, j
                )
                cursor.execute(rsql)
                print i, j, k
                db.get_connection().commit()
                k += 1
            j += 1
        i += 1
    db.get_connection().commit()
    db.close()


class DB(object):

    def __init__(self, db, username, password, host='127.0.0.1', port='5432'):
        self.db = db
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None

    def get_connection(self):
        if not self.conn:
            self.conn = psycopg2.connect(database=self.db,
                                         user=self.username,
                                         password=self.password,
                                         host=self.host,
                                         port=self.port)
        return self.conn

    def get_cursor(self):
        if not self.cursor:
            self.cursor = self.get_connection().cursor()
        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    db = DB('base_staging', 'staginguser', 'xKjBq7NwdFH8dq', 'localhost',
            port='5432')
    parser_xml(xml_file_path, db)
