#!/usr/bin/env python
#coding:utf-8

import sqlite3


class Connection(object):
	"""A wrapper around sqlite3 API connections."""

	def __init__(self, database):
		super(Connetion, self).__init__()
		self.datebase = database
		
	def __del__(self):
		self.close()

	def close(self):
		"""Closes this database connection."""
		if getattr(self, "_db", None) is not None:
			self._db.close()
			self._db = None

	def reconnect(self):
		"""Closes the existing database connection and re-opens it."""
		self.close()
		self._db = sqlite3.connect(self.database)
		self._db.isolation_level = None

	def get(self, query, *parameters):
		cur = self._cursor()
		try:
			self._execute(cur, query, *parameters)
			return cur.fetchone()
		finally: 
			cur.close()

	def query(self, query, size, *parameters):
		cur = self._cursor()
		try:
			self._execute(cur, query, *parameters)
			return cur.fetchmany(size)
		finally:
			cur.close()

	def execute(self, query, *parameters):
        """Executes the given query, returning the lastrowid from the query."""
        return self.execute_lastrowid(query, *parameters)

    def execute_lastrowid(self, query, *parameters):
        """Executes the given query, returning the lastrowid from the query."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def execute_rowcount(self, query, *parameters):
        """Executes the given query, returning the rowcount from the query."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            return cursor.rowcount
        finally:
            cursor.close()

    def executemany(self, query, parameters):
        """Executes the given query against all the given param sequences.

        We return the lastrowid from the query.
        """
        return self.executemany_lastrowid(query, parameters)

    def executemany_lastrowid(self, query, parameters):
        """Executes the given query against all the given param sequences.

        We return the lastrowid from the query.
        """
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def executemany_rowcount(self, query, parameters):
        """Executes the given query against all the given param sequences.

        We return the rowcount from the query.
        """
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.rowcount
        finally:
            cursor.close()

    # def _ensure_connected(self):
    #     # Mysql by default closes client connections that are idle for
    #     # 8 hours, but the client library does not report this fact until
    #     # you try to perform a query and it fails.  Protect against this
    #     # case by preemptively closing and reopening the connection
    #     # if it has been idle for too long (7 hours by default).
    #     if (self._db is None or
    #         (time.time() - self._last_use_time > self.max_idle_time)):
    #         self.reconnect()
    #     self._last_use_time = time.time()

    def _cursor(self):
        # self._ensure_connected()
        return self._db.cursor()

    def _execute(self, cursor, query, parameters):
        try:
            return cursor.execute(query, parameters)
        except OperationalError:
            logging.error("Error connecting to Sqlite3 data file on %s", self.database)
            self.close()
            raise


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
		super(SqliteImpl, self).__init__()
		self.arg = arg
		


