<template>
  <div class="dashboardPage">
    <div class="d-flex sidebar" id="wrapper">
      <!-- Sidebar -->
      <div class="bg-light border-right" id="sidebar">
        <div class="list-group list-group-flush">
          <a class="list-group-item list-group-item-action bg-light">
            <a href="#" @click="activateAccount" class="navbar-toggler navbar-toggler-account" type="button"
              data-toggle="collapse" data-target="#accountContent" aria-controls="navbarSupportedContent"
              aria-expanded="false" aria-label="Toggle navigation">
              <a><i class="bi-house-door-fill"></i>
                Account
              </a>
            </a>
          </a>
          <div id="accountContent" class="collapse accountContent">
            <a href="#" @click="activateResetUsername" class="list-group-item list-group-item-action bg-light">Reset
              Username</a>
            <a href="#" @click="activateResetPassword" class="list-group-item list-group-item-action bg-light">Reset
              Password</a>
            <a href="#" @click="logout" class="list-group-item list-group-item-action bg-light">Logout</a>
          </div>
          <a href="#" @click="activateHistory" class="list-group-item list-group-item-action bg-light"><i
              class="bi-eye-fill"></i> History</a>
          <a href="#" @click="activateLikes" class="list-group-item list-group-item-action bg-light"><i
              class="bi-heart-fill"></i>
            Favourite</a>
          <a href="#" class="list-group-item list-group-item-action bg-light">About</a>
        </div>
      </div>
    </div>
    <div
      v-if="(!this.likesActivated && !this.historyActivated && !this.resetUsernameActivated && !this.resetPasswordActivated)"
      class="dashboard">
      <div class="dashboardContent">
        <div class="dashboardTitle">Dashboard
        </div>
        <div class="dashboardHistory">
          <hr>
          <div style="font-size: larger;">Recent Viewed
            <div v-if="(historyInfluencers !== [])" class="more">
              <button @click="activateHistory" class="buttonMore">More</button>
            </div>
          </div>
          <div v-for="i in [0, 1, 2]" v-bind:key="i" class="influencerInfo">
            <div v-if="(flagHistoryInfluencers(i))" class="dashboardBox">
              <p class="influencerName">{{
                  historyInfluencers[i]["author_stats"]["nickname"]
              }}
              </p>
              <p>{{ "Author ID: " + historyInfluencers[i]["author_stats"]["id"] }}</p>
              <p>{{ "Follower Count: " +
                  historyInfluencers[i]["author_stats"]["stats"]["followerCount"]
              }}
              </p>
              <!-- 
              <p>{{ "Like Count: " + historyInfluencers[i]["author_stats"]["stats"]["heart"] }}</p>
              <p>{{ "Video Count: " + historyInfluencers[i]["author_stats"]["stats"]["videoCount"] }}
              </p> -->
              <div class="links">
                <p>{{ "Influencer Detail: " }}</p>
                <router-link
                  :to="{ name: 'Detail', params: { author_id: historyInfluencers[i]['author_stats']['id'] } }">{{
                      "@" + historyInfluencers[i]["author_stats"]["id"]
                  }}</router-link>
              </div>
            </div>
          </div>
          <div v-if="(historyInfluencers === [])" class="noRecentData">
            No recent viewed influencers
          </div>
        </div>
        <div class="dashboardFavourite">
          <hr>
          <div style="font-size: larger;"> Recent Favourite
            <div v-if="(likesInfluencers !== [])" class="more">
              <button @click="activateLikes" class="buttonMore">More</button>
            </div>
          </div>
          <div v-for="i in [0, 1, 2]" v-bind:key="i" class="influencerInfo">
            <!-- <a href="#" style="float: right;">...</a> -->
            <div v-if="(flagLikesInfluencers(i))" class="dashboardBox">
              <p class="influencerName">{{
                  likesInfluencers[i]["author_stats"]["nickname"]
              }}
              </p>
              <p>{{ "Author ID: " + likesInfluencers[i]["author_stats"]["id"] }}</p>
              <p>{{ "Follower Count: " +
                  likesInfluencers[i]["author_stats"]["stats"]["followerCount"]
              }}
              </p>
              <!-- 
              <p>{{ "Like Count: " + likesInfluencers[i]["author_stats"]["stats"]["heart"] }}</p>
              <p>{{ "Video Count: " + likesInfluencers[i]["author_stats"]["stats"]["videoCount"] }}
              </p> -->
              <div class="links">
                <p>{{ "Influencer Detail: " }}</p>
                <router-link
                  :to="{ name: 'Detail', params: { author_id: likesInfluencers[i]['author_stats']['id'] } }">{{
                      "@" + likesInfluencers[i]["author_stats"]["id"]
                  }}</router-link>
              </div>
            </div>
          </div>
          <div v-if="(likesInfluencers === [])" class="noRecentData">
            No recent favourite influencers
          </div>
        </div>
      </div>
    </div>
    <div v-if="this.historyActivated">
      <div v-for="i in [showAuthorIndexHistory, showAuthorIndexHistory + 1, showAuthorIndexHistory + 2]" v-bind:key="i"
        class="influencerInfoHistory">

        <div v-if="(flagHistoryInfluencers(i))" class="dashboardBox">
          <p class="influencerName">{{
              historyInfluencers[i]["author_stats"]["nickname"]
          }}
          </p>
          <p>{{ "Author ID: " + historyInfluencers[i]["author_stats"]["id"] }}</p>
          <p>{{ "Follower Count: " +
              historyInfluencers[i]["author_stats"]["stats"]["followerCount"]
          }}
          </p>

          <p>{{ "Like Count: " + historyInfluencers[i]["author_stats"]["stats"]["heart"] }}</p>
          <p>{{ "Video Count: " + historyInfluencers[i]["author_stats"]["stats"]["videoCount"] }}
          </p>
          <div class="links">
            <p>{{ "Influencer Detail: " }}</p>
            <router-link :to="{ name: 'Detail', params: { author_id: historyInfluencers[i]['author_stats']['id'] } }">{{
                "@" + historyInfluencers[i]["author_stats"]["id"]
            }}</router-link>
          </div>
        </div>
      </div>
      <div class="index">
        <button class="indexButton" :disabled="leftNav()"
          v-on:click="leftMove(this.startIndexHistory, this.curPageHistory, 'activeBtnHistory')">{{ "<" }} </button>

            <button class="indexButton" :class="{ active: activeBtnHistory === 0 }"
              :disabled="checkIndex(0, this.historyInfluencers, this.startIndexHistory)"
              v-on:click="showAuthor(0, this.startIndexHistory, 'activeBtnHistory')">{{
                  startIndexHistory
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnHistory === 1 }"
              :disabled="checkIndex(1, this.historyInfluencers, this.startIndexHistory)"
              v-on:click="showAuthor(1, this.startIndexHistory, 'activeBtnHistory')">{{
                  1 +
                  startIndexHistory
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnHistory === 2 }"
              :disabled="checkIndex(2, this.historyInfluencers, this.startIndexHistory)"
              v-on:click="showAuthor(2, this.startIndexHistory, 'activeBtnHistory')">{{
                  2 +
                  startIndexHistory
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnHistory === 3 }"
              :disabled="checkIndex(3, this.historyInfluencers, this.startIndexHistory)"
              v-on:click="showAuthor(3, this.startIndexHistory, 'activeBtnHistory')">{{
                  3 +
                  startIndexHistory
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnHistory === 4 }"
              :disabled="checkIndex(4, this.historyInfluencers, this.startIndexHistory)"
              v-on:click="showAuthor(4, this.startIndexHistory, 'activeBtnHistory')">{{
                  4 +
                  startIndexHistory
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnHistory === 5 }"
              :disabled="rightNav(this.historyInfluencers, this.startIndexHistory)"
              v-on:click="rightMove(this.startIndexHistory, this.curPageHistory, 'activeBtnHistory')">></button>
      </div>
    </div>
    <div v-if="this.likesActivated">
      <div v-for="i in [showAuthorIndexLikes, showAuthorIndexLikes + 1, showAuthorIndexLikes + 2]" v-bind:key="i"
        class="influencerInfoHistory">

        <div v-if="(flagLikesInfluencers(i))" class="dashboardBox">
          <p class="influencerName">{{
              likesInfluencers[i]["author_stats"]["nickname"]
          }}
          </p>
          <p>{{ "Author ID: " + likesInfluencers[i]["author_stats"]["id"] }}</p>
          <p>{{ "Follower Count: " +
              likesInfluencers[i]["author_stats"]["stats"]["followerCount"]
          }}
          </p>

          <p>{{ "Like Count: " + likesInfluencers[i]["author_stats"]["stats"]["heart"] }}</p>
          <p>{{ "Video Count: " + likesInfluencers[i]["author_stats"]["stats"]["videoCount"] }}
          </p>
          <div class="links">
            <p>{{ "Influencer Detail: " }}</p>
            <router-link :to="{ name: 'Detail', params: { author_id: likesInfluencers[i]['author_stats']['id'] } }">{{
                "@" + likesInfluencers[i]["author_stats"]["id"]
            }}</router-link>
          </div>
        </div>
      </div>
      <div class="index">
        <button class="indexButton" :disabled="leftNav()"
          v-on:click="leftMove(this.startIndexLikes, this.curPageLikes, 'activeBtnLikes')">{{ "<" }} </button>

            <button class="indexButton" :class="{ active: activeBtnLikes === 0 }"
              :disabled="checkIndex(0, this.likesInfluencers, this.startIndexLikes)"
              v-on:click="showAuthor(0, this.startIndexLikes, 'activeBtnLikes')">{{
                  startIndexLikes
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnLikes === 1 }"
              :disabled="checkIndex(1, this.likesInfluencers, this.startIndexLikes)"
              v-on:click="showAuthor(1, this.startIndexLikes, 'activeBtnLikes')">{{
                  1 +
                  startIndexLikes
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnLikes === 2 }"
              :disabled="checkIndex(2, this.likesInfluencers, this.startIndexLikes)"
              v-on:click="showAuthor(2, this.startIndexLikes, 'activeBtnLikes')">{{
                  2 +
                  startIndexLikes
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnLikes === 3 }"
              :disabled="checkIndex(3, this.likesInfluencers, this.startIndexLikes)"
              v-on:click="showAuthor(3, this.startIndexLikes, 'activeBtnLikes')">{{
                  3 +
                  startIndexLikes
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnLikes === 4 }"
              :disabled="checkIndex(4, this.likesInfluencers, this.startIndexLikes)"
              v-on:click="showAuthor(4, this.startIndexLikes, 'activeBtnLikes')">{{
                  4 +
                  startIndexLikes
              }}</button>
            <button class="indexButton" :class="{ active: activeBtnLikes === 5 }"
              :disabled="rightNav(this.likesInfluencers, this.startIndexLikes)"
              v-on:click="rightMove(this.startIndexLikes, this.curPageLikes, 'activeBtnLikes')">></button>
      </div>
    </div>
    <div v-if="this.resetUsernameActivated">
      <form @submit.prevent="resetUsername" class="login">
        <div>
          <label class="login-prompt">
            New Username:
          </label>
          <input type="text" v-model="newUsername" class="login-input" />
        </div>
        <button type="submit" class="button-87">Reset</button>
        <br>
      </form>
      <div id="alert" v-if="alert">{{ alert }}</div>
    </div>
    <div v-if="this.resetPasswordActivated">
      <form @submit.prevent="resetPassword" class="login">
        <div>
          <label class="login-prompt">
            New Password:
          </label>
          <input type="text" v-model="newPassword" class="login-input" />
        </div>
        <div>
          <label class="login-prompt">
            Verify New Password:
          </label>
          <input type="text" v-model="newPasswordVerify" class="login-input" />
        </div>
        <button type="submit" class="button-87">Reset</button>
        <br>
      </form>
      <div id="alert" v-if="alert">{{ alert }}</div>
    </div>
  </div>

</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import 'popper.js/dist/umd/popper.min.js';
import 'jquery/dist/jquery.min.js';
import { GetUser, ChangeUsername, ChangePassword } from '../api/user';
import { GetInfluencer } from '@/api/influencer';

export default {

  data() {
    return {
      username: localStorage.getItem('username'),
      history: null,
      likes: null,
      historyInfluencers: [],
      likesInfluencers: [],
      historyActivated: false,
      likesActivated: false,
      resetUsernameActivated: false,
      resetPasswordActivated: false,

      startIndexHistory: 1,
      activeBtnHistory: 0,
      curPageHistory: 1,
      showAuthorIndexHistory: 0,
      startIndexLikes: 1,
      activeBtnLikes: 0,
      curPageLikes: 1,
      showAuthorIndexLikes: 0,

      newUsername: '',
      newPassword: '',
      newPasswordVerify: "",
      alert: '',
    };
  },
  mounted() {
    this.updateData();
  },

  methods: {
    logout() {
      localStorage.clear();
      localStorage.setItem('authenticated', 'false')
      this.$router.push('/').then(() => { this.$router.go() })
    },

    flagLikesInfluencers(index) {
      return this.likesInfluencers[index] !== undefined;
    },

    flagHistoryInfluencers(index) {
      return this.historyInfluencers[index] !== undefined;
    },

    activateAccount() {
      this.newUsername = '',
      this.newPassword = '',
      this.newPasswordVerify = "",
      this.alert = '',
      this.likesActivated = false;
      this.historyActivated = false;
      this.resetUsernameActivated = false;
      this.resetPasswordActivated = false;
    },

    activateLikes() {
      this.newUsername = '',
      this.newPassword = '',
      this.newPasswordVerify = "",
      this.alert = '',
      this.likesActivated = true;
      this.historyActivated = false;
      this.resetUsernameActivated = false;
      this.resetPasswordActivated = false;
    },

    activateHistory() {
      this.newUsername = '',
      this.newPassword = '',
      this.newPasswordVerify = "",
      this.alert = '',
      this.likesActivated = false;
      this.historyActivated = true;
      this.resetUsernameActivated = false;
      this.resetPasswordActivated = false;
    },

    activateResetUsername() {
      this.newUsername = '',
      this.newPassword = '',
      this.newPasswordVerify = "",
      this.alert = '',
      this.likesActivated = false;
      this.historyActivated = false;
      this.resetUsernameActivated = true;
      this.resetPasswordActivated = false;
    },

    activateResetPassword() {
      this.newUsername = '',
      this.newPassword = '',
      this.newPasswordVerify = "",
      this.alert = '',
      this.likesActivated = false;
      this.historyActivated = false;
      this.resetUsernameActivated = false;
      this.resetPasswordActivated = true;
    },

    resetUsername() {
      this.alert = "";
      ChangeUsername(this.username, this.newUsername).then(response => {
        if (response.data.status === 'fail') {
          this.alert = 'Failed to reset username, username already exists'
        } else if (response.data.status === "success") {
          this.username = response.data.username
          this.alert = 'successfully reset username'
          localStorage.setItem('username', this.username)
        } else {
          console.log('error')
        }
      }).catch(err => {
        console.log(err);
      });
    },

    resetPassword() {
      this.alert = "";
      if (this.password !== this.passwordVerify) {
        this.alert = "Passwords must match";
        return;
      }
      ChangePassword(this.username, this.newPassword).then(response => {
        if (response.data.status === 'fail') {
          this.alert = 'Failed to reset password'
        } else if (response.data.status === "success") {
          this.alert = 'successfully reset password'
        } else {
          console.log('error')
        }
      }).catch(err => {
        console.log(err);
      });
    },

    async updateData() {
      await GetUser(this.username).then(response => {
        this.likes = response.data.likes
        this.history = response.data.history
        console.log("this.likes: ", this.likes)
        console.log("this.history: ", this.history)

        for (let i = 0; i < this.likes.length; i++) {
          GetInfluencer(this.likes[i]["influ_id"]).then(response => {
            this.likesInfluencers.push(response.data)
          }).catch(err => {
            console.log(err);
          });
        }
        console.log("this.likesInfluencers: ", this.likesInfluencers)
        for (let j = 0; j < this.history.length; j++) {
          GetInfluencer(this.history[j]["influ_id"]).then(response => {
            this.historyInfluencers.push(response.data)
          }).catch(err => {
            console.log(err);
          });
        }
        console.log("this.historyInfluencers: ", this.historyInfluencers)
      }).catch(err => {
        console.log(err);
      });
    },

    checkIndex(curr, influencers, startIndex) {
      return 3 * (curr + startIndex) - 2 > influencers.length;
    },
    leftNav(startIndex) {
      return startIndex === 1;
    },
    rightNav(influencers, startIndex) {
      return influencers.length - (Math.ceil(startIndex / 5) * 15) <= 0;
    },
    leftMove(startIndex, curPage, activeBtn) {
      if (activeBtn === 'activeBtnHistory') {
        this.startIndexHistory = startIndex - 5;
      }
      else {
        this.startIndexLikes = startIndex - 5;
      }
      if (curPage >= startIndex && curPage < startIndex + 5) {
        if (activeBtn === 'activeBtnHistory') {
          this.activeBtnHistory = curPage - startIndex;
        }
        else {
          this.activeBtnLikes = curPage - startIndex;
        }
      } else {
        if (activeBtn === 'activeBtnHistory') {
          this.activeBtnHistory = -1;
        }
        else {
          this.activeBtnLikes = -1;
        }
      }
    },
    rightMove(startIndex, curPage, activeBtn) {
      if (activeBtn === 'activeBtnHistory') {
        this.activeBtnHistory = -1;
        this.startIndexHistory = startIndex + 5;
      }
      else {
        this.activeBtnLikes = -1;
        this.startIndexLikes = startIndex + 5
      }
      if (curPage >= startIndex && curPage < startIndex + 5) {
        if (activeBtn === 'activeBtnHistory') {
          this.activeBtnHistory = curPage - startIndex;
        }
        else {
          this.activeBtnLikes = curPage - startIndex;
        }
      } else {
        if (activeBtn === 'activeBtnHistory') {
          this.activeBtnHistory = -1;
        }
        else {
          this.activeBtnLikes = -1;
        }
      }
    },
    showAuthor(curr, startIndex, activeBtn) {
      if (activeBtn === 'activeBtnHistory') {
        this.curPageHistory = startIndex + curr;
        this.activeBtnHistory = curr;
        this.showAuthorIndexHistory = 3 * (curr + startIndex - 1);
      }
      else {
        this.curPageLikes = startIndex + curr;
        this.activeBtnLikes = curr;
        this.showAuthorIndexLikes = 3 * (curr + startIndex - 1);
      }
      // curPage = startIndex + curr;
      // activeBtn = curr;
      // showAuthorIndex = 3 * (curr + startIndex - 1);
      console.log("Show authors index from " + (3 * (curr + this.startIndex - 1)) + " to " + (3 * (curr + this.startIndex)))
    },
  }
}
</script>

<style>
.dashboardPage {
  display: grid;
  grid-template-columns: 20% 80%;
  height: 100%;
}

.dashboard {
  text-align: center;
  display: inline-block;
  font-weight: bold;
}

.dashboardContent {
  height: 100%;
  display: grid;
  grid-template-rows: 5% 37% 37%;
}

.dashboardTitle {
  font-size: xx-large;
  vertical-align: middle;
}

.dashboardHistory {
  border: 5px;
}

.dashboardFavourite {
  border: 5px;
}

.influencerInfo {
  margin-left: 3%;
  margin-right: 1%;
  right: 7px;
  float: left;
  width: 28%;
  height: 100%;
}

.influencerInfoHistory {
  font-size: large;
  margin-top: 15%;
  margin-left: 3%;
  margin-right: 1%;
  right: 7px;
  float: left;
  width: 28%;
  height: 30%;
  vertical-align: middle;
}

.influencerName {
  font-style: italic;
  font-size: large;
}

.noRecentData {
  color: grey;
  font-style: italic;
  font-size: xx-large;
}

.more {
  float: right;
}

.buttonMore {
  border-radius: 15px;
  background: rgb(253, 226, 230);
  font-size: medium;
  border: 1px;
  height: 25px;
  width: 60px;
}

.dashboardBox {
  text-align: left;
  --borderWidth: 5px;
  position: relative;
  border-radius: 15px;
}

.dashboardBox:after {
  text-align: left;
  content: '';
  position: absolute;
  top: calc(-3 * var(--borderWidth));
  /* left: calc(-1 * var(--borderWidth)); */
  /* height: 200px; */
  height: calc(100% + var(--borderWidth) * 2);
  width: calc(100% + var(--borderWidth) * 2);
  background: rgb(253, 226, 230);
  /* linear-gradient(45deg,
            #e39e59,
            #ea7e66,
            #e26d8d,
            #c096c9,
            #748cba,
            #579faf,
            #5fc4b2,
            #85bb94); */
  border-radius: 15px;
  z-index: -1;
  /* animation: animated 3s ease alternate infinite; */
  background-size: 300% 300%;
}

#sidebar {
  /* min-height: 100vh; */
  position: fixed;
  height: 100vh;
  margin-left: -15rem;
  -webkit-transition: margin .25s ease-out;
  -moz-transition: margin .25s ease-out;
  -o-transition: margin .25s ease-out;
  transition: margin .25s ease-out;
  font-size: x-large;
  font-weight: bold;
}

#sidebar .sidebar-heading {
  padding: 0.875rem 1.25rem;
  font-size: 1.2rem;
}

.sidebar {
  z-index: 99;
  /* width: 20%; */
}

#sidebar .list-group {
  width: 15rem;
}

.list-group {
  height: 30rem;
}

#wrapper.toggled #sidebar-wrapper {
  margin-left: 0;
}

@media (min-width: 768px) {
  #sidebar {
    margin-left: 0;
  }

  #wrapper.toggled #sidebar {
    margin-left: -15rem;
  }
}

.accountContent {
  font-size: medium;
}

.navbar-toggler-account {
  text-decoration: none;
  font-weight: bold;
  color: black;
}
</style>