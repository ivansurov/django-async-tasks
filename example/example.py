from async_tasks.utils import delay_task, ready_task, result_task


def test(a, b):
    return a + b

def test_delay_task():
    idn = delay_task(test, **{'a': 1, 'b': 2})
    status = None
    while status not in ['SUCCESS', 'FAIL']:
        status = ready_task(idn)

    if status == 'SUCCESS':
      print result_task(idn) # return result
    else:
      print status


if __name__ == "__main__":
    test_delay_task()