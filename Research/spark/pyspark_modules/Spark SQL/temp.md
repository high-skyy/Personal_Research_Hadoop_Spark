# temp data

## header and schema
### header option
In the csv file header = true
> csv file에 가장 첫번째 row를 dataframe's column name으로 사용. (사용하지 않을 시 _c0...으로 표현됨)

### Schema
inferSchema = false
> 해당하는 모든 column들을 string type으로 받아들이겠다.
- [Reference](https://stackoverflow.com/questions/56927329/spark-option-inferschema-vs-header-true)

### multipolygons and polygons
https://gis.stackexchange.com/questions/225368/understanding-difference-between-polygon-and-multipolygon-for-shapefiles-in-qgis