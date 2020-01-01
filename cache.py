"""Implements a cache intended for drop-in memoization optimization with persistence.

Hugo O. Rivera 2020
"""

import sqlite3
import sys
from pickle import dumps, loads

SCHEMA = """CREATE TABLE cache
    (func blob, args blob, kwargs blob, results blob)
"""


class PersistentMemoizationCache(object):
    """SQL-based cache intended for drop-in memoization optimization with persistence."""

    def __init__(self, cache_name='cache', db='sqlite', caching_frequency=1):
        """Create a persistent memoization cache for function calls."""
        # TODO create probablistic structure with caching_frequency=0.5, only
        # commit ever other function call (approx.)
        if db == 'sqlite':
            db_name = f'{cache_name}.sqlitedb'
            self.conn = sqlite3.connect(db_name)

            c = self.conn.cursor()
            exists = c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='cache'""")
            if len(exists.fetchall()) == 0:
                c.execute(SCHEMA)
                self.conn.commit()


    def __del__(self):
        """Release resources as needed."""
        self.conn.close()

    def call(self, f, *args, **kwargs):
        """Wrap call to function f.

        >>> # Old, un-memoized code:
        >>> r = f(x, a=b)

        New, memoized code:

        >>> c = PersistentMemoizationCache()
        >>> r = c.call(f, x, a=b)

        The speed savings could be huge!

        WARNING: f.__name__ is used to uniquely identify functions.
        """

        func_name = f.__name__
        args_pickled = dumps(args)
        kwargs_pickled = dumps(kwargs)

        c = self.conn.cursor()
        results = c.execute("""SELECT * FROM cache WHERE func=? AND args=? AND kwargs=?""",
            (func_name, args_pickled, kwargs_pickled)
        ).fetchmany(2)
        in_cache = len(results) == 1

        if len(results) > 1:
            error = 'double-entry in cache for function {func_name}'
            print(error, file=sys.stderr)
            raise Exception(error)

        def cache_and_return(result):
            c.execute("""INSERT INTO cache VALUES (?, ?, ?, ?)""",
                    (func_name, args_pickled, kwargs_pickled, dumps(result)))
            self.conn.commit()
            return result

        if in_cache:
            row = results[0]
            _, _, _, result = row
            return loads(result)
        else:
            return cache_and_return(f(*args, **kwargs))
