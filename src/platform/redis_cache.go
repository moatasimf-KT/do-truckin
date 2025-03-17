package platform

import (
    "os"
    "github.com/go-redis/redis/v8"
    "github.com/joho/godotenv"
    "context"
)

type CacheService struct {
    client *redis.Client
}

func NewCacheService() *CacheService {
    godotenv.Load()
    
    client := redis.NewClient(&redis.Options{
        Addr:     os.Getenv("REDIS_URL"),
        Password: os.Getenv("REDIS_PASSWORD"),
        DB:       0,
    })
    
    return &CacheService{client: client}
} 