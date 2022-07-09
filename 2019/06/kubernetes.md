labels: Draft
created: 2019-06-13T11:06
modified: 2022-06-16T10:08
place: Phuket, Thailand

# Kubernetes

## Pods

ssh:
```bash
kubectl get po -n <ns> -o wide
kubectl exec -it <NAME> bash -n <ns>
```

## Cron

Force start a cron job:
```bash
kubectl create job <job name> --from cronjob/<cron job name> -n <ns>
```

Show cron jobs:
```bash
kubectl get cronjob -n <ns>
```

Show cron job logs:
```bash
kubectl logs <cron pod name> -n <ns>
```

## Secrets

Show secret content:
```bash
kubectl get secret <secret name> -n <ns> -o jsonpath='{.data.*}' | base64 -d
```

List secrets:
```bash
kubectl get secrets -n <ns>
```
