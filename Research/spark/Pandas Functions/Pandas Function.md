# Pandas Functions

## Drop
DataFrame.drop(labels=None, *, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

- Parameters
  - labels : single label or list-like
  - axis
  - index
  - columns
  - level
  - inplace
  - errors

## apply
DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)

- Parameters
  - func : function
  - axis : 0 or 'index' , 1 or 'columns', default 0
  - raw : bool, default False
  - result_type : 'expand', 'reduce', 'broadcast', None
  - args : tuple
  - **kwargs

## Reference
- [Reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)