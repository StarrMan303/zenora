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


import typing
from zenora.utils.helpers import fetch, error_checker, patch, delete
from zenora.utils.endpoints import *
from zenora.base.query import Query as QueryBase
from zenora.errors import *


class Query(QueryBase):
    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    def channel(self, snowflake: int) -> typing.Dict:
        """Implementation for the REST API query to get channels.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_CHANNEL.format(snowflake),
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        error_checker(data)
        return data

    def user(self, snowflake: int) -> typing.Dict:
        """Implementation for the REST API query to get user.

        Parameters:
        snowflake: int
                The ID of a Discord user

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_USER.format(snowflake),
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        error_checker(data)
        return data

    def current_user(self) -> typing.Dict:
        """Implementation for the REST API query to get current user.

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_CURRENT_USER,
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        return data

    def modify_me(self, args: dict) -> typing.Dict:
        """Implementation for the REST API query to modify current user.

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = patch(
            BASE_URL + FETCH_CURRENT_USER,
            headers={
                "Authorization": f"{self.token_type} {self.token}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            },
            params=args,
        )
        error_checker(data)
        return data

    def leave_guild(self, snowflake: int):
        """Implementation for the REST API query to leave a guild.

        Returns:
        code: int
            Code for response status. Will return 204 on success
        """

        data = delete(
            BASE_URL + FETCH_CURRENT_USER + GET_GUILD.format(snowflake),
            headers={
                "Authorization": f"{self.token_type} {self.token}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            },
        )
        raise GuildError("Invalid Guild") if data == 404 else print("")
        return data
