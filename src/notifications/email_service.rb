require 'sendgrid-ruby'
require 'dotenv/load'

class EmailService
  def initialize
    @client = SendGrid::API.new(api_key: ENV['SENDGRID_API_KEY'])
  end

  def send_welcome_email(user)
    mail = SendGrid::Mail.new(
      from: SendGrid::Email.new(email: 'welcome@example.com'),
      subject: 'Welcome to Our Platform!',
      to: SendGrid::Email.new(email: user.email),
      content: SendGrid::Content.new(
        type: 'text/plain',
        value: "Welcome #{user.name}! We're excited to have you onboard."
      )
    )

    @client.client.mail._('send').post(request_body: mail.to_json)
  rescue => e
    Rails.logger.error("Failed to send welcome email: #{e.message}")
  end
end 