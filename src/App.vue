<template>
  <div id="nav">
    <nav class="container navbar navbar-expand-lg navbar-light bg-light">
      <!-- <div >
        <a class="navbar-brand" href="/"><img src="./assets/INFLUCO.jpg" width="60" height="60">InfluCo</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div> -->

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <a class="navbar-brand" href="/"><img src="./assets/INFLUCO.jpg" width="60" height="60">InfluCo</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="navbar-nav mr-auto">
          <router-link to="/popular" class="nav-item nav-link">Popular</router-link>
          <router-link to="/search" class="nav-item nav-link">Search</router-link>
        </div>
        <!-- <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
          </form> -->
      </div>
      <div class="dashboard-icon">
        <router-link to="/dashboard" class="nav-item nav-link"><i class="bi-person"></i></router-link>
      </div>
    </nav>
  </div>
  <div class="main"><router-view /></div>
</template>

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