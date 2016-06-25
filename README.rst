==================
django-async-tasks
==================

Django application. It's a simple system to process queue task in real time.


Requirements
------------

* python 2.7
* Django 1.7 through Django 1.9
* django-redis



Install
-------

1. Download it from PyPi with ``pip install django-async-tasks``

2. Add "async_tasks" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'async_tasks',
      )

3. Configure settings

* Set setting name that defined for Redis in ``settings.CACHES``. The default used 'default' setting name. ::

      ASYNC_TASKS_REDIS_SETTING_NAME = 'default'

* Setup log path and log filename. The default used for path ``os.path.join(BASE_DIR, 'logs')`` and filename ``'async-tasks.log'``. ::

      ASYNC_TASKS_LOG_PATH = os.path.join(BASE_DIR, 'logs') # Log path
      ASYNC_TASKS_LOG_FILENAME = 'async-tasks.log' # Log filename

4. Add cron job to execute every minute::

      python manage.py django_async_tasks



Example
-------

::

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
