# cookbook

### graphene install - this package is used for graphql

[graphene installation doc link](https://docs.graphene-python.org/projects/django/en/latest/installation/)

```shell
pip install graphene-django
```

```graphql
query {
	questionById(id:1){
    title
  }
  answerListByQuestionId(questionId:1){
    answerText
  }
}
```
```graphql
query GetQuestion($id: Int= 1){
	questionById(id:$id){
    title
  }
  answerListByQuestionId(questionId:$id){
    answerText
  }
}
```