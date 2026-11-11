import sender_stand_request
import data

def get_user_body(name):
    current_body = data.user_body.copy()
    current_body["firstName"] = name
    return current_body

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""



def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")


    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    assert user_table_response.text.count(str_user) == 1

    users_table_response = sender_stand_request.get_users_table()
    srt_user = user_body["firstName"] + "," + user_body["phone"] + "," + user_body["address"] + ",,," + \
               user_response.json()["authToken"]
    assert user_table_response.text.count(str_user) == 1


def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")



    def test_create_user_1_letter_in_first_name_get_success_response():
        positive_assert("A")
        

        assert user_response.status_code == 400


