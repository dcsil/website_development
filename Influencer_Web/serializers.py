from rest_framework import serializers
# from Influencer_Web.models import influencer_info, user_info
from Influencer_Web.models import influencer_info


class InfluencerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = influencer_info
        fields = ('url', 'author_stats', 'video_list')
