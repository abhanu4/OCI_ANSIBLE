#!/bin/python

def average(lists):
    return sum(lists) / float(len(lists))


class FilterModule(object):
    ''' Query filter '''

    def filters(self):
        return {
         'average': average
          }
