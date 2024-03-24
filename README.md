This repository is used to run airflow locally using `docker compose` and run example dags that demonstrate usage of the ccd parser.

To do this:
- Clone this and the (private) `ccd-parse` repos.
- Edit the `.env` file included in this repository to reflect the local location of your `ccd-parse` clone and your local `.xml` files.
- If using the example `.xml` files in the `ccda` directory of the `ccd-parse` repo, you will have to grant airflow read access to this directory using `chmod 704`.
- Install Docker Engine, if not already installed (try `docker compose` in cli`): https://docs.docker.com/engine/install/ubuntu/
- `cd` into the root of this repository and enter `docker compose up`. `sudo` may be neccessary for all docker commands.
- Wait for necessary services to start (can check with `docker container ps -a` for success).
- In the browser, type in `http://localhost:8080` to access the airflow web UI.
- Login using username: `airflow`, password: `airflow.
- Run the desired DAG from the UI. `test_basic_extract` is provided.
- To stop airflow use `docker compose down`.
