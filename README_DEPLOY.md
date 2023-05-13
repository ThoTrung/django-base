# 1. SSH to produciont
```
ssh tung@192.168.88.221
```

# 2. Turn off server 
``` 
cd tung
docker compose -f docker-compose_pro.yml down
```

# 3. Pull latest code
```
git pull
```


# 4. Build server (if something wrong)
```
docker compose -f docker-compose_pro.yml build
```

# 5. Turn on server
``` 
docker compose -f docker-compose_pro.yml up
```
