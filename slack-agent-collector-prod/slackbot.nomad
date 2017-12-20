job "agent-collector-bot" {

  region = "us-east-1"

  datacenters = ["production"]

  group "python-bot" {
    count = 1
    task "slack-bot" {
      driver = "docker"

      config {
        image = "systeminsights/ops-agent-slackbot:latest"
      }

      env {
      "NOMAD_CLIENT_IP_ADDRESS" = "${attr.unique.network.ip-address}"
      }

    resources {
      cpu = 500
      memory = 128
    }

    }
  }
}
