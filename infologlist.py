# -*- coding: utf-8 -*-
from bottle import route,request
from siteglobals import env, db
from utils import *
from backend import InfoLog

@route('/list', method='GET')
def output():
	try:
		session = db.sessionmaker()
		infologs = session.query( InfoLog ).all()
		ret = env.get_template('list.html').render( infologs=infologs )
		session.close()
		return ret

	except Exception, m:
		return env.get_template('error.html').render(err_msg=str(m))
