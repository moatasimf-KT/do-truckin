require 'aws-sdk-ecr'
require 'dotenv/load'

class ContainerRegistry
  def initialize
    @ecr = Aws::ECR::Client.new(
      access_key_id: ENV['AWS_ACCESS_KEY_ID'],
      secret_access_key: ENV['AWS_SECRET_ACCESS_KEY'],
      region: 'us-west-2'
    )
  end

  def get_image_tags(repository_name)
    @ecr.describe_images(
      repository_name: repository_name,
      filter: { tagStatus: 'TAGGED' }
    ).image_details
  end
end 