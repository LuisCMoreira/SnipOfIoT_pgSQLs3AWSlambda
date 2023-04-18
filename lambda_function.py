import psycopg2
import boto3

def lambda_handler(event, context):
    # Get the search key from the event payload
    search_name = event['search_name']
    table=event['search_table']
    
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=event['search_host'],
        port=event['search_port'],
        database=event['search_database'],
        user=event['search_user'],
        password=event['search_password']
    )
    cur = conn.cursor()
    
    # Execute the SQL query to search for the key
    cur.execute("SELECT * FROM "+ table +" WHERE name =%s",  (search_name,))
    row = cur.fetchone()
    
    # Close the database connection
    cur.close()
    conn.close()
    
    # If a row is found, save the data to an S3 bucket
    if row is not None:
        # Create an S3 client
        s3 = boto3.client('s3')
        
        # Define the S3 bucket and file name to save the data
        bucket_name = 'your_bucket_name'
        file_name = f'your_folder/{search_name}.txt'
        
        # Convert the row data to a string and save it to the S3 bucket
        row_data = ','.join(str(value) for value in row)
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=row_data.encode())
        
        # Return a success message
        return {
            'statusCode': 200,
            'body': f'Data for key {search_name} saved to S3 bucket {bucket_name} as file {file_name}'
        }
    
    # If no row is found, return an error message
    else:
        return {
            'statusCode': 404,
            'body': f'No data found for key {search_name}'
        }
