To access swagger UI of postgrest, run following command
```
kubectl port-forward svc/postgrest -n postgrest 3000 3001
```
and then open http://localhost:3000