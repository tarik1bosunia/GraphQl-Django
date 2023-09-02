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

### for filtering 
```shell
pip install django-filter
```

### query
```code
query {
  allIngredients {
    edges {
      node {
        id,
        name
      }
    }
  }
}
```
```code
query {
  # You can also use `category: "CATEGORY GLOBAL ID"`
  allIngredients(name_Icontains: "e", category_Name: "Meat") {
    edges {
      node {
        name
      }
    }
  }
}
```