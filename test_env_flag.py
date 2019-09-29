import os
import uuid
from env_flag import env_flag


def test_that_env_flag_for_unset_returns_false():
    env_var = str(uuid.uuid4())
    assert os.environ.get(env_var) is None
    assert env_flag(env_var) is False


def test_that_env_flag_for_empty_string_returns_false():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = ""
    assert os.environ.get(env_var) == ""
    assert env_flag(env_var) is False


def test_that_env_flag_for_empty_string_returns_default():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = ""
    assert os.environ.get(env_var) == ""
    assert env_flag(env_var, False) is False
    assert env_flag(env_var, True) is True


def test_that_env_flag_for_string_with_spaces_returns_default():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = "     "
    assert os.environ.get(env_var) == "     "
    assert env_flag(env_var, False) is False
    assert env_flag(env_var, True) is True


def test_that_env_flag_for_0_returns_false():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = "0"
    assert os.environ.get(env_var) == "0"
    assert env_flag(env_var) is False


def test_that_env_flag_for_0_does_not_return_default():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = "0"
    assert os.environ.get(env_var) == "0"
    assert env_flag(env_var, True) is False


def test_that_env_flag_for_1_returns_true():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = "1"
    assert os.environ.get(env_var) == "1"
    assert env_flag(env_var) is True


def test_that_env_flag_for_true_returns_true():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = "true"
    assert os.environ.get(env_var) == "true"
    assert env_flag(env_var) is True


def test_that_env_flag_for_any_capitalized_true_returns_true():
    env_var = str(uuid.uuid4())
    os.environ[env_var] = "tRue"
    assert os.environ.get(env_var) == "tRue"
    assert env_flag(env_var) is True
