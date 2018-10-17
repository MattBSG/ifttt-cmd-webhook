# [IFTTT](https://ifttt.com) Command Webhook Executor

This is a small script created in a small amount of time to allow IFTTT to send a webhook and run a system level command to do just about anything locally

## Setup
Setup is pretty simple. All you want to do is edit `webhook.py` with list seperated values (strings) of command line args in the `exec_args` list. Edit `auth_key` with a large/secure value and do not share it. You can also now change the port in `run()` to reflect a different setup if you choose. Requests to the server should be the **POST** method and have the following as json:

```json
{
  "auth": "your_auth_key"
}
```
