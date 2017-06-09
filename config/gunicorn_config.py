import os

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))



bind = "127.0.0.1:8000"
workers = 6
worker_class = "sync"
threads = 2
timeout = 30
daemon = True
