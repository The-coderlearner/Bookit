TERMINAL - 1 (BACKEND):
 python app.py

TERMINAL - 2 (FRONTEND):
 npm install
 npm run serve

TERMINAL - 3 (WSL) (BACKEND):
 redis-server

TERMINAL - 4 (WSL) (BACKEND):
 celery -A jobs.celery beat --loglevel=info

TERMINAL - 5 (WSL) (BACKEND):
 celery -A jobs.celery worker --loglevel=info
