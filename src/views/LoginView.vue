<template>
    <div id="login">
        <form @submit.prevent="loginWithPassword" class="login">
            <div>
                <label class="login-prompt">
                    Username:
                </label>
                <input type="text" v-model="username" class="login-input" />
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
        <div class="button-register">New to InfluCo? Try&nbsp;<router-link to="/register">Register</router-link>
        </div>
    </div>
</template>

<script>
import { UserLogin } from '../api/user';

export default {
    name: 'loginView',
    data() {
        return {
            username: "",
            password: "",
            alert: "",
        };
    },
    methods: {
        loginWithPassword() {
            this.alert = "";
            UserLogin(this.username, this.password).then(response => {
                if (response.data.status === 'fail') {
                    this.alert = 'incorrect password'
                } else if (response.data.status === "success") {
                    this.$router.push('/dashboard')
                    this.$emit("authenticated", true)
                    localStorage.setItem('authenticated', 'true')
                    localStorage.setItem('username', this.username)
                } else {
                    console.log('error')
                }
            }).catch(err => {
                console.log(err);
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
    position: relative;
    top: 100px;
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
    margin-top: 100px;
    padding: 5px 15px;
    font-size: medium;
}
</style>