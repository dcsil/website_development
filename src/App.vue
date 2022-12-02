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
            <router-link to="/popular" class="nav-item nav-link">Popular</router-link>
          </div>
          <div v-else-if="!this.authenticated">
            <a href="/login" class="nav-item nav-link">Popular</a>
          </div>
          <div v-if="this.authenticated">
            <router-link to="/search" class="nav-item nav-link">Search</router-link>
          </div>
          <div v-else-if="!this.authenticated">
            <a href="/login" class="nav-item nav-link">Search</a>
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
    console.log("this.authenticated: 0", localStorage.getItem('authenticated'))
    return {
      authenticated: (localStorage.getItem('authenticated') === 'true'),
    }
  },

  mounted() {
    this.authenticated = (localStorage.getItem('authenticated') === 'true'),
    console.log("this.authenticated: 1", this.authenticated)
    if (!this.authenticated) {
      console.log("this.authenticated 2: ", this.authenticated)
    }
  },

  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
      console.log("this.authenticated 3: ", this.authenticated)
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
  margin-top: 2%;
}

#nav {
  width: 100%;
  height: 10%;
  top: 0;
  position: fixed;
  text-align: center;
  align-items: center;
  margin-bottom: 0px;
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
  min-height: 40%;
}

.navbar-collapse {
  margin-bottom: 0px;
}

.main {
  margin-top: 250px;
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