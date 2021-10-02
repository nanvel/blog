labels: Draft
created: 2019-06-13T11:06
modified: 2021-10-02T14:45
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
