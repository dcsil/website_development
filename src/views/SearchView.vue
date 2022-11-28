<template>
    <div class="search">
        <div class="searchBox">
            <label>
                <input type="text" v-model="tag" class="searchInputBox" placeholder="Type any tag to search">
            </label>


            <!-- /influco.api/tag/<string:tag_str>-->
            <button class="searchButton" v-on:click="searching();">Search</button>
        </div>

        <div class="tagButtons">
            This is tag buttons div
        </div>

        <div class="filterButtons">

            <label>
                <select v-model="selected">
                    <option value="" selected disabled hidden>Choose sort by:</option>
                    <option value="Recommend">Recommend</option>
                    <option value="Followers: High to Low">Followers: High to Low</option>
                    <option value="Video Count: High to Low">Video Count: High to Low</option>
                    <option value="Like Count: High to Low">Like Count: High to Low</option>
                </select>
                <p>Currently selected: {{ selected }}</p>
            </label>
        </div>

        <h3>Total results: {{ influencers.length }}</h3>

        <div class="authorDetails">
            <div class="singleAuthor1">
                <label>Author Nickname: </label>
<!--                <p>{{ nickname }}</p>-->

                <label>Author ID: </label>
<!--                <p>{{ id }}</p>-->

                <label>Follower Count: </label>
<!--                <p>{{ followerCount }}</p>-->

                <label>Video Count: </label>
<!--                <p>{{ videoCount }}</p>-->

                <label>Like Count:</label>
<!--                <p>{{ heartCount }}</p>-->

                <label>Official site: @zachking</label>
<!--                <label>Official site: @{{ zachking }}</label>-->
<!--                <a :href="`https://www.tiktok.com/@${zachking}`">https://www.tiktok.com/@{{ zachking }}</a>-->
            </div>
            <div class="singleAuthor2">
                <label>Author Nickname: </label>
<!--                <p>{{ nickname }}</p>-->

                <label>Author ID: </label>
<!--                <p>{{ id }}</p>-->

                <label>Follower Count: </label>
<!--                <p>{{ followerCount }}</p>-->

                <label>Video Count: </label>
<!--                <p>{{ videoCount }}</p>-->

                <label>Like Count:</label>
<!--                <p>{{ heartCount }}</p>-->

                <label>Official site: @zachking</label>
<!--                <label>Official site: @{{ zachking }}</label>-->
<!--                <a :href="`https://www.tiktok.com/@${zachking}`">https://www.tiktok.com/@{{ zachking }}</a>-->
            </div>
            <div class="singleAuthor3">
                <label>Author Nickname: </label>
<!--                <p>{{ nickname }}</p>-->

                <label>Author ID: </label>
<!--                <p>{{ id }}</p>-->

                <label>Follower Count: </label>
<!--                <p>{{ followerCount }}</p>-->

                <label>Video Count: </label>
<!--                <p>{{ videoCount }}</p>-->

                <label>Like Count:</label>
<!--                <p>{{ heartCount }}</p>-->

                <label>Official site: @zachking</label>
                <p></p>
<!--                <label>Official site: @{{ zachking }}</label>-->
<!--                <a :href="`https://www.tiktok.com/@${zachking}`">https://www.tiktok.com/@{{ zachking }}</a>-->
            </div>
        </div>

        <div class="index">
            <button class="indexButton" :disabled="leftNav()" v-on:click="leftMove()">{{"<"}}</button>

            <button class="indexButton" :disabled="checkIndex(0)" v-on:click="showAuthor(0)">{{ startIndex }}</button>
            <button class="indexButton" :disabled="checkIndex(1)" v-on:click="showAuthor(1)">{{ 1 + startIndex }}</button>
            <button class="indexButton" :disabled="checkIndex(2)" v-on:click="showAuthor(2)">{{ 2 + startIndex }}</button>
            <button class="indexButton" :disabled="checkIndex(3)" v-on:click="showAuthor(3)">{{ 3 + startIndex }}</button>
            <button class="indexButton" :disabled="checkIndex(4)" v-on:click="showAuthor(4)">{{ 4 + startIndex }}</button>

            <button class="indexButton" :disabled="rightNav()" v-on:click="rightMove()">></button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            tag: "",
            influencers: ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            startIndex: 1,
            left: false,
            right: false,
            selected: "",
        }
    },
        methods: {
            searching() {
                console.log("clicked");
                // this.alert = "";
                const path = '/influco.api/tag/' + this.tag
                axios.get(path).then(response => {
                    if (response.data.status === "success") {
                        this.influencers = response.data
                    }
                }).catch(err => {
                    console.log(err);
                });
            },
            checkIndex(curr) {
                return 3 * (curr + this.startIndex) - 2 > this.influencers.length;
            },
            leftNav() {
                return this.startIndex === 1;
            },
            rightNav() {
                return this.influencers.length - (this.startIndex * 3) + 1 <= 15;
            },
            leftMove() {
                this.startIndex -= 5;
            },
            rightMove() {
                this.startIndex += 5;
            },
            showAuthor(curr) {
                // show influencers[3 * startIndex - 2, 3 * startIndex]
                // startIndex >= 1
                // startIndex <= Mth.ceil(influencers.length / 3)

                console.log("Author list has " + this.influencers.length + " authors")
                console.log("Show authors index from " + (3 * (curr + this.startIndex) - 2) + " to " + (3 * (curr + this.startIndex) + 1))
            }
        },
}
</script>

<style>
.searchBox{
    display: inline;
}

.searchInputBox{
    width: 600px;
    height: 50px;
    border-radius: 20px;
    margin-left: 10px;
}

.searchButton{
    width: 150px;
    height: 50px;
    border-radius: 15px;
    margin-left: 10px;
    border: none;
    background-color: gray;
    font-size: 23px;
}

.searchButton:hover {
    color: purple;
}

.singleAuthor1{
    margin-left: 5%;
    float: left;
    width: 28%;
    height: 300px;
}

.singleAuthor2{
    margin-left: 3%;
    float: left;
    width: 28%;
    height: 300px;
    margin-right: 5%;
}

.singleAuthor3{
    margin-left: 3%;
    float: left;
    width: 28%;
    height: 300px;
}

.index{
    width: 100%;
}

.indexButton{
    margin: 20px;
    width: 50px;
    height: 50px;
    border-radius: 15px;
}
</style>
