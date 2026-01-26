username: admin
password: admin2026
email: admin@vertical-innovations.com

playlist: https://youtube.com/playlist?list=PLZgxeXKYwDRg44_q4LQ_PDsqLO-dBm_94&si=WOML8YOZR6iO4cER

episode 4 ongoing 01.41.00



start the server

activate env:
source env/bin/activate

Activate REDIS:
docker-compose up -d

Celery worker:
celery -A vertex worker -l info

celery beat:
celery -A vertex beat --loglevel=info 