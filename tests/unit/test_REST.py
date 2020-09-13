# Zenora, a modern Python API wrapper for the Discord REST API
#
# Copyright (c) 2020 K.M Ahnaf Zamil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import zenora
import unittest
import test_config

api = zenora.RESTAPI("Token", "Bot", testing=True)


class TestRESTAPI(unittest.TestCase):

    # Just trying Travis CI
    def setUp(self):
        """Setting up the data that will be used to check the values from the API mock"""
        self.channel = {"id": 753859569859690509, "name": "general"}
        self.user = {"id": 479287754400989217, "username": "Ahnaf"}
        self.me = {"id": 479287754400989217, "username": "Ahnaf"}
        self.leave_guild = 652717519848603658

    def test_get_channel(self):
        """Testing the get_channel method with specific ID and expected data

        Note: Make sure the ID is of a server text channel because we are mocking an API response with a guild text channel response.
        """
        channel = api.get_channel(self.channel["id"])
        self.assertEqual(channel.id, self.channel["id"])
        self.assertEqual(channel.name, self.channel["name"])

    def test_get_user(self):
        """Testing the get_user method with specific ID and expected data"""
        user = api.get_user(self.user["id"])
        self.assertEqual(user.id, self.user["id"])
        self.assertEqual(user.username, self.user["username"])

    def test_get_current_user(self):
        """Testing the get_current_user method with specific ID and expected data"""
        user = api.get_current_user()
        self.assertEqual(user.id, self.me["id"])
        self.assertEqual(user.username, self.me["username"])

    def test_modify_current_user(self):
        """Testing the modify_current_user method with specific ID and expected data"""
        modified_user = api.modify_current_user({"username": "Ahnaf"})
        self.assertEqual(modified_user.id, self.me["id"])
        self.assertEqual(modified_user.username, "Ahnaf")

    def test_leave_guild(self):
        """Testing the leave_guild method with specific ID and expected data.

        Note: Your bot has to be in a guild with the specific ID as the leave_guild's ID for this test to work.
        You can change the leave_guild ID to the ID of a guild your bot is in.
        """
        left = api.leave_guild(self.leave_guild)
        self.assertEqual(left, 204)


if __name__ == "__main__":
    unittest.main()
