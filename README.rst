=====================================
django-async-tasks
=====================================

Django application. It's a simple system to process queue task in real time.


INSTALL
-----------

1. Install Redis on your server. 

2. Install and configure django-redis.

3. Install django-async-tasks

4. Add "async_tasks" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'async_tasks',
      )

5. Configure settings
  
      ASYNC_TASKS_REDIS_SETTING_NAME = 'default' # Use the name you have defined for Redis in settings.CACHES
      ASYNC_TASKS_LOG_PATH = os.path.join(BASE_DIR, 'logs') # Log path
      ASYNC_TASKS_LOG_FILENAME = 'async-tasks.log' # Log filename

6. Add task to crontab
      
      */1 * * * * python manage.py django_async_tasks



Example
-----------

```python
    from async_tasks.utils import delay_task, ready_task, result_task

    def test(a, b):
        return a + b

    def test_delay_task():

        app_idn = delay_task(test, {'a': 1, 'b': 2})

        status = ready_task(app_idn) # return response 'SUCCESS' or 'FAIL'

        if status == 'SUCCESS':
            print result_task(app_idn) # return result
        else:
            print status


    if __name__ == "__main__":
        test_delay_task()
```