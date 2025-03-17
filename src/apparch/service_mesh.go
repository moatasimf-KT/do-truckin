package apparch

import (
    "os"
    "github.com/go-redis/redis/v8"
    "github.com/joho/godotenv"
)

type ServiceMesh struct {
    discoveryCache *redis.Client
}

func NewServiceMesh() *ServiceMesh {
    godotenv.Load()
    
    cache := redis.NewClient(&redis.Options{
        Addr:     os.Getenv("REDIS_URL"),
        Password: os.Getenv("REDIS_PASSWORD"),
    })
    
    return &ServiceMesh{
        discoveryCache: cache,
    }
} 