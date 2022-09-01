## Local DynamoDB Installation
```sh

wget https://s3.ap-south-1.amazonaws.com/dynamodb-local-mumbai/dynamodb_local_latest.tar.gz
tar -xvf dynamodb_local_latest.tar.gz
##To start the server
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
##Config aws with any dummy key_id and secret_key like
nano ~/.aws/credentials <or> aws config
```

