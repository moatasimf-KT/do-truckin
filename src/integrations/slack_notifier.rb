require 'httparty'
require 'dotenv/load'

class SlackNotifier
  WEBHOOK_URL = ENV['SLACK_WEBHOOK_URL']

  def self.notify_deployment(environment, version)
    message = {
      text: "🚀 New deployment to #{environment}",
      blocks: [
        {
          type: "section",
          text: {
            type: "mrkdwn",
            text: "*New Deployment*\nEnvironment: #{environment}\nVersion: #{version}"
          }
        }
      ]
    }

    HTTParty.post(
      WEBHOOK_URL,
      body: message.to_json,
      headers: { 'Content-Type' => 'application/json' }
    )
  rescue => e
    Rails.logger.error("Failed to send Slack notification: #{e.message}")
  end
end 