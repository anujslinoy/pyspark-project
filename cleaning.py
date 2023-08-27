from pyspark import SparkContext, SparkConf

# Create a SparkConf and SparkContext
conf = SparkConf().setAppName("S3FileReadExample")
sc = SparkContext(conf=conf)

# Replace 'your-s3-bucket' and 'path/to/your/file.txt' with your actual S3 bucket and file path
s3_file_path = "s3a://your-s3-bucket/path/to/your/file.txt"

# Read the file from S3
rdd = sc.textFile(s3_file_path)

# Perform operations on the RDD as needed
rdd.collect()  # Collect the RDD data into a list
# ... other RDD operations ...



rdd.sortBy("sample")