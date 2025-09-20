import boto3
import botocore.config
import json
from datetime import datetime

def blog_generate_using_bedrock(blogtopic: str) -> str:
    # Prompt
    prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]
    """

    # Model config
    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        # Bedrock client config
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1",
            config=botocore.config.Config(
                read_timeout=300,
                retries={'max_attempts': 3}
            )
        )
        
        # Invoke model
        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId="meta.llama3-1-8b-instruct-v1:0"
        )
        
        # Parse response
        response_content = response.get('body').read()
        response_data = json.loads(response_content)  # ✅ fixed
        print(response_data)

        blog_details = response_data.get('generation', "")
        return blog_details

    except Exception as e:
        print(f"Error Generating the Blog: {e}")
        return ""


def save_blog_details_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client('s3')

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)  # ✅ fixed Body
        print("Blog saved to S3")

    except Exception as e:
        print(f"Error while saving blog to S3: {e}")


def lambda_handler(event, context):
    # Handle API Gateway event or direct invocation
    if "body" in event:
        event = json.loads(event["body"])
    
    blogtopic = event.get("blog_topic", "Default Topic")

    generate_blog = blog_generate_using_bedrock(blogtopic=blogtopic)

    if generate_blog:
        current_time = datetime.now().strftime('%H%M%S')
        s3_key = f"blog-output/{current_time}.txt"
        s3_bucket = "aws_storage_blog"
        save_blog_details_s3(s3_key, s3_bucket, generate_blog)
    else:
        print("No blog was generated")

    return {
        'statusCode': 200,
        'body': json.dumps('Blog generation completed')
    }
