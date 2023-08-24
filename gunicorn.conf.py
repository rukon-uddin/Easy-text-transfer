import multiprocessing

# Gunicorn configuration
bind = "192.168.0.109:8000"  # Change the IP and port as needed
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class = "gthread"
timeout = 30
keepalive = 2

# Logging
accesslog = "-"  # Logs to stdout
errorlog = "-"   # Logs to stdout
loglevel = "debug"