import multiprocessing

# Gunicorn configuration
bind = "0.0.0.0:80"  # Change the IP and port as needed
workers = multiprocessing.cpu_count() * 2 + 1
threads = 1
worker_class = "gthread"
timeout = 15
keepalive = 5

# SSL configuration
#certfile = "/etc/letsencrypt/live/easytt.rukonu.com/fullchain.pem"
#keyfile = "/etc/letsencrypt/live/easytt.rukonu.com/privkey.pem"

# Logging
accesslog = "-"  # Logs to stdout
errorlog = "-"   # Logs to stdout
loglevel = "info"
