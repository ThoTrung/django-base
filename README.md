# Recipe App API (v2) Source Code

This is the code for the second edition of the course that was released in 2022.

Course code for: [Build a Backend REST API with Python &amp; Django - Advanced](https://londonapp.dev/c2)


# Setting github action job
https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment


# Add SimpleJWT token
```
  curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "tho.nt@gmail.com", "password": "123456"}' \
  http://localhost:8880/api/token/
```


# Log changed DB
https://django-auditlog.readthedocs.io/en/latest/usage.html


#Clear docker none
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')

# Theme 
https://upmin-react.blueupcode.com/