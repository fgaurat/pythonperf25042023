from celery import Celery


app = Celery('tasks', backend='rpc://',broker='pyamqp://guest@localhost//')

result = app.send_task('celery_worker.add', args=(4, 6))
result = app.send_task('celery_worker.download', args=("url"))
print("Task result:", result.get())
