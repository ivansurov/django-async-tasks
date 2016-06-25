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