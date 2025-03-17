package cloud

import (
    "os"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/credentials"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)

type AWSClient struct {
    s3Client *s3.S3
}

func NewAWSClient() *AWSClient {
    sess := session.Must(session.NewSession(&aws.Config{
        Region: aws.String("us-west-2"),
        Credentials: credentials.NewStaticCredentials(
            os.Getenv("AWS_ACCESS_KEY_ID"),
            os.Getenv("AWS_SECRET_ACCESS_KEY"),
            "",
        ),
    }))

    return &AWSClient{
        s3Client: s3.New(sess),
    }
} 