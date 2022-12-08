<template>
  <div id="app">
    <div class="home">
      <h1><strong>{{ mainPageMSG1 }}</strong></h1>
      <h2><strong>{{ mainPageMSG2 }}</strong></h2>
      <ul>
        <button class="button-87" role="button" onclick="window.location.href='/search';">Start Browse</button>
      </ul>
      <div>
        <div v-if="!this.authenticated">
          <ul>
            <router-link to="/register" class="button-87">Register</router-link>
          </ul>
          <ul>
            <div>Already have an account? Try&nbsp;</div><router-link v-if="!this.authenticated"
              to="/login">login</router-link>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      authenticated: (localStorage.getItem('authenticated') === 'true'),
      mainPageMSG1: 'Welcome to InfluCo!',
      mainPageMSG2: 'The world’s most powerful influencer analysis platform'
    }
  },
}
</script>

<style>
.main {
  margin-top: 250px;
  height: 100%;
}

.home {
  position: relative;
  top: 100px;
}

body {
  background-image: url('../assets/mainPageBackground.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

a {
  margin: 0px;
}

h1 {
  font-size: 500%;
  font-style: italic;
  font-weight: bold;
}

h2 {
  font-size: 250%;
  font-weight: bold;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  padding: 0;
  margin: 25px;
  display: flex;
  justify-content: center;
}

a {
  color: #42b983;
  margin: 0px;
}

.button-87 {
  width: 200px;
  margin: 10px;
  padding: 15px 30px;
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: white;
  border-radius: 10px;
  display: block;
  border: 0px;
  font-weight: 700;
  box-shadow: 0px 0px 14px -7px #f09819;
  background-image: linear-gradient(45deg, #FF512F 0%, #F09819 51%, #FF512F 100%);
  cursor: pointer;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-87:hover {
  background-position: right center;
  /* change the direction of the change here */
  color: #fff;
  text-decoration: none;
}

.button-87:active {
  transform: scale(0.95);
}
</style>