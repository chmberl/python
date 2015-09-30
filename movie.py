# coding:utf-8

from pandas import DataFrame
import pandas as pd


headers = ['id', 'name', 'year', 'drc', 'scw',
           'act', 'genre', 'area', 'language',
           'release_dt', 'runtime', 'alias',
           'rating', 'votes']

movie = pd.read_table('~/movie.txt', sep='\t', header=None, names=headers)

frame = DataFrame(movie)
vc = frame['year'].value_counts()
vc = vc.sort_index()
vc.plot(kind='bar')
