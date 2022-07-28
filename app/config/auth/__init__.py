from calendar import month
from datetime import datetime, timedelta
import sys
import os
import jwt
from urllib import response
# postgresql
import psycopg2

keepalive_kwargs = {
    "keepalives": 1,
    "keepalives_idle": 60,
    "keepalives_interval": 10,
    "keepalives_count": 5
}

CONNECT = None
CURSOR = None

SECRET_KEY = """MIIEoQIBAAKCAQEA4e8S3WZb2ChaSCnkSTzjh/ZHOcBt8Dx4mf7VG43wISNa1GQ9
0Mt/L3Wha0ZGTjUODs49AQw2hUOQa/4u1r8PjSJu3ARLnJFIOFBmAtHji2A6hFV5
VPMyxY4YLhldgMbI8V7cYCp7HyTXwrhZQJE/6A9sa1AiFV9HBRqt46iU1OXLraGr
UFSR1aub7TKPivZ+LG26QoDWED2Oc9mqdgPrJuLb2mN5GLbtKs4ac11bHysMmEfL
mWpwahmvUwfoijnFifgy0kYkUYE4jluB4i335Rf4aBpVjHoD32AHPenVW6cQZqK9
spGZUrr4+YsXONyhyzMszv6MV2b3np6FaQHT9wIDAQABAoH/UaKQrm7NwMzT0j9Q
vSXDEN1r3vIoxyUSbpIlbk9a9J5Rs2yE6WyeCAf4y0oZHSkOa0sZv8cp6/z9sgel
5PIkLFrEs7rZlzjnX3GtaldsYG/ktOwtawR00+0Dz6RapK0u7gfYmObAlgA59aGm
ni3daXwpMJ1Ds3U5tB5vtlKzdDjmEg6+xgxvIZMyaWyrY3tCc33XX/mgSS2xd/6b
+j8vTrHRMuwW3hEtkT/H8RUMxptyQ1kfB7I2FQDkff1Atol7KG5iZ8MV1wU48B1g
YKshNniBjEgvU3+iJWKR3ZR8QifXUuSOOzLOQsNKWUwqS6Ydp5ATNc/oLWKx6Djq
8O3RAoGBAPJLpIcOFznVEP/rkzBMUrzlZuf5GJ24KDLSAhG1h08NXwT2kQSWoJgT
+4WR/arnzIzX+oxOG1ErlC/demdZJBQ0hdmoTs/joNkBuJX6tZGf1vyOpXRiXk5p
qZcu5QdzRwLUUVfHMeO1GOX7og7QabMFCH2io/WstTZmK3dhQrZxAoGBAO62hUMr
STkPzObEZmlyzj4BJHSPGrmykfTTI30nSPXlQ9cvRILtluYDprhUmzbWEcau4aHh
Q2JHnRev/65L9VQUptCfLrUDCFSYKEdBSrbbzuhsuWygmyD+qACploOhaXbLyh8A
z7GTwcJsXp2ZZVcaFUrJCJ7/rfT+jzcXZHTnAoGAP0w1mja7KJeaDlGbrTVzM/f2
L0nq/WEb11L3yWqUA7npheFoNzumjrRBtD5Ud66AyJav1LGe/1CUMQD6Nj+aZlDm
WttWY4cDAU4qy7uobXfFcUtOvB3qpy+BZ4aPvKeH+JxA996JEQTBkWtwhdA6nNMG
ydOQY+EPojuExXY6OHECgYEAr++Z/E105Dd+/z4VdPaGhzB0W+v0+JRh+p169Iz1
uzXEcF6IEi9mHhTm1ciVtS7FXzgZWCQcc9zwLTssKJwXLmciI3SPCh44D5Etboby
uB79OlSXvTYJ36GQ1RwosM9QWZwNVhhU+z45ekBA48rg4/d3Ze0RC47J+V181E/L
XFUCgYBnOe8QLUSQnFcuiP0VGv/tT3CcBfJNTdHYXCVNZiwrxlOAD1FYPCKVWYzH
Knv30UnTl/lHe9UDSvXzvb0PYWHJUoF3v514aHrj5jhLWFll2IcJxdXMKJlwOoLD
udcLl7FJ0Ml6AOzPjiC6MgMKsKqeJ/lBZ0bZbONR48kYSyq0jw=="""

async def search_user(email):
    try:
        print('[connecting  Database]')
        CONNECT = psycopg2.connect(host='127.0.0.1', database='metronic_db',user='postgres',password='3167582', **keepalive_kwargs)
        CURSOR = CONNECT.cursor()
        query = "select * from usuarios where email='{}'".format(email)
        CURSOR.execute(query)
        recset = CURSOR.fetchall()
        if len(recset) <= 0:
            return 'email does not exist'
        else:
            return recset
    except Exception as e:
        return 'PostgreSQL Connection Fail'


async def create_user(name,last_name,email,password):
    try:
        print('[connecting  Database]')
        CONNECT = psycopg2.connect(host='127.0.0.1', database='metronic_db',user='postgres',password='3167582', **keepalive_kwargs)
        CURSOR = CONNECT.cursor()
        if await search_user(email) == 'email does not exist':
            print(name,last_name,email,password)
            dados = (name,last_name,email,password, datetime.now().strftime('%d/%m/%y'))
            query =  """ INSERT INTO usuarios (name, sobrenome, email, password, create_date) VALUES (%s,%s,%s,%s,%s)"""
            CURSOR.execute(query, dados)
            CONNECT.commit()
            return True
        return 'email already exists'
    except Exception as e:
        print('ERROR|',e)
        return e

async def expired(token):
    try:
        global SECRET_KEY
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except Exception as e:
        trace_back = sys.exc_info()[2]
        line = trace_back.tb_lineno
        print(f"{line} Error Token: {e} {line}")
        print(token)
        return False

async def descripiton_token(token):
    try:
        global SECRET_KEY
        data= jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidSignatureError:
        return False
    except Exception as e:
        trace_back = sys.exc_info()[2]
        line = trace_back.tb_lineno
        print(f"{line} Error Token: {e} {line}")
        print(token)
        return False


async def generation_token(email, password):
    global SECRET_KEY
    try:
        response = await search_user(email=email)
        payload = {
            "id": response[0][0],
            "email": response[0][2],
            "name": response[0][1],
            "acess": response[0][6],
            "exp": datetime.utcnow() + timedelta(weeks=4, days=0, minutes=0, seconds=0),
            "iat": datetime.utcnow(),
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm="HS256"
        )
    except Exception as e:
        trace_back = sys.exc_info()[2]
        line = trace_back.tb_lineno
        print("ERRO GENERATION TOKEN |LINE: {}|\n|ERROR: {}|".format(line, e))
        return 'Error Server 502'
