from tests.test_settings import TestData


class UserTestCase(TestData):
    def test_user_exist(self):
        self.assertEqual(self.support_user.username, "support_user")
        self.assertTrue(self.support_user.groups.filter(name="Support").exists())

    def test_user_can_login(self):
        self.client.force_login(self.manager_user)
        response = self.client.get("/")
        self.assertTrue(response.context["user"].is_authenticated)
