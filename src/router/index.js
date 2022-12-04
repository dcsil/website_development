import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/AboutView.vue";
import Search from "@/views/SearchView.vue";
import Popular from "@/views/PopularView.vue";
import Dashboard from "@/views/DashboardView.vue";
import Login from "@/views/LoginView.vue";
import Register from "@/views/RegisterView.vue";
import Detail from "@/views/DetailView.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/popular",
    name: "Popular",
    component: Popular,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/detail/:author_id",
    name: "Detail",
    component: Detail,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;