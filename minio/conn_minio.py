import os

from minio import Minio

# create a connection to the object store
minio_client = Minio(
    endpoint="minio:9000",
    access_key=os.environ["MINIO_ACCESS_KEY"],
    secret_key=os.environ["MINIO_SECRET_KEY"],
    secure=False
)

# write a sample file
with open("sample.txt", "w") as f:
    f.write("This is just a sample text")

# Write data
# create a minio bucket
minio_client.make_bucket("sample-bucket")

# write the object to minio
minio_client.fput_object(
    bucket_name="sample-bucket", 
    object_name="sample-file.txt", 
    file_path="./sample.txt"
)
# Read data in bucket
minio_client.get_object("sample-bucket", "sample-file.txt").data.decode()