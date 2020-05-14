from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class AnimalCountByTypeView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Коровы": the_farm.breedingstock_count,
            "Молодняк до 12 месяцев": the_farm.calf_set.less_12_months_count(),
            "Молодняк после 12 месяцев": the_farm.calf_set.greater_12_months_count(),
            "Племенные быки": the_farm.breedingbull_count,
            "Нетели (беременные телки)": the_farm.breedingstock_set.pregnant_count(),
        }

        return Response(response_data, status=status.HTTP_200_OK)


class CalfToCowsRatioView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Выход телят": the_farm.calf_count / the_farm.breedingstock_count * 100,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class PastureToAnimalRatioView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Обеспеченность пастбищами (га/голову)": the_farm.total_pastures_area_in_ha
            / the_farm.total_animal_count,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class BirthWeightAverageView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Лёгкость отела (кг)": the_farm.calf_set.sum_birth_weight()
            / the_farm.calf_count,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class Predicted205DayWeightAverageView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Вес на 205 день (кг)": the_farm.calf_set.avg_205_day_predicted_weight()
        }

        return Response(response_data, status=status.HTTP_200_OK)


class CowEffectivenessAverageView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Эффективность коров (%)": the_farm.calf_set.cows_effectiveness()
        }

        return Response(response_data, status=status.HTTP_200_OK)


class CowSKTAverageView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {"СКТ коров (%)": the_farm.breedingstock_set.avg_cow_skt()}

        return Response(response_data, status=status.HTTP_200_OK)


class CowCountByYearView(APIView):
    def get(self, request):
        the_farm = request.user.farm

        response_data = {
            "Структура поголовья по возрасту (%)": {
                str(i): the_farm.breedingstock_set.get_cows_count_by_year(i)
                for i in range(2, 14)
                if i not in range(5, 10)
            }
        }

        response_data["Структура поголовья по возрасту (%)"][
            "5-9"
        ] = the_farm.breedingstock_set.get_cows_count_by_year_range(5, 9)

        return Response(response_data, status=status.HTTP_200_OK)