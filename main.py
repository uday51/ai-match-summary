
import json
from groq import Groq
import boto3



Groq_API_Key="API_Key"



s3=boto3.client('s3',aws_access_key_id="aws_access_key",aws_secret_access_key="aws_secret_key")
def get_data():
  data=s3.get_object(
   Bucket="Bucket name",
   Key="match_data.json")
  response = data['Body'].read().decode('utf-8')
  print(response)
  return json.loads(response)
match_data=get_data()

def generate_prompt(data):
    """Create a structured prompt for the AI"""
    return f"""
    Generate a cricket match report with:
    1. A catchy headline
    2. 3-paragraph summary with key events
    3. Bullet-point key performances
    4. Tactical analysis (50 words)
    5. Imaginary player/coach quote

    Match Data:
    {json.dumps(data, indent=2)}

    Write in an engaging, journalistic style. Embed stats naturally.
    """
    
def generate_groq_report(prompt):
  client=Groq(api_key=Groq_API_Key)
  response=client.chat.completions.create(
     messages=[{"role":"user","content":prompt}],
     model="mistral-saba-24b",
     temperature=0.7,
     max_tokens=1024)
  return response.choices[0].message.content
  
  print("inside")
prompt=generate_prompt(match_data)
print(prompt)
report=generate_groq_report(prompt)
print(report)


