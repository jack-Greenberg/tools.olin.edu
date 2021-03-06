from tests.conftest import mock_tool, mock_training


def test_new_training_prerequisite(client, db_session, current_user):
    tool = mock_tool(1, db_session, name="Lathe", category="MetalWorking")
    mock_training(1, db_session, tools=[tool], name="Fundamental Lathe Training")

    resp = client.post(
        "/api/",
        data={
            "query": """
            mutation newTraining {
                addTraining (
                    toolId: 1,
                    name: "Intermediate Lathe Training",
                    prerequisiteId: 1,
                ) {
                    name
                    tools {
                        name
                        category {
                            name
                        }
                    }
                    prerequisite {
                        name
                    }
                }
            }
        """
        },
    ).get_json()

    assert "errors" not in resp
    assert {
        "data": {
            "addTraining": {
                "name": "Intermediate Lathe Training",
                "tools": [{"name": "Lathe", "category": {"name": "MetalWorking"}}],
                "prerequisite": {"name": "Fundamental Lathe Training"},
            }
        }
    } == resp


def test_new_multitool_training(client, db_session, current_user):
    mock_tool(2, db_session, name="Bandsaw", category="Green Machines")
    mock_tool(3, db_session, name="Belt Sander", category="Green Machines")
    mock_tool(4, db_session, name="Drill Press", category="Green Machines")

    resp = client.post(
        "/api/",
        data={
            "query": """
            mutation newTraining {
                addTraining (
                    toolIds: [2, 3, 4],
                    name: "Green Shop Training",
                ) {
                    name
                    tools {
                        name
                        category {
                            name
                        }
                    }
                }
            }
        """
        },
    ).get_json()

    assert "errors" not in resp
    assert {
        "data": {
            "addTraining": {
                "name": "Green Shop Training",
                "tools": [
                    {"name": "Bandsaw", "category": {"name": "Green Machines"}},
                    {"name": "Belt Sander", "category": {"name": "Green Machines"}},
                    {"name": "Drill Press", "category": {"name": "Green Machines"}},
                ],
            }
        }
    } == resp


def test_training_queries(client, db_session, current_user):
    tool = mock_tool(1, db_session, name="Tool 1")
    tr = mock_training(1, db_session, tools=[tool], name="Beginning")
    mock_training(2, db_session, tools=[tool], prerequisite=tr, name="Intermediate")

    resp = client.post(
        "/api/",
        data={
            "query": """
                query getTraining {
                    training (
                        id: 1
                    ) {
                        id
                        name
                        tools {
                            name
                        }
                    }
                }
            """
        },
    ).get_json()

    assert "errors" not in resp
    assert {
        "data": {
            "training": {"id": "1", "name": "Beginning", "tools": [{"name": "Tool 1"}]}
        }
    } == resp

    resp = client.post(
        "/api/",
        data={
            "query": """
                query getTrainings {
                    trainings {
                        id
                        name
                        tools {
                            name
                        }
                        prerequisite {
                            id
                            name
                        }
                    }
                }
            """
        },
    ).get_json()

    assert "errors" not in resp
    assert {
        "data": {
            "trainings": [
                {
                    "id": "1",
                    "name": "Beginning",
                    "tools": [{"name": "Tool 1"}],
                    "prerequisite": None,
                },
                {
                    "id": "2",
                    "name": "Intermediate",
                    "tools": [{"name": "Tool 1"}],
                    "prerequisite": {"id": "1", "name": "Beginning"},
                },
            ]
        }
    } == resp
