<template>
  <div id="app">
    <!-- <img src="../assets/INFLUCO.jpg"> -->
    <h1><strong>{{ mainPageMSG1 }}</strong></h1>
    <h2><strong>{{ mainPageMSG2 }}</strong></h2>
    <ul>
      <button class="button-87" role="button" onclick="window.location.href='https://vuejs.org';">Start Browse</button>
    </ul>
    <ul>
      <button class="button-87" role="button" onclick="window.location.href='https://vuejs.org';">Register</button>
    </ul>
    <ul>
      <div>Already having an account? Try&nbsp;</div><a href="http://router.vuejs.org/">login</a>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      mainPageMSG1: 'Welcome to InfluCo!',
      mainPageMSG2: 'The world’s most powerful influencer analysis platform'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 5%;
}

body {
  background-image: url('../assets/mainPageBackground.jpg');
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
  display: flex;
  justify-content: center;
}

a {
  color: #42b983;
}

.button-87 {
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

<!-- <template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->