from flask import Flask, request
from controller import UserController


app = Flask("foody")

# todo: add Kafka


@app.route('/api/v1/keepalive', methods=['GET'])
def keep_alive():
    return "Hello, World!"


def user():
    user_controller = UserController()

    @app.route('/api/v1/user/create', methods=['POST'])
    def create_user() -> dict:
        content = request.get_json(silent=False)
        return user_controller.user_creator(content)


if __name__ == '__main__':
    user()
    app.run(host="127.0.0.1", port=5000, debug=True)
