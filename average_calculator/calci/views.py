from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from environ import test_base_url, ACCESS_TOKEN
import requests
import time

windowSize = 10
NUMBERS = []


def giveMeNumbers(whatType):
    url = test_base_url + whatType
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    retries = 10

    for _ in range(retries):
        start_time = time.time()
        try:
            response = requests.get(url, headers=headers, timeout=0.5)
            response_time = time.time() - start_time

            if response.status_code == 200:
                data = response.json()
                numbers = data.get("numbers", [])
                return numbers
            elif response_time > 0.5:
                continue
        except requests.exceptions.Timeout:
            continue

    return []


class Type(APIView):
    def get(self, request, type):
        if type not in ["e", "p", "f", "r"]:
            return Response(
                {"error": "Invalid type"}, status=status.HTTP_400_BAD_REQUEST
            )

        endpoint_mapping = {
            "e": "/test/even",
            "p": "/test/prime",
            "f": "/test/fibonacci",
            "r": "/test/random",
        }

        new_numbers = giveMeNumbers(endpoint_mapping[type])
        if not new_numbers:
            return Response(
                {"error": "Failed to fetch numbers within 500ms after 10 retries"},
                status=status.HTTP_504_GATEWAY_TIMEOUT,
            )

        prev = NUMBERS.copy()
        for num in new_numbers:
            if num not in NUMBERS:
                NUMBERS.append(num)
                if len(NUMBERS) > windowSize:
                    NUMBERS.pop(0)

        curr = NUMBERS.copy()
        avg = sum(curr) / len(curr) if curr else 0

        return Response(
            {
                "numbers": new_numbers,
                "windowPrevState": prev,
                "windowCurrState": curr,
                "avg": avg,
            },
            status=status.HTTP_200_OK,
        )
