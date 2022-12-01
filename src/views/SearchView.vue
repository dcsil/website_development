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
        <div class="tagButtonsList">
            <button class="allButton" v-on:click="showAll()">{{ "ALL" }}</button>

            <button class="allButton" :disabled="leftNavTag()" v-on:click="leftMoveTag()">{{ "<" }}</button>

            <button class="tagButtons" v-for="item in (tagFrequencyAll().slice(startIndexTag, startIndexTag + 5))" v-bind:key="item[0]" v-on:click="filterTag(item[0])">{{ "#" + item[0] }}</button>

            <button class="allButton" :disabled="rightNavTag()" v-on:click="rightMoveTag()">></button>
        </div>

        <div class="filterButtons">

            <label>
                <select v-model="selected" v-on:click="sort()">
                    <p>Choose order here: </p>
<!--                    <option value="" selected disabled hidden>Choose sort by:</option>-->
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
                <div v-if="flag(showAuthorIndex)" class="sameBorder">
                    <p>{{ "Author Nickname: " + influencers[showAuthorIndex]["author_stats"]["nickname"] }}</p>

                    <p>{{ "Author ID: " + influencers[showAuthorIndex]["author_stats"]["id"] }}</p>

                    <p>{{ "Follower Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["followerCount"] }}</p>

                    <p>{{ "Like Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["heart"] }}</p>

                    <p>{{ "Video Count: " + influencers[showAuthorIndex]["author_stats"]["stats"]["videoCount"] }}</p>

                    <p>{{ "Official site: " }}</p>
                    <a :href="influencers[showAuthorIndex].url"> {{ influencers[showAuthorIndex]["url"] }}</a>

                    <p>{{ "Popular tags: " }}</p>
                    <button class="tagButton" v-for="item in tagFrequency(influencers[showAuthorIndex])" v-bind:key="item" v-on:click="filterTag(item)">{{ "#" + item }}</button>

                    <p>{{ "Influencer Detail: " }}</p>
                    <a :href="`/detail/${influencers[showAuthorIndex].author_stats.id}`"> {{ "@" + influencers[showAuthorIndex].author_stats.id }}</a>
                </div>
            </div>
            <div class="singleAuthor2">
                <div v-if="flag(showAuthorIndex + 1)" class="sameBorder">
                    <p>{{ "Author Nickname: " + influencers[showAuthorIndex + 1]["author_stats"]["nickname"] }}</p>

                    <p>{{ "Author ID: " + influencers[showAuthorIndex + 1]["author_stats"]["id"] }}</p>

                    <p>{{ "Follower Count: " + influencers[showAuthorIndex + 1]["author_stats"]["stats"]["followerCount"] }}</p>

                    <p>{{ "Like Count: " + influencers[showAuthorIndex + 1]["author_stats"]["stats"]["heart"] }}</p>

                    <p>{{ "Video Count: " + influencers[showAuthorIndex + 1]["author_stats"]["stats"]["videoCount"] }}</p>

                    <p>{{ "Official site: " }}</p>
                    <a :href="influencers[showAuthorIndex + 1].url"> {{ influencers[showAuthorIndex + 1]["url"] }}</a>

                    <p>{{ "Popular tags: " }}</p>
                    <button class="tagButton" v-for="item in tagFrequency(influencers[showAuthorIndex + 1])" v-bind:key="item" v-on:click="filterTag(item)">{{ "#" + item }}</button>

                    <p>{{ "Influencer Detail: " }}</p>
                    <a :href="`/detail/${influencers[showAuthorIndex + 1].author_stats.id}`"> {{ "@" + influencers[showAuthorIndex + 1].author_stats.id }}</a>
                </div>
            </div>

            <div class="singleAuthor3">
                <div v-if="flag(showAuthorIndex + 2)" class="sameBorder">
                    <p>{{ "Author Nickname: " + influencers[showAuthorIndex + 2]["author_stats"]["nickname"] }}</p>

                    <p>{{ "Author ID: " + influencers[showAuthorIndex + 2]["author_stats"]["id"] }}</p>

                    <p>{{ "Follower Count: " + influencers[showAuthorIndex + 2]["author_stats"]["stats"]["followerCount"] }}</p>

                    <p>{{ "Like Count: " + influencers[showAuthorIndex + 2]["author_stats"]["stats"]["heart"] }}</p>

                    <p>{{ "Video Count: " + influencers[showAuthorIndex + 2]["author_stats"]["stats"]["videoCount"] }}</p>

                    <p>{{ "Official site: " }}</p>
                    <a :href="influencers[showAuthorIndex + 2].url"> {{ influencers[showAuthorIndex + 2]["url"] }}</a>

                    <p>{{ "Popular tags: " }}</p>
                    <button class="tagButton" v-for="item in tagFrequency(influencers[showAuthorIndex + 2])" v-bind:key="item" v-on:click="filterTag(item)">{{ "#" + item }}</button>

                    <p>{{ "Influencer Detail: " }}</p>
                    <a :href="`/detail/${influencers[showAuthorIndex + 2].author_stats.id}`"> {{ "@" + influencers[showAuthorIndex + 2].author_stats.id }}</a>
                </div>
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
            copy_influencers: 0,
            // influencers: null, => impossible for vue3 to declare null variable during rendering
            startIndex: 1,
            left: false,
            right: false,
            selected: "",
            isLoading: false,
            isShowing: false,
            showAuthorIndex: 0,
            startIndexTag: 0,
            allTagsLength: 0,
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
                    this.copy_influencers = this.influencers;
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
                    this.copy_influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["followerCount"] - a["author_stats"]["stats"]["followerCount"];
                    });
                } else if (this.selected === "Video Count: High to Low") {
                    this.influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["videoCount"] - a["author_stats"]["stats"]["videoCount"];
                    });
                    this.copy_influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["videoCount"] - a["author_stats"]["stats"]["videoCount"];
                    });
                } else if (this.selected === "Like Count: High to Low") {
                    this.influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["heart"] - a["author_stats"]["stats"]["heart"];
                    });
                    this.copy_influencers.sort(function(a, b) {
                        return b["author_stats"]["stats"]["heart"] - a["author_stats"]["stats"]["heart"];
                    });
                }
                this.startIndex = 1;
                this.showAuthorIndex = 0;
            },
            tagFrequency(influencer) {
                let tag_obj = {};
                for (let i = 0; i < influencer["video_list"].length; i++) {
                    // console.log(influencer["video_list"][i]["label_list"]);
                    for (let j = 0; j < influencer["video_list"][i]["label_list"].length; j++) {
                        // console.log(influencer["video_list"][i]["label_list"][j]);
                        if (!(influencer["video_list"][i]["label_list"][j] in tag_obj)) {
                            tag_obj[influencer["video_list"][i]["label_list"][j]] = 1;
                        } else {
                            tag_obj[influencer["video_list"][i]["label_list"][j]] += 1;
                        }
                    }
                }
                // console.log(tag_obj);
                let tag_arr = [];
                for (let element in tag_obj) {
                    tag_arr.push([element, tag_obj[element]]);
                }
                tag_arr.sort(function(a, b) {
                    return b[1] - a[1];
                })
                // console.log(tag_arr);
                if (tag_arr.length >= 3) {
                    return [tag_arr[0][0], tag_arr[1][0], tag_arr[2][0]]
                } else if (tag_arr.length === 2) {
                    return [tag_arr[0][0], tag_arr[1][0]]
                } else if (tag_arr.length === 1) {
                    return [tag_arr[0][0]]
                }
            },
            tagFrequencyAll() {
                let tag_obj = {};
                for (let k = 0; k < this.copy_influencers.length; k++) {
                    let influencer = this.copy_influencers[k];
                    for (let i = 0; i < influencer["video_list"].length; i++) {
                        for (let j = 0; j < influencer["video_list"][i]["label_list"].length; j++) {
                            if (!(influencer["video_list"][i]["label_list"][j] in tag_obj)) {
                                tag_obj[influencer["video_list"][i]["label_list"][j]] = 1;
                            } else {
                                tag_obj[influencer["video_list"][i]["label_list"][j]] += 1;
                            }
                        }
                    }
                }

                let tag_arr = [];
                for (let element in tag_obj) {
                    tag_arr.push([element, tag_obj[element]]);
                }
                tag_arr.sort(function(a, b) {
                    return b[1] - a[1];
                })
                this.allTagsLength = tag_arr.length;
                return tag_arr;
            },
            showAll() {
                this.influencers = this.copy_influencers;
            },
            leftNavTag() {
                return this.startIndexTag === 0;
            },
            rightNavTag() {
                return this.allTagsLength - this.startIndexTag - 5 <= 0;
            },
            leftMoveTag() {
                this.startIndexTag -= 5;
            },
            rightMoveTag() {
                this.startIndexTag += 5;
            },
            filterTag(tagName) {
                // console.log(tagName);
                // console.log(this.copy_influencers[0]["video_list"][0]["label_list"]);
                // console.log(this.copy_influencers[0]["video_list"][1]["label_list"]);
                // console.log(this.copy_influencers[0]["video_list"][2]["label_list"]);
                this.influencers = [];
                for (let k = 0; k < this.copy_influencers.length; k++) {
                    let influencer = this.copy_influencers[k];
                    for (let i = 0; i < influencer["video_list"].length; i++) {
                        if (influencer["video_list"][i]["label_list"].includes(tagName)) {
                            this.influencers.push(influencer)
                            break;
                        }
                    }
                }
                this.startIndex = 1;
                this.showAuthorIndex = 0;
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
    background-color: #aaaaaa;
    font-size: 23px;
}

.searchButton:hover {
    background-color: #525252;
}

.singleAuthor1{
    margin-left: 5%;
    float: left;
    width: 28%;
    height: 400px;
}

.singleAuthor2{
    margin-left: 3%;
    float: left;
    width: 28%;
    height: 400px;
}

.singleAuthor3{
    margin-left: 3%;
    float: left;
    width: 28%;
    height: 400px;
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

.tagButton{
    border: none;
    color: #0000cd;
    background-color:rgba(0, 0, 0, 0);
    cursor: pointer;
    margin-right: 10px;
}

.tagButtons{
    color: #0000cd;
    background-color: white;
    margin-right: 10px;
    border-radius: 10px;
}

.allButton{
    margin-right: 10px;
    border-radius: 10px;
}


.sameBorder {
  --borderWidth: 3px;
  position: relative;
  border-radius: 15px;
}
.sameBorder:after {
  content: '';
  position: absolute;
  top: calc(-1 * var(--borderWidth));
  left: calc(-1 * var(--borderWidth));
  height: calc(100% + var(--borderWidth) * 2);
  width: calc(100% + var(--borderWidth) * 2);
  background: linear-gradient(45deg, #e39e59, #ea7e66, #e26d8d, #c096c9, #748cba, #579faf, #5fc4b2, #85bb94);
  border-radius: 15px;
  z-index: -1;
  animation: animated 3s ease alternate infinite;
  background-size: 300% 300%;
}


@keyframes animated {
	0% {
		background-position: 0 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0 50%;
	}
}
</style>
