<template>
  <div id="nav">
    <nav class="container navbar navbar-expand-lg navbar-light bg-light">
      <div>
        <a class="navbar-brand" href="/"><img src="./assets/INFLUCO.jpg" width="60" height="60">InfluCo</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="navbar-nav mr-auto">
          <div v-if="this.authenticated">
            <router-link to="/search" class="nav-item nav-link">Browse</router-link>
          </div>
          <div v-else-if="!this.authenticated">
            <a href="/login" class="nav-item nav-link">Browse</a>
          </div>
        </div>
      </div>
      <div class="dashboard-icon">
        <div v-if="this.authenticated">
          <router-link to="/dashboard" class="nav-item nav-link"><i class="bi-person"></i></router-link>
        </div>
        <div v-else-if="!this.authenticated">
          <a href="/login" class="nav-item nav-link"><i class="bi-person"></i></a>
        </div>
      </div>
    </nav>
  </div>
  <div class="main"><router-view @authenticated="setAuthenticated" /></div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      authenticated: (localStorage.getItem('authenticated') === 'true'),
    }
  },

  mounted() {
    this.authenticated = (localStorage.getItem('authenticated') === 'true');
  },

  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
    },
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
  height: 100%;
}

html {
  height: 100%;
}

body {
  height: 100%;
  margin-top: -105px;
}

#nav {
  width: 100%;
  height: 95px;
  top: 0;
  position: fixed;
  text-align: center;
  align-items: center;
  margin-bottom: 0px;
  z-index: 99;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: whitesmoke;
  background: purple;
  border-radius: .3rem;
}

.navbar {
  min-width: 100%;
  height: 95px;
}

.navbar-collapse {
  margin-bottom: 0px;
}

.dashboard-icon {
  position: fixed;
  right: 20px;
  top: 2%;
  font-size: xx-large;
}

.navbar-brand {
  font-size: xx-large;
  font-family: cursive;
}

.navbar-nav {
  font-size: xx-large;
}
</style>