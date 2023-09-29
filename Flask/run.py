from flask import Flask

app = Flask(__name__)

data = {
    "list": [
        {
            "uuid": "test id 1",
            "firstName": "test fName",
            "lastName": "test lName",
            "timestamp": "2023/09/28 00:00:00",
            "files": [],
            "propertyName": "test property",
            "licenseNumber": "test license number",
            "location": {
                "address 1": "test address",
                "address 2": None,
                "City": "test city",
                "State": "test state",
            },
        },
        {
            "uuid": "test id 2",
            "firstName": "test fName",
            "lastName": "test lName",
            "timestamp": "2023/09/28 00:00:00",
            "files": [],
            "propertyName": "test property",
            "licenseNumber": "test license number",
            "location": {
                "address 1": "test address",
                "address 2": None,
                "City": "test city",
                "State": "test state",
            },
        },
    ]
}


@app.route("/sir")
def sir():
    return data


if __name__ == "__main__":
    app.run(debug=True)
