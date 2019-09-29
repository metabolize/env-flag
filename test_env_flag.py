import os
import unittest
import uuid
from env_flag import env_flag


class EnvironGetBoolTest(unittest.TestCase):
    def test_that_env_flag_for_unset_returns_false(self):
        env_var = str(uuid.uuid4())
        self.assertIsNone(os.environ.get(env_var))
        self.assertFalse(env_flag(env_var))

    def test_that_env_flag_for_empty_string_returns_false(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = ""
        self.assertEquals(os.environ.get(env_var), "")
        self.assertFalse(env_flag(env_var))

    def test_that_env_flag_for_empty_string_returns_default(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = ""
        self.assertEquals(os.environ.get(env_var), "")
        self.assertFalse(env_flag(env_var, False))
        self.assertTrue(env_flag(env_var, True))

    def test_that_env_flag_for_string_with_spaces_returns_default(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = "     "
        self.assertEquals(os.environ.get(env_var), "     ")
        self.assertFalse(env_flag(env_var, False))
        self.assertTrue(env_flag(env_var, True))

    def test_that_env_flag_for_0_returns_false(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = "0"
        self.assertEquals(os.environ.get(env_var), "0")
        self.assertFalse(env_flag(env_var))

    def test_that_env_flag_for_0_does_not_return_default(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = "0"
        self.assertEquals(os.environ.get(env_var), "0")
        self.assertFalse(env_flag(env_var, True))

    def test_that_env_flag_for_1_returns_true(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = "1"
        self.assertEquals(os.environ.get(env_var), "1")
        self.assertTrue(env_flag(env_var))

    def test_that_env_flag_for_true_returns_true(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = "true"
        self.assertEquals(os.environ.get(env_var), "true")
        self.assertTrue(env_flag(env_var))

    def test_that_env_flag_for_any_capitalized_true_returns_true(self):
        env_var = str(uuid.uuid4())
        os.environ[env_var] = "tRue"
        self.assertEquals(os.environ.get(env_var), "tRue")
        self.assertTrue(env_flag(env_var))
