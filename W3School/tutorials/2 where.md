## The WHERE clause is used to filter records. It is used to extract only those records that fulfill a specified condition.

## Note: The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!

## Text Fields vs. Numeric Fields
- SQL requires single quotes around text values (most database systems will also allow double quotes).
- However, numeric fields should not be enclosed in quotes:

| Operator | Description                                                                 |
| -------- | --------------------------------------------------------------------------- |
| =        | Equal                                                                       |
| >        | Greater than                                                                |
| <        | Less than                                                                   |
| >=       | Greater than or equal                                                       |
| <=       | Less than or equal                                                          |
| <>       | Not equal. Note: In some versions of SQL this operator may be written as != |
| BETWEEN  | Between a certain range                                                     |
| LIKE     | Search for a pattern                                                        |
| IN       | To specify multiple possible values for a column                            |
