from flask import Flask, request
import copy
import json

app = Flask(__name__)

data = {
    "list": [
        {
            "uuid": "test incident id 1",
            "firstName": "test first name",
            "lastName": "test last name",
            "timestamp": "The date the incident is logged",
            "files": [],
            "propertyName": "the propety name if it exists",
            "licenseNumber": "the licenses number if it exists",
            "location": {
                "address1": "test address",
                "address2": None,
                "city": "the city (add another button to show the specific address and zip code)",
                "state": "the state",
            },
            "reportSubject": "The subject/title of the incident",
            "reportDescription": "More description about it",
            "relatedReportId": [],
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
                "address1": "test address",
                "address2": None,
                "city": "test city",
                "state": "test state",
            },
            "reportSubject": "report subject 2",
            "reportDescription": "test description",
            "relatedReportId": [],
        },
    ]
}


@app.route("/sir")
@app.route("/sir/")
@app.route("/sir/<search>")
def sir_search(search=None):
    temp = copy.deepcopy(data)

    if search != None:
        temp["list"] = [
            d for d in temp["list"] if d["reportSubject"].startswith(search)
        ]

    return temp


@app.route("/add", methods=["POST"])
def sir_add():
    data["list"] = [
        {
            "uuid": "test id x",
            "firstName": "test fName",
            "lastName": "test lName",
            "timestamp": "2023/09/28 00:00:00",
            "files": [],
            "propertyName": "test property",
            "licenseNumber": "test license number",
            "location": {
                "address1": "test address",
                "address2": None,
                "city": "test city",
                "state": "test state",
            },
            "reportSubject": request.json["subject"],
            "reportDescription": "test description",
            "relatedReportId": [],
        }
    ] + data["list"]
    # data["list"].append(
    #     {
    #         "uuid": "test id x",
    #         "firstName": "test fName",
    #         "lastName": "test lName",
    #         "timestamp": "2023/09/28 00:00:00",
    #         "files": [],
    #         "propertyName": "test property",
    #         "licenseNumber": "test license number",
    #         "location": {
    #             "address1": "test address",
    #             "address2": None,
    #             "city": "test city",
    #             "state": "test state",
    #         },
    #         "reportSubject": request.json["subject"],
    #         "reportDescription": "test description",
    #         "relatedReportId": [],
    #     }
    # )
    return data


if __name__ == "__main__":
    app.run(debug=True)
