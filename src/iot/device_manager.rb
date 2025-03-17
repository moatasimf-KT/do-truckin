require 'aws-sdk-iot'
require 'dotenv/load'

class DeviceManager
  def initialize
    @iot_client = Aws::IoT::Client.new(
      access_key_id: ENV['AWS_ACCESS_KEY_ID'],
      secret_access_key: ENV['AWS_SECRET_ACCESS_KEY'],
      region: 'us-west-2'
    )
  end

  def provision_device(device_id, device_type)
    policy = create_device_policy(device_id)
    certificate = create_certificate
    attach_policy_to_certificate(policy.policy_name, certificate.certificate_arn)
    register_thing(device_id, device_type)
  end
end 