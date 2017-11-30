import luigi
import time


class HelloLuigi(luigi.Task):
    def run(self):
        time.sleep(60)
        print("hello")


if __name__ == '__main__':
    luigi.run()
