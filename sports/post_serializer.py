
from email.policy import default
from rest_framework import serializers
   
# POST  
 
class PostTableOfContentSer(serializers.Serializer):  
    parentcontent_id    = serializers.IntegerField(required = False,default=0)
    description         = serializers.CharField(required=True)

# PUT

class PutTableOfContentSer(serializers.Serializer):  
    table_id            = serializers.IntegerField(required = True)
    parentcontent_id    = serializers.IntegerField(required = False,default=0)
    description         = serializers.CharField(required=True)
