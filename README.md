# cookbook

### graphene install - this package is used for graphql
[graphene installation doc link](https://docs.graphene-python.org/projects/django/en/latest/installation/)

```shell
pip install graphene-django
```

### load data for ingredients
```shell
python manage.py loaddata ingredients

```

### query
```code
query {
  allIngredients {
    id
    name
  }
}
```
```code
query {
  categoryByName(name: "Dairy") {
    id
    name
    ingredients {
      id
      name
    }
  }
}
```