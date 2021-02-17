def benchmark(func):
  import time

  def wrapper():
    start = time.time()
    func()
    end = time.time()
    print('Время выполнения: {} секунд.'.format(end-start))
  return wrapper

