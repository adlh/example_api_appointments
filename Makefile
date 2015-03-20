clean:
	rm -f db.sqlite3

create_database:
	./manage.py syncdb --noinput
	./manage.py makemigrations --noinput
	./manage.py migrate --noinput
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

make_fixtures:
	./manage.py create_participants
	./manage.py create_appointments
	./manage.py create_options
	./manage.py create_accepted_options

all: clean create_database make_fixtures
