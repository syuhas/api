# create a dynamodb model for dog names, breeds, colors and ages

import boto3

class Dog:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('dogs')
        
    def listdogs(self):
        response = self.table.scan()
        return response['Items']
    
    def getdog(self, dog_name):
        response = self.table.get_item(Key={'name': dog_name})
        return response['Item']
    
    def createdog(self, dog):
        response = self.table.put_item(Item=dog)
        return response
    
    def updatedog(self, dog):
        response = self.table.update_item(
            Key={'name': dog['name']},
            UpdateExpression="set breed=:b, color=:c, age=:a",
            ExpressionAttributeValues={
                ':b': dog['breed'],
                ':c': dog['color'],
                ':a': dog['age']
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    
    def deletedog(self, dog_name):
        response = self.table.delete_item(Key={'name': dog_name})
        return response