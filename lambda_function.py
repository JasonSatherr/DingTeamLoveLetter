import requests
import sys
sys.path.append(".")
sys.path.append('./src/')
#This means that when I move it all into the zip, I must stuff the src folder into the zip as well
from main import main
def lambda_handler(event, context):   
    main()
    return 'lambda function completed'
