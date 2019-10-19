# Docker starter kit for Django development

This is the way I learned to do Django development with docker.

Images available:

`python3.7.4` (could be modified to match your virtual environment)

`postgres:11`

`pgadmin4`

Steps:

- Create your python virtual environment to work with. `python3 -m venv ${NAME_OF_YOUR VENV}`
- Enter your env dir and activate it `cd ${NAME_OF_YOUR VENV} && source bin/activate`
- Install Django and needed third part dependencies.
- Freeze your dependencies in a `requirements.txt` file `pip freeze > requirements.txt`
- Set up you environments variables in the `.env` file.
- Copy the docker related files to your project. `docker-compose.yml`, `.dockerignore` and `Dockerfile`
- Modify image versions as needed.
- Run with make commands available through the provided `Makefile`.

NOTE on python docker image.

The default command for the container is set to run `makemigration`, `migrate` and `runserver` Django commands by default.

In order to use for development and apply changes to your models, replace command defined with the `runserver` command in order to create and run migrations manually.

`makemigration` and `migrate` result files should be againts the container. Since volume is mapped your migrations files will appear in your local folder for git version control as usual.

`make db-make-migrations` - Creates new migrations in the container.

`db-migrate` - Commit migrations to the DB.
