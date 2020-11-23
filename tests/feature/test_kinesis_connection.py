import boto3

def test_kinesis_connection_with_localstack():
    # currently there is an issue with localstack that is breaking the port assignments
    # so we have to use 4566
    client = boto3.client('kinesis', endpoint_url='http://localhost:4566')
    streams = client.list_streams()

    assert 'budget' in streams['StreamNames']