<template>
    <div class="search">
        <div class="searchBox">
            <label>
                <input type="text" v-model="tag" class="searchInputBox" placeholder="Type any tag to search">
            </label>

            <button class="searchButton" v-on:click="searching();">Search</button>
        </div>
    </div>

    <div v-if="isLoading" class="loading">
        <h1>Loading ...</h1>
    </div>

    <div v-if="isShowing" class="result">
        <div class="tagButtons">
            This is tag buttons div
        </div>

        <div class="filterButtons">

            <label>
                <select v-model="selected" v-on:click="sort()">
                    <option value="" selected disabled hidden>Choose sort by:</option>
                    <!-- TODO: <option value="Recommend">Recommend</option>-->
                    <option value="Followers: High to Low">Followers: High to Low</option>
                    <option value="Video Count: High to Low">Video Count: High to Low</option>
                    <option value="Like Count: High to Low">Like Count: High to Low</option>
                </select>
                <p>Sorted by {{ selected }}</p>
            </label>
        </div>

        <h4>Total results: {{ influencers !== 0 ? influencers.length : "Loading" }}</h4>

        <div class="authorDetails">
            <div class="singleAuthor1">
<!--                <p>{{ influencers !== 0 && influencers[showAuthorIndex] !== null ? "Author Nickname: " + influencers[showAuthorIndex]["author_stats"]["nickname"] : "" }}</p>-->
                <p v-if="flag(showAuthorIndex)">{{ "Author Nickname: " + influencers[showAuthorIndex]["author_stats"]["nickname"] }}</p>

<!--                <p>{{ influencers !== 0 && influencers[showAuthorIndex] !== null ? "Author ID: " + influencers[showAuthorIndex]["author_stats"]["id"] : "" }}</p>-->
                <p v-if="flag(showAuthorIndex)">{{ "Author ID: " + influencers[showAuthorIndex]["author_stats"]["id"] }}</p>

<!--                <p>{{ influencers !== 0 && influencers[showAuthorIndex] !== null ? "Follower Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["followerCount"] : "" }}</p>-->
                <p v-if="flag(showAuthorIndex)">{{ "Follower Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["followerCount"] }}</p>

<!--                <p>{{ influencers !== 0 && influencers[showAuthorIndex] !== null ? "Like Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["heart"] : "" }}</p>-->
                <p v-if="flag(showAuthorIndex)">{{"Like Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["heart"] }}</p>

<!--                <p >{{ influencers !== 0 && influencers[showAuthorIndex] !== null ? "Video Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["videoCount"] : "" }}</p>-->
                <p v-if="flag(showAuthorIndex)">{{"Video Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["videoCount"] }}</p>

                <label v-if="flag(showAuthorIndex)">Official site: </label>
                <a v-if="flag(showAuthorIndex)" :href="influencers[showAuthorIndex].url"> {{ influencers[showAuthorIndex]["url"] }}</a>
            </div>
            <div class="singleAuthor2">
                <p v-if="flag(showAuthorIndex + 1)">{{ "Author Nickname: " + influencers[showAuthorIndex + 1]["author_stats"]["nickname"] }}</p>

                <p v-if="flag(showAuthorIndex + 1)">{{ "Author ID: " + influencers[showAuthorIndex + 1]["author_stats"]["id"] }}</p>

                <p v-if="flag(showAuthorIndex + 1)">{{ "Follower Count: " + influencers[showAuthorIndex + 1]["author_stats"]["stats"]["followerCount"] }}</p>

                <p v-if="flag(showAuthorIndex + 1)">{{"Like Count: " + influencers[showAuthorIndex + 1]["author_stats"]["stats"]["heart"] }}</p>

                <p v-if="flag(showAuthorIndex + 1)">{{"Video Count: " + influencers[showAuthorIndex + 1]["author_stats"]["stats"]["videoCount"] }}</p>

                <label v-if="flag(showAuthorIndex + 1)">Official site: </label>
                <a v-if="flag(showAuthorIndex + 1)" :href="influencers[showAuthorIndex + 1].url"> {{ influencers[showAuthorIndex + 1]["url"] }}</a>
            </div>
            <div class="singleAuthor3">
                <p v-if="flag(showAuthorIndex + 2)">{{ "Author Nickname: " + influencers[showAuthorIndex + 2]["author_stats"]["nickname"] }}</p>

                <p v-if="flag(showAuthorIndex + 2)">{{ "Author ID: " + influencers[showAuthorIndex + 2]["author_stats"]["id"] }}</p>

                <p v-if="flag(showAuthorIndex + 2)">{{ "Follower Count: " + influencers[showAuthorIndex + 2]["author_stats"]["stats"]["followerCount"] }}</p>

                <p v-if="flag(showAuthorIndex + 2)">{{"Like Count: " + influencers[showAuthorIndex + 2]["author_stats"]["stats"]["heart"] }}</p>

                <p v-if="flag(showAuthorIndex + 2)">{{"Video Count: " + influencers[showAuthorIndex + 2]["author_stats"]["stats"]["videoCount"] }}</p>

                <label v-if="flag(showAuthorIndex + 2)">Official site: </label>
                <a v-if="flag(showAuthorIndex + 2)" :href="influencers[showAuthorIndex + 2].url"> {{ influencers[showAuthorIndex + 2]["url"] }}</a>
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
    components: {},
    data() {
        return {
            tag: "",
            influencers: 0,
            // influencers: null, => impossible for vue3 to declare null variable during rendering
            startIndex: 1,
            left: false,
            right: false,
            selected: "",
            isLoading: false,
            isShowing: false,
            showAuthorIndex: 0,
        }
    },
        methods: {
            flag(index) {
                return this.influencers[index] !== undefined;
            },
            searching() {
                this.isLoading = true;
                this.isShowing = false;
                this.startIndex = 1;
                this.showAuthorIndex = 0;

                const path = '/influco.api/tag/' + this.tag;
                console.log(path);
                axios.get(path).then(response => {
                    // TODO: what does this: if (response.data.status === "success") {} means?
                    this.influencers = response.data;
                    if (!Array.isArray(this.influencers)) {
                        throw new Error('API does not return anything for frontend')
                    }
                    this.isLoading = false;
                    this.isShowing = true;
                    console.log("Author list has " + this.influencers.length + " authors");
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
                // return this.influencers.length - (this.startIndex * 3) + 1 <= 15;
                return this.influencers.length - (Math.ceil(this.startIndex / 5) * 15) <= 0;
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
                this.showAuthorIndex = 3 * (curr + this.startIndex - 1);
                console.log("Show authors index from " + (3 * (curr + this.startIndex - 1)) + " to " + (3 * (curr + this.startIndex)))
            },
            sort() {
                if (this.selected === "") {
                    return;
                }
                if (this.selected === "Followers: High to Low") {
                    this.influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["followerCount"] - a["author_stats"]["stats"]["followerCount"];
                    });
                } else if (this.selected === "Video Count: High to Low") {
                    this.influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["videoCount"] - a["author_stats"]["stats"]["videoCount"];
                    });
                } else if (this.selected === "Like Count: High to Low") {
                    this.influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["heart"] - a["author_stats"]["stats"]["heart"];
                    });
                }
                this.startIndex = 1;
                this.showAuthorIndex = 0;
            },
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
}

.singleAuthor3{
    margin-left: 3%;
    float: left;
    width: 28%;
    height: 300px;
    margin-right: 5%;
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
