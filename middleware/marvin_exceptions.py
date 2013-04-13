#!/usr/bin/env python
import logging

#log = logging.getLogger('middleware.exceptions')


class MiddlewareError(Exception):
    pass
    # def __init__(self, value):
    #     self.value = value
    #     if not value:
    #         raise ValueError('You deserve to be shot for not providing an '
    #                          'actionable error message mister developer')
    #     log.error(str(self))

    # def __str__(self):
    #     return "[%s: %s]" % (type(self).__name__, self.value.encode('utf-8'))
