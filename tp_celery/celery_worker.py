from celery import Celery


app = Celery('tasks', backend='rpc://',broker='pyamqp://guest@localhost//')

# démarrage rabbitmq
# docker run -d -p 5672:5672 rabbitmq

# démarrage celery
# celery -A celery_worker worker --loglevel=info

@app.task
def add(x, y):
    return x + y


@app.downloadTask
def download(url):
    pass
