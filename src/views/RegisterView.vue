<template>
    <div id="register">
        <form @submit.prevent="signupWithPassword" class="register">
            <div>
                <label class="register-prompt">
                    Username:
                </label>
                <input type="text" v-model="username" class="register-input" />
            </div>
            <div>
                <label class="register-prompt">
                    Password:
                </label>
                <input type="password" v-model="password" class="register-input" />
            </div>
            <div>
                <label class="register-prompt">
                    Verify password:
                </label>
                <input type="password" v-model="passwordVerify" class="register-input" />
            </div>
            <button type="submit" class="button-87">Submit</button>
            <br>
        </form>
        <div id="alert" v-if="alert">{{ alert }}</div>
        <div class="login-at-register">Already have an account? Try&nbsp;<router-link to="/login">login</router-link>
        </div>
    </div>
</template>

<script>
import { UserRegister } from '../api/user';
// same: import { UserRegister } from '@/api/user';

export default {
    data() {
        return {
            username: "",
            password: "",
            passwordVerify: "",
            alert: "",
        };
    },
    methods: {
        signupWithPassword() {
            // Reset the alert to empty
            this.alert = "";
            // Verify that the passwords match
            if (this.password !== this.passwordVerify) {
                this.alert = "Passwords must match";
                return;
            }
            UserRegister(this.username, this.password).then(response => {
                if (response.data.status === 'fail') {
                    this.alert = 'Username already exist!'
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

.register {
    font-size: x-large;
    position: relative;
    top: 100px;
}

.register-input {
    width: 330px;
    border-style: hidden;
    border-radius: 10px;
}

.register-prompt {
    display: inline-block;
    width: 250px;
    text-align: left;
    font-weight: bold;
}

#alert {
    color: red;
    margin-bottom: 10px;
}

.button-87 {
    display: inline-block;
}

.login-at-register {
    margin-top: 100px;
}
</style>