#!/usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'my_filter': self.my_filter,
        }

    def my_filter(self, var):
        return var + "ok"
