from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Influencer_Web.models import ModelStats, Model, VideoListStats, VideoList, influencer_info
from Influencer_Web.serializers import InfluencerInfoSerializer

# Create your views here.

@csrf_exempt
def influencerInfoApi(request):
    if request.method == 'GET':
        influencerInfo = influencer_info.objects.all()
        influencerInfo_serializer = InfluencerInfoSerializer(influencerInfo,
                                                             many=True)
        return JsonResponse(influencerInfo_serializer.data, safe=False)
    elif request.method == 'POST':
        influencerInfo_data = JSONParser().parse(request)
        influencerInfo_serializer = InfluencerInfoSerializer(
            data=influencerInfo_data)
        if influencerInfo_serializer.is_valid():
            influencerInfo_serializer.save()
            return JsonResponse("POST successfully!", safe=False)
        return JsonResponse("POST failed!", safe=False)
    elif request.method == 'PUT':
        influencerInfo_data = JSONParser().parse(request)
        influencer = influencer_info.objects.get(
            id=influencerInfo_data['author_stats']['id'])
        influencerInfo_serializer = InfluencerInfoSerializer(
            influencer, data=influencerInfo_data)
        if influencerInfo_serializer.is_valid():
            influencerInfo_serializer.save()
            return JsonResponse("PUT successfully!", safe=False)
        return JsonResponse("PUT failed!", safe=False)
    elif request.method == 'DELETE':
        influencerInfo_data = JSONParser().parse(request)
        influencer = influencer_info.objects.get(
            id=influencerInfo_data['author_stats']['id'])
        influencerInfo_serializer = InfluencerInfoSerializer(
            influencer, data=influencerInfo_data)
        if influencerInfo_serializer.is_valid():
            influencer.delete()
            return JsonResponse("DELETE successfully!", safe=False)
        return JsonResponse("DELETE failed!", safe=False)

