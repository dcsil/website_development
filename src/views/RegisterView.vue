<template>
    <div id="register">
        <form @submit.prevent="signupWithPassword" class="register">
            <div>
                <label class="register-prompt">
                    Email address:
                </label>
                <input type="text" v-model="email" class="register-input" />
            </div>
            <div>
                <label class="register-prompt">
                    Account name:
                </label>
                <input type="text" v-model="accountName" class="register-input" />
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
        <div class="login-at-register">Already have an account? Try&nbsp;<router-link to="/login">login</router-link></div>
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
            email: "",
            accountName: "",
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
            Userfront.signup({
                method: "password",
                email: this.email,
                password: this.password,
                data: {
                    accountName: this.accountName,
                },
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

.register {
    font-size: x-large;
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
    margin-top: 20px;
}
</style>