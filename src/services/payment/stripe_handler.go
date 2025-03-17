package payment

import (
    "os"
    "github.com/stripe/stripe-go/v72"
    "github.com/joho/godotenv"
)

type StripeService struct {
    apiKey string
}

func NewStripeService() *StripeService {
    godotenv.Load()
    return &StripeService{
        apiKey: os.Getenv("STRIPE_API_KEY"),
    }
}

func (s *StripeService) ProcessPayment(amount int64, currency string) (*stripe.PaymentIntent, error) {
    stripe.Key = s.apiKey
    params := &stripe.PaymentIntentParams{
        Amount: stripe.Int64(amount),
        Currency: stripe.String(currency),
    }
    return stripe.PaymentIntents.New(params)
} 