# Geopandas functions

## geopandas.sjoin
geopandas.sjoin(left_df, right_df, how='inner', predicate='intersects', lsuffix='left', rsuffix='right', **kwargs)

- Parameters
  - left_df, right_df : GeoDataFrames
  - how : string, default 'inner' ('left', 'right', 'inner')
  - predicate : sting, default 'intersects'