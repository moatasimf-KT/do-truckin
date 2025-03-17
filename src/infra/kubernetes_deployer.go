package infra

import (
    "os"
    "github.com/slack-go/slack"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/rest"
)

type KubernetesDeployer struct {
    slackClient *slack.Client
    k8sClient   *kubernetes.Clientset
}

func NewKubernetesDeployer() *KubernetesDeployer {
    slackClient := slack.New(os.Getenv("SLACK_WEBHOOK_URL"))
    
    config, _ := rest.InClusterConfig()
    clientset, _ := kubernetes.NewForConfig(config)
    
    return &KubernetesDeployer{
        slackClient: slackClient,
        k8sClient:   clientset,
    }
} 