from .utils import is_prime, is_perfect, is_armstrong, digit_sum, get_number_fact
from django.http import JsonResponse



def number_properties_view(request):
    number_str = request.GET.get("number")

    # Validate input
    if not number_str or not number_str.isdigit():
        return JsonResponse({"number": number_str, "error": "Invalid input"}, status=400)

    number = int(number_str)

    properties = []
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    fact = get_number_fact(number)

    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fact,
    }

    return JsonResponse(response_data, status=200)
