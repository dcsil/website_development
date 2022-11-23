<template>
    <div id="login">
        <form @submit.prevent="loginWithPassword" class="login">
            <div>
                <label class="login-prompt">
                    Email or username:
                </label>
                <input type="text" v-model="emailOrUsername" class="login-input" />
            </div>
            <div>
                <label class="login-prompt">
                    Password:
                </label>
                <input type="password" v-model="password" class="login-input" />
            </div>
            <button type="submit" class="button-87">Log in</button>
            <br>
        </form>
        <div id="alert" v-if="alert">{{ alert }}</div>
        <div class="button-register">New to InfluCo? Try&nbsp;<router-link to="/register">Register</router-link></div>
    </div>
</template>

<script>
// Initialize Userfront
import Userfront from "@userfront/core";
Userfront.init("demo1234");

// If the URL contains token & uuid params, log in
if (
  document.location.search.includes("token=") &&
  document.location.search.includes("uuid=")
) {
  Userfront.login({ method: "link" });
}

export default {
    data() {
        return {
            emailOrUsername: "",
            password: "",
            alert: "",
        };
    },
    methods: {
        loginWithPassword() {
            this.alert = "";
            Userfront.login({
                method: "password",
                emailOrUsername: this.emailOrUsername,
                password: this.password,
            }).catch((error) => {
                this.alert = error.message;
            });
        },
    },
};
</script>

<style>
div {
    margin-bottom: 20px;
}

.login {
    font-size: x-large;
}

.login-input {
    width: 330px;
    border-style: hidden;
    border-radius: 10px;
}

.login-prompt {
    display: inline-block;
    width: 250px;
    text-align: left;
    font-weight: bold;
}

#alert {
    color: red;
    margin-bottom: 10px;
}

.button-register {
    display: inline-block;
    margin-top: 30px;
    padding: 5px 15px;
    font-size:medium;
}
</style>