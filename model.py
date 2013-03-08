#!/usr/bin/env python
#coding:utf-8

import sqlite3


class Connection(object):
	"""docstring for Connetion"""
	def __init__(self, arg):
		super(Connetion, self).__init__()
		self.arg = arg
		

class DB(object):
	"""数据库操作对象基类DB"""

	def __del__(self, sql):
		raise NotImplementedError()


	def cursor(self):
		raise NotImplementedError()


	def close(self):
		raise NotImplementedError()


	def reconnect(self):
		raise NotImplementedError()


	def iter(self, query, *parameters):
		raise NotImplementedError()


	def get(self):
		raise NotImplementedError()


	def query(self, query, *parameters):
		raise NotImplementedError()


	def execute(self, query, *parameters):
		raise NotImplementedError()


	def executemany(self, query, parameters):
		raise NotImplementedError()


	def _ensure_connected(self):
		raise NotImplementedError()


	def _cursor(self):
		raise NotImplementedError()

	def _execute(self, cursor, query, parameters):
		raise NotImplementedError()


class SqliteImpl(DB):
	"""docstring for SqliteImpl"""
	def __init__(self, arg):
		super(Sqlite, self).__init__()
		self.arg = arg
		


