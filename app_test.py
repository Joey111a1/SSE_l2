from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled the \
Earth 200 million years ago"


def test_does_not_know_about_astroids():
    assert process_query("asteroids") == "Unknown"


def test_find_largest_num():
    assert process_query("Which of the following numbers is the largest: "
                         "14, 77, 89?") == "89"


def test_add_number():
    assert process_query("What is 27 plus 25?") == "52"
    assert process_query("What is 27 plus 25 plus 2?") == "54"


def test_multiply_number():
    assert process_query("What is 1 multiplied by 59?") == "59"
    assert process_query("What is 10 multiplied by 59?") == "590"


def test_both_square_and_cube():
    assert process_query("Which of the following numbers is both a square and"
                         " a cube: 1, 216, 441, 2422, 2926, 6, 306?") == "1"
    assert process_query("Which of the following numbers is both a square and"
                         " a cube: 1000, 169, 4096, 1377, "
                         "4683, 805, 9?") == "4096"


def test_subtract_number():
    assert process_query("What is 96 minus 53?") == "43"


def test_prime():
    assert process_query("Which of the following numbers are primes: "
                         "5, 93, 88, 28, 3?") == "5, 3"
    assert process_query("Which of the following numbers are primes: "
                         "8, 27, 2, 83, 49?") == "2, 83"


def test_power():
    assert process_query("What is 65 to the power of 6?") == "75418890625"
