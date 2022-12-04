<template>
    <div v-if="!isLoading">
        <img class="pic" :src="`${influencerInfo.author_stats.avatar}`" alt="Avatar" @error="imageUrlAlt">

        <div class="influencerDetail">
            <p>{{ "Official Tiktok website: " + influencerInfo.url }}</p>
            <p>{{ "Author id " + influencerInfo.author_stats.id }}</p>
            <p>{{ "Author Nickname: " + influencerInfo.author_stats.nickname }}</p>
            <p>{{ "Region: " + influencerInfo.author_stats.region }}</p>
            <p>{{ "Follower Count: " + influencerInfo.author_stats.stats.followerCount }}</p>
            <p>{{ "Like Count: " + influencerInfo.author_stats.stats.heart }}</p>
            <p>{{ "Video Count: " + influencerInfo.author_stats.stats.videoCount }}</p>
        </div>

        <div class="videoDetail">
            <p>======================ALL Video Information(Total 30 results)=======================</p>

            <div v-for="(element, index) in influencerInfo.video_list" v-bind:key="index">
                <p>{{ "Video Creat Location: " + element.create_location }}</p>
                <p>{{ "Video Description: " + element.description }}</p>
                <p>{{ "Video Label List: " + printLabel(element.label_list) }}</p>
                <p>{{ "Video Like Count: " + element.stats.diggCount }}</p>
                <p>{{ "Video View Count: " + element.stats.playCount }}</p>
                <p>{{ "Video Share Count: " + element.stats.shareCount }}</p>
                <p>==========================================================================</p>
            </div>
        </div>
    </div>

</template>

<script>
import { useRoute } from "vue-router";
import { GetInfluencer } from "../api/influencer";

export default {
    data() {
        return {
            influencerInfo: 0,
            isLoading: true,
            isLast: false,
            videoNum: 0,
        };
    },
    mounted() {
        const route = useRoute();
        const id = route.params.author_id;
        console.log(id);

        GetInfluencer(id).then(response => {
            this.influencerInfo = response.data
        })
        this.isLoading = false;
    },
    methods: {
        printLabel(lst) {
            console.log(lst);
            if (lst[0] === undefined) {
                return "No tag existed!"
            } else {
                return "#" + lst.join(' #')
            }
        },
        imageUrlAlt(event) {
            event.target.src = "https://i.pinimg.com/564x/d9/7b/bb/d97bbb08017ac2309307f0822e63d082.jpg"
        },
    }
};
</script>

<style>
.pic{
    width: 150px;
    height: 150px;
    margin-left: 10%;
    float: left;
}

.influencerDetail{
    margin-top: 180px;
    margin-left: 25%;
    text-align:left
}

.videoDetail{
    margin-left: 10%;
    text-align:left
}
</style>